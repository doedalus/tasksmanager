from src.services.tasks_services import create_task_service, get_task, get_tasks_service, delete_task_service, update_task_service
from src.schemas.tasks_schemas import UpdateTaskSchema

def test_create_task(db, create_task_payload):
    created_task = create_task_service(db, create_task_payload)

    assert created_task.id is not None
    assert created_task.title == create_task_payload.title
    assert created_task.description == create_task_payload.description
    assert created_task.is_completed == create_task_payload.is_completed

def test_get_task_by_id(db, created_task):
    task = get_task(db, created_task.id)

    assert task.id == created_task.id
    assert task.title == created_task.title
    assert task.description == created_task.description

def test_get_tasks(db, created_task):
    tasks = get_tasks_service(db)

    assert len(tasks) == 1
    assert created_task.id == tasks[0].id

def test_delete_task(db, created_task):
    delete_task_service(db, created_task.id)
    tasks = get_tasks_service(db)

    assert len(tasks) == 0

def test_update_task(db, created_task):
    update_task_schema = UpdateTaskSchema(title="Updated title")
    updated_task = update_task_service(db, created_task.id, update_task_schema)

    assert updated_task.title == "Updated title"
    assert updated_task.description == created_task.description
    assert updated_task.is_completed == created_task.is_completed



