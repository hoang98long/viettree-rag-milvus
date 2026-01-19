from app.vectordb.faiss_store import FaissStore

docs = [
    "RAG là kỹ thuật kết hợp truy hồi và sinh văn bản",
    "FAISS là thư viện tìm kiếm vector hiệu năng cao",
    "Ollama cho phép chạy LLM local"
]

store = FaissStore()
store.add_texts(docs)

print("Ingest done")
