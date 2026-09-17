import uuid
from datetime import datetime
from pydantic import BaseModel, Field
from pymongo import AsyncMongoClient
from pymongo.errors import ConnectionFailure, PyMongoError
from app.core.config import settings
from loguru import logger
from fastapi import HTTPException


class Event(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    task_id: str
    status: str
    result: int | None = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime | None = Field(default_factory=datetime.now)

class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    username: str
    password: str


def get_mongo_connection(db_name: str):
    async def _get_db():
        async with AsyncMongoClient(settings.MONGO_URI) as client:
            try:
                db = client.get_database(db_name)
                yield db
            except ConnectionFailure as err:
                logger.error(f"Erro de timeout ao tentar conectar ao MongoDB: {err}")
                raise HTTPException(status_code=503, detail="Serviço de banco de dados indisponível")
            except PyMongoError as e:
                logger.error(f"Erro interno do PyMongo: {e}")
                raise HTTPException(status_code=500, detail="Erro interno do banco de dados")
    return _get_db