from dataclasses import dataclass
import logging
import random
from typing import Optional
import chess
import chess.engine
from .Optimizer import Optimizer, EquilibriumMoveOptimizer, RandomMoveOptimizer

from .MovementList import MovementList
from ..utils.funcs import format_info, generate_random_move_list

logger = logging.getLogger(__name__)


@dataclass
class Board:
    """Class representing the chessboard object

    Args:
        engine: Engine instance
        depth_limit: Depth limit for the search
        time_limit: Time limit for the search
    """

    engine: chess.engine
    depth_limit = 10
    time_limit = 10

    def __post_init__(self):
        self.current_analyse: list[MovementList]
        self.next_move: chess.Move
        self._score: int = 100
        self.chessboard = chess.Board()
        self.score_if_movement: int = None
        self.search_limit = chess.engine.Limit(
            depth=self.depth_limit, time=self.time_limit
        )

    @property
    def score(self) -> int:
        return self._score

    @property
    def fen(self) -> str:
        return self.chessboard.fen()

    def generate_random_position(self):
        """Generate a random position for the chessboard"""
        self.chessboard = chess.Board.from_chess960_pos(random.randint(0, 959))
        for _ in range(random.randint(0, 10)):
            self.analyze_position(
                random_analysis=True,
            )
            move = self.get_next_move(RandomMoveOptimizer)
            self.perform_movement(move)

    def move_to_equilibrium(self) -> bool:
        """Move from the current position to an equilibrium position

        Returns:
            bool: True if the current position is equal and was found within 40 moves
        """
        for _ in range(40):
            self.analyze_position(
                num_moves_to_return=10,
            )
            move = self.get_next_move(EquilibriumMoveOptimizer)
            self.perform_movement(move)
            if self.score == 0:
                return True
        return False

    def get_next_move(self, optimizer_model: Optimizer) -> chess.Move:
        """Perform the next move based on the optimizer

        Args:
            optimizer_model (Optimizer): Model selecting the next move based on its internal strategy model

        Returns:
            chess.Move: Move to perform
        """
        next_move = optimizer_model.pick_next_move_from_list(self.current_analyse)
        self.score_if_movement = next_move.centipawn_score
        self.next_move = chess.Move.from_uci(next_move.pv)

        return self.next_move

    def perform_movement(self, move: Optional[chess.Move] = None) -> None:
        """Perform the given move on the board

        Args:
            move (Optional[chess.Move]): Move to perform. If None, the next move is used
        """
        if not move:
            move = self.next_move
        if self.score_if_movement is not None:
            self._score = self.score_if_movement
            self.score_if_movement = None
        self.chessboard.push(move)

    def analyze_position(
        self, num_moves_to_return: int = 1, random_analysis: bool = False
    ) -> None:
        """Analyze the current position using the engine

        Args:
            num_moves_to_return (int, optional): Number of best moves to return. Defaults to 1.
            random_analysis (bool): Whether movement should be random
        """
        if random_analysis:
            moves = list(self.chessboard.legal_moves)
            self.current_analyse = generate_random_move_list(moves)
            return

        infos = self.engine.analyse(
            self.chessboard, self.search_limit, multipv=num_moves_to_return
        )
        self.current_analyse = [format_info(info) for info in infos]
