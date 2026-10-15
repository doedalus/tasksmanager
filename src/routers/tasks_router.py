from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from src.core.db import get_db
from src.helpers.exceptions import TaskNotFound
from src.schemas.tasks_schemas import CreateTaskSchema, TaskSchema, UpdateTaskSchema
from src.services.tasks_services import create_task_service, get_tasks_service, get_task_service, delete_task_service, \
    update_task_service

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

@router.post("/", response_model=TaskSchema, status_code=201)
def create_task(
        payload: CreateTaskSchema,
        db: Session = Depends(get_db)
) -> TaskSchema:

    return create_task_service(db, payload)

@router.get("/", response_model=list[TaskSchema], status_code=200)
def read_tasks(
        limit: int = Query(10, ge=1, le=100),
        offset: int = Query(0, ge=0),
        db: Session = Depends(get_db)
) -> list[TaskSchema]:

    return get_tasks_service(db, offset, limit)

@router.get("/{task_id}", response_model=TaskSchema, status_code=200)
def read_task(
        task_id: int,
        db: Session = Depends(get_db)
) -> TaskSchema:

    try:
        return get_task_service(db, task_id)
    except TaskNotFound as e:
        raise HTTPException(status_code=404, detail="Task not found") from e

@router.delete("/{task_id}", status_code=204)
def delete_task(
        task_id: int,
        db: Session = Depends(get_db)
) -> None:

    try:
        delete_task_service(db, task_id)
    except TaskNotFound as e:
        raise HTTPException(status_code=404, detail="Task not found") from e

@router.patch("/{task_id}", response_model=TaskSchema, status_code=200)
def update_task(
        task_id: int,
        payload: UpdateTaskSchema,
        db: Session = Depends(get_db)
) -> TaskSchema:

    try:
        task = update_task_service(db, task_id, payload)
    except TaskNotFound as e:
        raise HTTPException(status_code=404, detail="Task not found") from e

    return task
