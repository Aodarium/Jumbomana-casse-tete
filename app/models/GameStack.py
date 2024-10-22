from dataclasses import dataclass, field
from threading import Thread

from app.models.Board import Board


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
@dataclass
class GameStack:
    """Class representing the game stack

    Args:
        list_of_positions (list[str]): List of FEN representations of the game positions
    """

    list_of_positions: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.populate(2)

    def populate(self, nb_of_positions_to_add: int = 1):
        """Populates the list with new random positions and moves them to an equilibrium state"""
        for _ in range(nb_of_positions_to_add):
            try:
                self.list_of_positions.append(self.load_one_of_position())
            except Exception as e:
                pass

    def load_one_of_position(self) -> str:
        """Loads a new random position and moves it to an equilibrium state"""
        chessboard = Board()
        chessboard.generate_random_position()
        if chessboard.move_to_equilibrium():
            if chessboard.is_board_equal(chessboard.fen):
                return chessboard.fen
            else:
                self.load_one_of_position()
        else:
            self.load_one_of_position()
        return ""

    def fetch_one(self) -> str:
        """Fetches one position and removes it from the list"""
        Thread(target=self.populate, args={2}).start()
        return self.list_of_positions.pop(0)
