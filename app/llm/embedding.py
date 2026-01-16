import requests
from app.config.settings import settings

def embed(text: str) -> list[float]:
    r = requests.post(
        f"{settings.OLLAMA_BASE_URL}/api/embeddings",
        json={
            "model": settings.EMBED_MODEL,
            "prompt": text
        }
    )
    return r.json()["embedding"]
