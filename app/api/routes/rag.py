from fastapi import APIRouter
from app.core.rag_pipeline import rag_answer

router = APIRouter()

@router.post("/rag")
def rag(q: str):
    return {"answer": rag_answer(q)}
