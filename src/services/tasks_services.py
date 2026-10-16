from sqlalchemy.orm import Session
from src.models.tasks_models import Task
from src.repositories.tasks_repositories import create_task, get_tasks, get_task, delete_task, update_task, delete_all_tasks
from src.helpers.mappers import from_model_to_schema
from src.schemas.tasks_schemas import CreateTaskSchema, TaskSchema, UpdateTaskSchema
from src.helpers.exceptions import TaskNotFound


def create_task_service(db: Session, payload: CreateTaskSchema) -> TaskSchema:
    task = Task(
        title=payload.title,
        description=payload.description,
        is_completed=payload.is_completed
    )

    try:
        create_task(db, task)
        db.commit()
    except Exception:
        db.rollback()
        raise

    return from_model_to_schema(task)

def get_tasks_service(db: Session, offset: int = 0, limit: int = 10) -> list[TaskSchema]:
    tasks = get_tasks(db, offset=offset, limit=limit)
    return [from_model_to_schema(task) for task in tasks]

def get_task_service(db: Session, task_id: int) -> TaskSchema:
    task = get_task(db, task_id)

    if task is None:
        raise TaskNotFound(f"Task {task_id} not found")

    return from_model_to_schema(task)

def delete_task_service(db: Session, task_id: int) -> None:
    task = get_task(db, task_id)

    if task is None:
        raise TaskNotFound(f"Task {task_id} not found")

    try:
        delete_task(db, task)
        db.commit()
    except Exception:
        db.rollback()
        raise

def update_task_service(db: Session, task_id: int, payload: UpdateTaskSchema) -> TaskSchema:
    task = get_task(db, task_id)

    if task is None:
        raise TaskNotFound(f"Task {task_id} not found")

    data = payload.model_dump(exclude_unset=True)

    try:
        update_task(db, task, data)
        db.commit()
    except Exception:
        db.rollback()
        raise

    return from_model_to_schema(task)

def delete_all_tasks_service(db: Session) -> None:
    try:
        delete_all_tasks(db)
        db.commit()
    except Exception:
        db.rollback()
        raise