def test_get_tasks(test_client):
    result = test_client.get('/tasks/')
    assert result.status_code == 200
    assert result.json() == []