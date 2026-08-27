import uuid
from datetime import datetime
from pydantic import BaseModel, Field
from pymongo import AsyncMongoClient
from pymongo.errors import ConnectionFailure, PyMongoError
from app.core.config import settings
from loguru import logger


class Event(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    task_id: str
    status: str
    result: int | None = None
    created_at: datetime = Field(default_factory=datetime.now)


async def get_mongo_connection():
    async with AsyncMongoClient(settings.MONGO_URI) as client:
        try:
            db = client.get_database("event")
            yield db
        except ConnectionFailure as err:
            logger.error(f"Erro de timeout ao tentar conectar ao MongoDB: {err}")
        except PyMongoError as e:
            logger.error(f"Erro interno do PyMongo: {e}")
