from src.models.Board import Board
import chess.engine

import tomli

with open("config.toml", mode="rb") as configfile:
    config = tomli.load(configfile)

engine = chess.engine.SimpleEngine.popen_uci(config["Engine"]["stockfish"])


def get_equal_game(nb_moves: int) -> str:
    chessboard = Board(engine)
    chessboard.generate_random_position(nb_moves)
    if chessboard.move_to_equilibrium():
        return chessboard.fen
    else:
        get_equal_game(nb_moves)
