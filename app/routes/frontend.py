from fastapi import APIRouter, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter(
    prefix="/display",
    responses={404: {"description": "Page not found"}},
)

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "../templates"))

print(BASE_PATH)
router.mount(
    "/display/img",
    StaticFiles(directory=str(BASE_PATH / "../templates/img"), html=True),
)


@router.get("/showGame")
async def generate_position(request: Request):
    return TEMPLATES.TemplateResponse(
        "board.html",
        {"request": request},
    )
