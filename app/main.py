from fastapi import FastAPI
from app.core.rag_pipeline import rag_answer

app = FastAPI(title="RAG Ollama FAISS")

@app.post("/rag")
def rag(q: str):
    return {"answer": rag_answer(q)}
