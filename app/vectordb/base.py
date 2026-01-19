from abc import ABC, abstractmethod

class VectorStore(ABC):

    @abstractmethod
    def add_texts(self, texts: list[str]):
        pass

    @abstractmethod
    def similarity_search(self, query: str, top_k: int):
        pass
