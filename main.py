from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.routes import board

# Information
# - protection against ddos attacks handle by firewall
# - restriction access not needed

app = FastAPI()

origins = [
    "http://localhost",
    "http://127.0.0.1:5500",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(board.router)


@app.get("/")
async def root():
    return JSONResponse(
        status_code=200,
        content={"message": f"Server is running"},
    )


@app.exception_handler(Exception)
async def general_handler(request: Request):
    return JSONResponse(
        status_code=500,
        content={"message": f"Check the logs, something's odd"},
    )
