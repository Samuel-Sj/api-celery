from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    REDIS_URL: str = "redis://localhost:6379/0"
    MONGO_URI: str = "mongodb://localhost:27017"

    CELERY_TASK_SERIALIZER: str = "json"
    CELERY_ACCEPT_CONTENT: list[str] = ["json"]
    CELERY_RESULT_SERIALIZER: str = "json"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def CELERY_BROKER_URL(self) -> str:
        # Sempre segue REDIS_URL (inclusive quando vier de variável de ambiente)
        return self.REDIS_URL

    @property
    def CELERY_RESULT_BACKEND(self) -> str:
        return self.REDIS_URL

    @property
    def MONOGO_URI(self) -> str:
        return self.MONGO_URI

settings = Settings()