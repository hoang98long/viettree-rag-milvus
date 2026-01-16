from pydantic import BaseSettings

class Settings(BaseSettings):
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    LLM_MODEL: str = "qwen2.5:7b"
    EMBED_MODEL: str = "nomic-embed-text"

    MILVUS_HOST: str = "localhost"
    MILVUS_PORT: int = 19530
    COLLECTION_NAME: str = "rag_docs"

settings = Settings()
