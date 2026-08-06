from datetime import datetime
from fastapi import APIRouter
from app.core.celery_app import celery
from app.tasks.example_task import add

router = APIRouter()

@router.post("/add")
async def add_numbers(x:int, y:int):
    task = add.delay(x,y)

    return {"task_id": task.id, "status":"em fila", "data": datetime.now()}


@router.get("/status/{task_id}")
async def get_status(task_id: str):
    result = celery.AsyncResult(task_id)
    return {
        "task_id":task_id,
        "status": result.status,
        "result": result.result if result.ready else None
    }   