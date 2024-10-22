from app.models.Board import Board
from app.models.GameStack import GameStack
from app.models.api_variables import Fen


def get_equal_game() -> str:
    """
    This function generates a random chess position and attempts to move the pieces to an equilibrium state.
    If the equilibrium state is reached, it returns the FEN representation of the chessboard.
    If the equilibrium state is not reached, it recursively calls itself until an equilibrium state is found.

    Returns:
        str: The FEN representation of the chessboard in equilibrium state.
    """
    game_stack = GameStack()
    return game_stack.fetch_one()


def verify_fen(fen: Fen) -> bool:
    """Verifies that game is in the equilibrium state

    Args:
        fen (Fen): fen to verify

    Returns:
        bool: is the game equal
    """
    return Board().is_board_equal(str(fen.fen))
