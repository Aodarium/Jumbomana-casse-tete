from abc import abstractmethod
from dataclasses import dataclass
from src.models.MovementList import MovementList, NextMovement


@dataclass
class Optimizer:
    @staticmethod
    def pick_next_move_from_list(list_next_moves: list[MovementList]) -> NextMovement:
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
    @staticmethod
    def pick_next_move_from_list(list_next_moves: list[MovementList]) -> NextMovement:
        raise NotImplementedError


@dataclass
class EquilibriumMoveOptimizer(Optimizer):
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
