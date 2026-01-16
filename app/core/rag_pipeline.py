from app.llm.embedding import embed
from app.llm.ollama_client import generate
from app.vectordb.collections import get_collection
from app.core.prompt import build_prompt

def retrieve(query: str, top_k: int = 3):
    col = get_collection()
    q_emb = embed(query)

    res = col.search(
        data=[q_emb],
        anns_field="embedding",
        param={"metric_type": "COSINE"},
        limit=top_k,
        output_fields=["text"]
    )

    return [hit.entity.get("text") for hit in res[0]]

def rag_answer(question: str) -> str:
    ctx = retrieve(question)
    prompt = build_prompt("\n".join(ctx), question)
    return generate(prompt)
