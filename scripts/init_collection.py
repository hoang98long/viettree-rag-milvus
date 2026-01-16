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

schema = CollectionSchema(fields)
Collection(settings.COLLECTION_NAME, schema)
