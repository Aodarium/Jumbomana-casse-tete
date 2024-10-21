from src.models.MovementList import MovementList, NextMovement


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
