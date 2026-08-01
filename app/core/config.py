from typing import Literal
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    REDIS_URL: Literal = "redis://localhost:6379/0"
    CELERY_BROKER_URL: str = REDIS_URL
    CELERY_RESULT_BACKEND: str = REDIS_URL
    CELERY_TASK_SERIALIZER: Literal = "json"
    CELERY_ACCETP_CONTENT: list[str] = ["json"]
    CELERY_RESULT_SERIALIZER: Literal = "json"


settings = Settings()
