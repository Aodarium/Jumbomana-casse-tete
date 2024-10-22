from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from app.models.Errors import FenError, NoMovementError, NoPositionYetError

from .routes import chessgame, frontend


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(chessgame.router)
app.include_router(frontend.router)

BASE_PATH = Path(__file__).resolve().parent
app.mount(
    "/display",
    StaticFiles(directory=str(BASE_PATH / "./templates"), html=True),
)


@app.get("/isRunning")
async def root():
    """API endpoint that returns if the server is running"""
    return JSONResponse(
        status_code=200,
        content={"message": f"Server is running"},
    )


@app.exception_handler(NoMovementError)
async def no_movement_handler(request: Request, _):
    """Returns an error for no movement available"""
    return JSONResponse(
        status_code=400,
        content={"message": f"No more move is available"},
    )


@app.exception_handler(NoPositionYetError)
async def no_movement_handler(request: Request, _):
    """Returns an error for no movement available"""
    return JSONResponse(
        status_code=429,
        content={"message": f"No more position is available"},
    )


@app.exception_handler(FenError)
async def no_movement_handler(request: Request, _):
    """Return an error for an invalid Fen"""
    return JSONResponse(
        status_code=400,
        content={"message": f"Fen is not valid"},
    )


@app.exception_handler(Exception)
async def general_handler(request: Request, _):
    return JSONResponse(
        status_code=500,
        content={"message": f"Check the logs, something's odd"},
    )
