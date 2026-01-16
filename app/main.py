from fastapi import FastAPI
from app.api.routes import rag
from app.vectordb.milvus_client import connect

app = FastAPI(title="RAG Ollama Milvus")

connect()
app.include_router(rag.router)
