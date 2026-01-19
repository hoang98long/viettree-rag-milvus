from pymilvus import (
    FieldSchema, CollectionSchema,
    DataType, Collection
)
from app.vectordb.milvus_client import connect
from app.config.settings import settings

connect()

fields = [
    FieldSchema("id", DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema("embedding", DataType.FLOAT_VECTOR, dim=768),
    FieldSchema("text", DataType.VARCHAR, max_length=2048)
]

schema = CollectionSchema(fields, description="RAG documents")

collection = Collection(
    name=settings.COLLECTION_NAME,
    schema=schema
)

collection.create_index(
    field_name="embedding",
    index_params={
        "metric_type": "COSINE",
        "index_type": "HNSW",
        "params": {"M": 8, "efConstruction": 64}
    }
)

collection.load()   # ⭐⭐⭐ BẮT BUỘC
print("Collection created & loaded")
