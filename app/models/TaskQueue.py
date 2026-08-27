from pydantic import BaseModel


class TaskQueue(BaseModel):
    task_id: str
    status: str = "em fila"
