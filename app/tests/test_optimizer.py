import pytest
from app.models.Movement import MovementList
from app.models.Optimizer import EquilibriumMoveOptimizer, RandomMoveOptimizer


@pytest.mark.parametrize(
    "list_next_moves,selection, centipawn_score",
    [
        (
            [
                MovementList(centipawn_score=10, pv=["d4"]),
                MovementList(centipawn_score=20, pv=["c4"]),
                MovementList(centipawn_score=30, pv=["e4"]),
            ],
            "d4",
            10,
        ),
        (
            [
                MovementList(centipawn_score=30, pv=["e4"]),
                MovementList(centipawn_score=20, pv=["c4"]),
                MovementList(centipawn_score=10, pv=["d4"]),
            ],
            "d4",
            10,
        ),
        (
            [
                MovementList(centipawn_score=-30, pv=["e4"]),
                MovementList(centipawn_score=-20, pv=["c4"]),
                MovementList(centipawn_score=10, pv=["d4"]),
            ],
            "d4",
            10,
        ),
        (
            [
                MovementList(centipawn_score=-30, pv=["e4"]),
                MovementList(centipawn_score=0, pv=["c4"]),
                MovementList(centipawn_score=10, pv=["d4"]),
            ],
            "c4",
            0,
        ),
    ],
)
def test_equilibrium_move_optimizer_pick_next_move_from_list(
    list_next_moves, selection, centipawn_score
):

    result_move = EquilibriumMoveOptimizer.pick_next_move_from_list(list_next_moves)

    assert result_move.centipawn_score == centipawn_score
    assert result_move.pv == selection


def test_random_move_optimizer_pick_next_move_from_list():
    list_next_moves = [
        MovementList(centipawn_score=0, pv=["d4"]),
        MovementList(centipawn_score=0, pv=["c4"]),
    ]
    result_move = RandomMoveOptimizer.pick_next_move_from_list(list_next_moves)

    assert result_move.centipawn_score == 0
