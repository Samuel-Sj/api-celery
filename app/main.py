from fastapi import FastAPI

from app.api.router import router

app = FastAPI(
    title="API Celery",
    description="API simples para trabalhar com Celery, Redis e outros conceitos de backend !",
)

app.include_router(router=router)