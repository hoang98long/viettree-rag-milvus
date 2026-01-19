import faiss
import pickle
import os
import numpy as np
from app.llm.embedding import embed
from app.vectordb.base import VectorStore

INDEX_PATH = "data/faiss/index.faiss"
TEXT_PATH = "data/faiss/texts.pkl"

class FaissStore(VectorStore):
    def __init__(self, dim: int = 768):
        self.dim = dim
        os.makedirs("data/faiss", exist_ok=True)

        if os.path.exists(INDEX_PATH):
            self.index = faiss.read_index(INDEX_PATH)
            self.texts = pickle.load(open(TEXT_PATH, "rb"))
        else:
            self.index = faiss.IndexFlatIP(dim)
            self.texts = []

    def add_texts(self, texts: list[str]):
        vectors = [embed(t) for t in texts]
        vectors = np.array(vectors).astype("float32")

        self.index.add(vectors)
        self.texts.extend(texts)

        faiss.write_index(self.index, INDEX_PATH)
        pickle.dump(self.texts, open(TEXT_PATH, "wb"))

    def similarity_search(self, query: str, top_k: int = 3):
        q_vec = np.array([embed(query)]).astype("float32")
        scores, indices = self.index.search(q_vec, top_k)

        return [self.texts[i] for i in indices[0] if i != -1]
