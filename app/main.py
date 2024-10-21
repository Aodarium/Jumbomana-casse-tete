from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from .routes import chessgame
from .routes import frontend

# Information
# - protection against ddos attacks handle by firewall
# - restriction access not needed

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


@app.get("/")
async def root():
    return JSONResponse(
        status_code=200,
        content={"message": f"Server is running"},
    )


@app.exception_handler(Exception)
async def general_handler(request: Request, _):
    return JSONResponse(
        status_code=500,
        content={"message": f"Check the logs, something's odd"},
    )
