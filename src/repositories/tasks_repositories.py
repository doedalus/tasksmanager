from sqlalchemy.orm import Session
from src.models.tasks_models import Task


def create_task(db: Session, task: Task):
    db.add(task)
    db.flush()

def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Task).offset(skip).limit(limit).all()
