from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "../templates"))


router = APIRouter(
    prefix="/display",
    responses={404: {"description": "Page not found"}},
)


@router.get("/equalBoard")
async def generate_position(request: Request):
    """Api endpoint that generates a display with a position for a game"""
    return TEMPLATES.TemplateResponse(
        "board.html",
        {"request": request},
    )
