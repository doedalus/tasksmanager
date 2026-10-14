from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from src.core.db import get_db
from src.helpers.exceptions import TaskNotFound
from src.schemas.tasks_schemas import CreateTaskSchema, TaskSchema
from src.services.tasks_services import create_task_service, get_tasks_service, get_task_service

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

@router.post("/", response_model=TaskSchema)
def create_task(payload: CreateTaskSchema, db: Session = Depends(get_db)) -> TaskSchema:
    return create_task_service(db, payload)

@router.get("/", response_model=list[TaskSchema])
def read_tasks(limit: int = Query(10, ge=1, le=100), skip: int = Query(0, ge=0), db: Session = Depends(get_db)) -> list[TaskSchema]:
    return get_tasks_service(db, skip, limit)

@router.get("/{task_id}", response_model=TaskSchema)
def read_task(task_id: int, db: Session = Depends(get_db)) -> TaskSchema:

    try:
        return get_task_service(db, task_id)
    except TaskNotFound as e:
        raise HTTPException(status_code=404, detail="Task not found") from e

