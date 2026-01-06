from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

class Roupa(BaseModel):
    tipo: str
    cor: Optional[str] = None
    tecido: Optional[str] = None

class Avaliacao(BaseModel):
    score: float
    explicacao: str

@app.post("/avaliar", response_model=Avaliacao)
def avaliar(r1: Roupa, r2: Roupa):
    score = 0

    if r1.cor == r2.cor:
        score += 0.5
    if r1.tecido == r2.tecido:
        score += 0.5

    return Avaliacao(
        score=score,
        explicacao=f"Score calculado com base em cor e tecido"
    )
