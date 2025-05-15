import pytest
import requests

BASE_URL = "https://api.yougile.com/api-v2"  # Замени на актуальный URL, если отличается

@pytest.fixture
def api_client():
    """Фикстура для создания HTTP-клиента Requests."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_TOKEN"  # Замени на свой токен
    }
    return requests.Session()

@pytest.fixture
def create_project(api_client):
    """Фикстура для создания проекта."""
    def _create_project(payload):
        response = api_client.post(f"{BASE_URL}/projects", json=payload)
        assert response.status_code == 201
        return response.json()["id"]
    return _create_project

@pytest.fixture
def get_project(api_client):
    """Фикстура для получения информации о проекте."""
    def _get_project(project_id):
        response = api_client.get(f"{BASE_URL}/projects/{project_id}")
        return response
    return _get_project

@pytest.fixture
def update_project(api_client):
    """Фикстура для обновления проекта."""
    def _update_project(project_id, payload):
        response = api_client.put(f"{BASE_URL}/projects/{project_id}", json=payload)
        return response
    return _update_project

@pytest.fixture
def delete_project(api_client):
    """Фикстура для удаления проекта."""
    def _delete_project(project_id):
        response = api_client.delete(f"{BASE_URL}/projects/{project_id}")
        return response
    return _delete_project