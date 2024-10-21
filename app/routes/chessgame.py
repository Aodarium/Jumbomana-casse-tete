from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from ..controllers.board_func import get_equal_game


router = APIRouter(
    prefix="/v1",
    responses={404: {"description": "Not found"}},
)


@router.get("/generateEqualGame")
async def generate_position() -> JSONResponse:
    """Api endpoint that generates a position for a game where
    the pieces are moved to an equilibrium state.

    Returns:
        JSONResponse
    """

    fen = get_equal_game()

    return JSONResponse(
        content={
            "fen": fen,
        }
    )
