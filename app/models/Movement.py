from dataclasses import dataclass


@dataclass
class MovementList:
    """Class representing a list of moves and their scores

    Args:
        centipawn_score (int): Score of the move in centipawns
        pv (list[str]): Principal variation of the move
    """

    centipawn_score: int
    pv: list[str]


@dataclass
class NextMovement:
    """Class representing the next move and its score

    Args:
        centipawn_score (int): Score of the move in centipawns
        pv (str): Principal variation of the move
    """

    centipawn_score: int
    pv: str
