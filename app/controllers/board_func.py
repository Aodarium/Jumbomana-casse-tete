from ..models.Board import Board
import chess.engine

import tomli

with open("pyproject.toml", mode="rb") as configfile:
    config = tomli.load(configfile)

engine = chess.engine.SimpleEngine.popen_uci(config["engine"]["stockfish"])


def get_equal_game() -> str:
    """
    This function generates a random chess position and attempts to move the pieces to an equilibrium state.
    If the equilibrium state is reached, it returns the FEN representation of the chessboard.
    If the equilibrium state is not reached, it recursively calls itself until an equilibrium state is found.

    Returns:
        str: The FEN representation of the chessboard in equilibrium state.
    """

    chessboard = Board(engine)
    chessboard.generate_random_position()
    if chessboard.move_to_equilibrium():
        return chessboard.fen
    else:
        get_equal_game()
    return ""
