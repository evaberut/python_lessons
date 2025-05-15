import pytest
import json

class TestProjects:
    def test_create_project_positive(self, api_client):
        """Позитивный тест создания проекта."""
        payload = {
            "name": "Test Project Positive",
            "description": "This is a positive test project."
            # Добавьте другие обязательные поля, если есть
        }
        response = api_client.post(f"{BASE_URL}/projects", json=payload)
        assert response.status_code == 201
        assert "id" in response.json()
        assert response.json()["name"] == "Test Project Positive"

    def test_create_project_negative_missing_required_field(self, api_client):
        """Негативный тест создания проекта с отсутствующим обязательным полем (name)."""
        payload = {
            "description": "This project is missing a name."
        }
        response = api_client.post(f"{BASE_URL}/projects", json=payload)
        assert response.status_code == 400  # Или другой ожидаемый код ошибки
        assert "error" in response.json()

    def test_get_project_positive(self, api_client, create_project):
        """Позитивный тест получения информации о проекте."""
        project_name = "Test Project To Get"
        payload = {"name": project_name}
        project_id = create_project(payload)
        response = api_client.get(f"{BASE_URL}/projects/{project_id}")
        assert response.status_code == 200
        assert response.json()["id"] == project_id
        assert response.json()["name"] == project_name

    def test_get_project_negative_invalid_id(self, api_client):
        """Негативный тест получения информации о проекте с невалидным ID."""
        invalid_id = "invalid_project_id"
        response = api_client.get(f"{BASE_URL}/projects/{invalid_id}")
        assert response.status_code == 404  # Или другой ожидаемый код ошибки
        assert "error" in response.json()

    def test_update_project_positive(self, api_client, create_project):
        """Позитивный тест обновления проекта."""
        initial_name = "Project To Update"
        payload_create = {"name": initial_name}
        project_id = create_project(payload_create)
        updated_name = "Updated Project Name"
        payload_update = {"name": updated_name}
        response = api_client.put(f"{BASE_URL}/projects/{project_id}", json=payload_update)
        assert response.status_code == 200
        assert response.json()["id"] == project_id
        assert response.json()["name"] == updated_name

    def test_update_project_negative_invalid_id(self, api_client):
        """Негативный тест обновления проекта с невалидным ID."""
        invalid_id = "invalid_project_id"
        payload_update = {"name": "Will Not Be Updated"}
        response = api_client.put(f"{BASE_URL}/projects/{invalid_id}", json=payload_update)
        assert response.status_code == 404  # Или другой ожидаемый код ошибки
        assert "error" in response.json()