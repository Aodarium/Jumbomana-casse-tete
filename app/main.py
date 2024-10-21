from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from .routes import board

# Information
# - protection against ddos attacks handle by firewall
# - restriction access not needed

app = FastAPI()

origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(board.router)

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))
app.mount("/img", StaticFiles(directory=str(BASE_PATH / "templates/img")), name="img")

@app.get("/showGame")
async def generate_position(request: Request):
    return TEMPLATES.TemplateResponse(
        "board.html",
        {"request": request},
    )


@app.get("/")
async def root():
    return JSONResponse(
        status_code=200,
        content={"message": f"Server is running"},
    )


# @app.exception_handler(Exception)
# async def general_handler(request: Request, _):
#     return JSONResponse(
#         status_code=500,
#         content={"message": f"Check the logs, something's odd"},
#     )
