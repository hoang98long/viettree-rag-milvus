from pymilvus import (
    FieldSchema, CollectionSchema,
    DataType, Collection
)
from app.config.settings import settings

def get_collection():
    return Collection(settings.COLLECTION_NAME)
