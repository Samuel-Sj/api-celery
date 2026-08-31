from pydantic import BaseModel

class TaskStatus(BaseModel):
    task_id: str
    status: str
    result: int | None