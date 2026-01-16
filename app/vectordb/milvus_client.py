from pymilvus import connections
from app.config.settings import settings

def connect():
    connections.connect(
        alias="default",
        host=settings.MILVUS_HOST,
        port=settings.MILVUS_PORT
    )
