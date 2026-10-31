def test_get_tasks(test_client, create_task):
    result = test_client.get('/tasks/')
    assert result.status_code == 200
    assert result.json()[0] == create_task.json()

def test_create_task(test_client):
    task = test_client.post("/tasks", json={"title": "test task1", "description": "some desc", "is_completed": False})
    assert task.status_code == 201
    assert task.json()["title"] == "test task1"

def test_get_task(test_client, create_task):
    task = test_client.get(f'/tasks/{create_task.json()["id"]}')
    assert task.status_code == 200

def test_update_task(test_client, create_task):
    task = test_client.patch(f'/tasks/{create_task.json()["id"]}', json={"title": "updated task"})
    assert task.status_code == 200
    assert task.json()["title"] == "updated task"

def test_delete_task(test_client, create_task):
    task = test_client.delete(f'/tasks/{create_task.json()["id"]}')
    assert task.status_code == 204