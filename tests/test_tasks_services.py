from src.services.tasks_services import create_task_service


def test_create_task(db, create_task_payload):
    created_task = create_task_service(db, create_task_payload)

    assert created_task.id is not None
    assert created_task.title == create_task_payload.title
    assert created_task.description == create_task_payload.description
    assert created_task.is_completed == create_task_payload.is_completed
