import pytest
import requests

BASE_URL = "https://ru.yougile.com/api-v2"
AUTH_TOKEN = "BEARER TOKEN"  # прикладываю в сообщении, согласно условиям ДЗ


class ApiClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        })

    def post(self, path, json=None, data=None, headers=None, params=None, timeout=None):
        return self.session.post(f"{self.base_url}{path}", json=json, data=data, headers=headers, params=params, timeout=timeout)

    def put(self, path, json=None, data=None, headers=None, params=None, timeout=None):
        return self.session.put(f"{self.base_url}{path}", json=json, data=data, headers=headers, params=params, timeout=timeout)

    def get(self, path, params=None, headers=None, timeout=None):
        return self.session.get(f"{self.base_url}{path}", params=params, headers=headers, timeout=timeout)

    def delete(self, path, params=None, headers=None, timeout=None):
        return self.session.delete(f"{self.base_url}{path}", params=params, headers=headers, timeout=timeout)


@pytest.fixture(scope="session")
def api_client():
    return ApiClient(BASE_URL, AUTH_TOKEN)


@pytest.fixture
def create_project(api_client, delete_project):
    created_project_ids = []

    def _create_project(payload):
        if "title" not in payload:
            raise ValueError(
                "Payload for creating project must contain 'title' field."
            )

        response = api_client.post("/projects", json=payload)
        assert response.status_code == 201, (
            f"Expected status code 201, but got {response.status_code}."
            f" Response: {response.text}"
        )
        project_id = response.json()["id"]
        created_project_ids.append(project_id)
        return project_id

    yield _create_project

    for project_id in created_project_ids:
        try:
            delete_response = delete_project(project_id)
            pass
        except Exception:
            pass

@pytest.fixture
def delete_project(api_client):
    def _delete_project(project_id):
        response = api_client.delete(f"/projects/{project_id}")
        return response

    return _delete_project


@pytest.fixture
def update_project(api_client):
    def _update_project(project_id, payload):
        response = api_client.put(f"/projects/{project_id}", json=payload)
        return response

    return _update_project


@pytest.fixture
def get_project(api_client):
    def _get_project(project_id):
        response = api_client.get(f"/projects/{project_id}")
        return response

    return _get_project
