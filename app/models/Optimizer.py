from dataclasses import dataclass
import random
from .Movement import MovementList, NextMovement


@dataclass
class Optimizer:
    """Base class for optimizers"""

    @staticmethod
    def pick_next_move_from_list(list_next_moves: list[MovementList]) -> NextMovement:
        """Select the next move based on the list of moves and a strategy

        Args:
            list_next_moves (list[MovementList]): List of moves

        Returns:
            NextMovement: Selected move
        """
        raise NotImplementedError


@dataclass
class BestMoveOptimizer(Optimizer):
    @staticmethod
    def pick_next_move_from_list(list_next_moves: list[MovementList]) -> NextMovement:
        raise NotImplementedError


@dataclass
class WorstMoveOptimizer(Optimizer):
    @staticmethod
    def pick_next_move_from_list(list_next_moves: list[MovementList]) -> NextMovement:
        raise NotImplementedError


@dataclass
class RandomMoveOptimizer(Optimizer):
    """Optimizer that always selects a random move"""

    @staticmethod
    def pick_next_move_from_list(list_next_moves: list[MovementList]) -> NextMovement:
        move = random.choice(list_next_moves)
        return NextMovement(0, move.pv[0])


@dataclass
class EquilibriumMoveOptimizer(Optimizer):
    """Optimizer that always selects the move with the closest to 0 score"""

    @staticmethod
    def pick_next_move_from_list(list_next_moves: list[MovementList]) -> NextMovement:
        current_move = ""
        current_score = 1_000
        for move in list_next_moves:
            if abs(move.centipawn_score) <= abs(current_score):
                current_score = move.centipawn_score
                current_move = move.pv[0]
            else:
                break
        return NextMovement(current_score, current_move)
