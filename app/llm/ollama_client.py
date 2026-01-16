import requests
from app.config.settings import settings

def generate(prompt: str) -> str:
    r = requests.post(
        f"{settings.OLLAMA_BASE_URL}/api/generate",
        json={
            "model": settings.LLM_MODEL,
            "prompt": prompt,
            "stream": False
        }
    )
    return r.json()["response"]
