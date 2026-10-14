from sqlalchemy.orm import Session
from src.models.tasks_models import Task
from src.repositories.tasks_repositories import create_task, get_tasks
from src.mappers.tasks_mappers import from_model_to_schema
from src.schemas.tasks_schemas import CreateTaskSchema, TaskSchema


def create_task_service(db: Session, payload: CreateTaskSchema) -> TaskSchema:
    task = Task(
        title=payload.title,
        description=payload.description,
        is_completed=payload.is_completed
    )

    create_task(db, task)

    try:
        db.commit()
    except Exception:
        db.rollback()
        raise

    return from_model_to_schema(task)

def get_tasks_service(db: Session, skip: int = 0, limit: int = 10) -> list[TaskSchema]:
    tasks = get_tasks(db, skip=skip, limit=limit)
    return [from_model_to_schema(task) for task in tasks]