from dataclasses import dataclass, field
from threading import Thread

from app.models.Board import Board
from app.models.Errors import NoPositionYetError


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
                if len(self.list_of_positions) < 5:
                    self.list_of_positions.append(self.load_one_of_position())

    def load_one_of_position(self, nb_attempt: int = 1) -> str:
        """Loads a new random position and moves it to an equilibrium state"""
        chessboard = Board()
        chessboard.generate_random_position()
        if chessboard.move_to_equilibrium():
            return chessboard.fen
        if nb_attempt < 10:
            self.load_one_of_position(nb_attempt + 1)
        return ""

    def fetch_one(self) -> str:
        """Fetches one position and removes it from the list"""
        if len(self.list_of_positions) < 5:
            Thread(target=self.populate, args={10}).start()
        if len(self.list_of_positions) == 0:
            raise NoPositionYetError
        game = self.list_of_positions.pop(0)
        return game
