from pydantic import BaseModel


class Fen(BaseModel):
    fen: str
