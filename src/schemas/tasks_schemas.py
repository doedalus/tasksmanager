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
    description: str | None = None
    is_completed: bool = False


class UpdateTaskSchema(BaseModel):
    title: str | None = None
    description: str | None = None
    is_completed: bool | None = None