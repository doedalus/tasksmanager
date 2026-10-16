from src.core.db import SessionLocal
from src.schemas.tasks_schemas import CreateTaskSchema
from src.services.tasks_services import delete_all_tasks_service
import pytest


@pytest.fixture
def create_task_payload():
    return CreateTaskSchema(title="test task1", description="some desc", is_completed=False)

@pytest.fixture()
def db():
    with SessionLocal() as db_session:
        yield db_session

@pytest.fixture(autouse=True)
def clear_db(db):
    delete_all_tasks_service(db)