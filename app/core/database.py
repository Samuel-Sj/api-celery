import uuid
from datetime import datetime

from pydantic import BaseModel, Field
from pymongo import MongoClient

from app.core.config import settings


class Event(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    task_id: str
    status: str
    result: int | None = None
    created_at: datetime = Field(default_factory=datetime.now)


client = MongoClient(settings.MONGO_URI)

db = client.get_database("event")

collection = db.get_collection("celery_event")
