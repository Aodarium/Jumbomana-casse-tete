import random
from ..models.MovementList import MovementList, NextMovement


def format_info(info) -> MovementList:
    # Normalize by always looking from White's perspective
    score = info["score"].white()
    centipawn_score = score.score()
    return MovementList(
        centipawn_score=centipawn_score,
        pv=format_moves(info["pv"]),
    )


# Convert the move class to a standard string
def format_moves(pv):
    return [move.uci() for move in pv]


def generate_fake_move_list(moves: list) -> list[MovementList]:
    print(moves)
    return [
        MovementList(
            centipawn_score=0, pv=[random.choice(moves).uci() if moves else None]
        )
        for _ in range(len(moves))
    ]
