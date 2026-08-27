from fastapi import APIRouter, Depends, HTTPException
from pymongo.asynchronous.database import AsyncDatabase
from pymongo.errors import CollectionInvalid
from app.core.celery_app import celery
from app.core.database import Event, get_mongo_connection
from app.tasks.example_task import add

router = APIRouter()


@router.post("/add",status_code=200)
async def add_numbers(
    x: int, y: int, db: AsyncDatabase = Depends(get_mongo_connection)
):
    task = add.delay(x, y)

    event = Event(task_id=task.id, status=str(task.result))
    try:
        collection = db.get_collection("celery_event")
        await collection.insert_one(event.model_dump())
    except CollectionInvalid:
        raise HTTPException(status_code=500,detail="Erro ao criar a collection")

    return {"task_id": task.id, "status": "em fila"}


@router.get("/status/{task_id}")
async def get_status(task_id: str):
    result = celery.AsyncResult(task_id)
    if not result:
        raise HTTPException(status_code=404, detail="task_id não encontrada !")
    return {
        "task_id": task_id,
        "status": result.status,
        "result": result.result if result.ready() else None,
    }
