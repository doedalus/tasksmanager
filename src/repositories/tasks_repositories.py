from sqlalchemy.orm import Session
from src.models.tasks_models import Task


def create_task(db: Session, task: Task):
    db.add(task)
    db.flush()

def get_tasks(db: Session, offset: int = 0, limit: int = 10):
    return db.query(Task).offset(offset).limit(limit).all()

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).one_or_none()

def delete_task(db: Session, task: Task):
    db.delete(task)

def update_task(db: Session, task: Task, data: dict):

    for key, value in data.items():
        setattr(task, key, value)

    db.flush()