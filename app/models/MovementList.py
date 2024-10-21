from dataclasses import dataclass


@dataclass
class MovementList:
    centipawn_score: int
    pv: list[str]


@dataclass
class NextMovement:
    centipawn_score: int
    pv: str
