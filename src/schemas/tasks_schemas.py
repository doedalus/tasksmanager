from datetime import datetime
from pydantic import BaseModel


class TaskSchema(BaseModel):
    id: int
    title: str
    description: str | None
    is_completed: bool
    created_at: datetime


class CreateTaskSchema(BaseModel):
    title: str
    description: str | None
    is_completed: bool = False