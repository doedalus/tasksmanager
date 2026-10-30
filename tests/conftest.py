from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.tasks_models import Base
from src.schemas.tasks_schemas import CreateTaskSchema
from src.services.tasks_services import delete_all_tasks_service, create_task_service
from src.core.settings import settings
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.core.db import get_db

database_url = settings.test_database_url
engine = create_engine(database_url)
SessionLocal = sessionmaker(bind=engine)


@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

@pytest.fixture
def create_task_payload():
    return CreateTaskSchema(title="test task1", description="some desc", is_completed=False)

@pytest.fixture()
def db():
    with SessionLocal() as db_session:
        yield db_session

@pytest.fixture()
def test_client(db):
    def override_get_db():
        yield db
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()

@pytest.fixture(autouse=True)
def clear_db(db):
    delete_all_tasks_service(db)
    yield
    delete_all_tasks_service(db)

@pytest.fixture
def created_task(db, create_task_payload):
    return create_task_service(db, create_task_payload)