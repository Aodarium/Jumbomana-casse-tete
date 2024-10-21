from dataclasses import dataclass
import logging
import random
from typing import Optional
import chess
import chess.engine
from src.models.Optimizer import EquilibriumMoveOptimizer

from src.models.MovementList import MovementList
from src.models.Optimizer import Optimizer
from src.utils.funcs import format_info

logger = logging.getLogger(__name__)


@dataclass
class Board:
    engine: chess.engine
    depth_limit = 10
    time_limit = 10

    def __post_init__(self):
        self.current_analyse: list[MovementList]
        self.board: chess.Board
        self.next_move: chess.Move
        self._score: int = 100
        self.board = chess.Board()
        self.score_if_movement: int = None
        self.search_limit = chess.engine.Limit(
            depth=self.depth_limit, time=self.time_limit
        )

    @property
    def score(self) -> int:
        return self._score

    @property
    def fen(self) -> str:
        return self.board.fen()

    def generate_random_position(self, number_of_movements):
        for _ in range(number_of_movements):
            move = self.get_random_move()
            self.perform_movement(move)

    def move_to_equilibrium(self) -> bool:
        for _ in range(40):
            self.analyze_position(
                num_moves_to_return=10,
            )
            move = self.get_next_move(EquilibriumMoveOptimizer)
            self.perform_movement(move)
            if self.score == 0:
                return True
        return False

    def get_random_move(self):
        moves = list(self.board.legal_moves)
        return random.choice(moves) if moves else None

    def get_next_move(self, optimizerModel: Optimizer) -> chess.Move:
        next_move = optimizerModel.pick_next_move_from_list(self.current_analyse)
        self.score_if_movement = next_move.centipawn_score
        self.next_move = chess.Move.from_uci(next_move.pv)

        return self.next_move

    def perform_movement(self, move: Optional[chess.Move] = None) -> None:
        if not move:
            move = self.next_move
        if self.score_if_movement is not None:
            self._score = self.score_if_movement
            self.score_if_movement = None
        self.board.push(move)

    def analyze_position(
        self,
        num_moves_to_return: int = 1,
    ) -> None:
        infos = self.engine.analyse(
            self.board, self.search_limit, multipv=num_moves_to_return
        )
        self.current_analyse = [format_info(info) for info in infos]
