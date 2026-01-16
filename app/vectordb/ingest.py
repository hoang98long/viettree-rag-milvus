from app.llm.embedding import embed
from app.vectordb.collections import get_collection

def ingest(texts: list[str]):
    col = get_collection()
    vectors = [embed(t) for t in texts]

    col.insert([
        vectors,
        texts
    ])
    col.load()
