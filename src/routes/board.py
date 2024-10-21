from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.controller.board_func import get_equal_game


router = APIRouter(
    prefix="/v1",
    responses={404: {"description": "Not found"}},
)


@router.get("/generateEqualGame")
async def generate_position(nb_moves: int = 10) -> JSONResponse:
    fen = get_equal_game(nb_moves)

    return JSONResponse(
        content={
            "fen": fen,
        }
    )
