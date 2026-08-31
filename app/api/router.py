from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from pymongo.asynchronous.database import AsyncDatabase
from pymongo.errors import CollectionInvalid
from app.core.celery_app import celery
from app.core.database import Event, get_mongo_connection
from app.tasks.example_task import add
from app.models.TaskQueue import TaskQueue
from app.models.TaskStatus import TaskStatus

router = APIRouter()


@router.get("/", status_code=200)
def home():
    return "API Running !"


@router.post("/add", status_code=200, response_model=TaskQueue)
async def add_numbers(
    x: int,
    y: int,
    db: AsyncDatabase = Depends(get_mongo_connection),
):
    task = add.delay(x, y)

    event = Event(task_id=task.id, status=str(task.result))

    new_task_queue = TaskQueue(task_id=task.id)
    try:
        collection = db.get_collection("celery_event")
        await collection.insert_one(event.model_dump())
    except CollectionInvalid:
        raise HTTPException(status_code=500, detail="Erro ao criar a collection")

    return new_task_queue


@router.get("/status")
async def get_status_missing_id():
    raise HTTPException(status_code=400, detail="task_id é obrigatório")


@router.get("/status/{task_id}", response_model=TaskStatus)
async def get_status(task_id: str, db: AsyncDatabase = Depends(get_mongo_connection)):
    result = celery.AsyncResult(task_id)

    collection = db.get_collection("celery_event")
    if not await collection.find_one({"task_id": task_id}):
        raise HTTPException(status_code=404, detail="task_id não encontrada !")
    await collection.update_one(
        {
            "task_id": task_id,
        },
        {"$set": {"status": result.status, "result": result.result, "updated_at": datetime.now()}},
    )
    return TaskStatus(task_id=task_id, status=result.status, result=result.result)
