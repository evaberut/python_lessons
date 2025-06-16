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

    def post(self, path, **kwargs):
        return self.session.post(f"{self.base_url}{path}", **kwargs)

    def put(self, path, **kwargs):
        return self.session.put(f"{self.base_url}{path}", **kwargs)

    def get(self, path, **kwargs):
        return self.session.get(f"{self.base_url}{path}", **kwargs)

    def delete(self, path, **kwargs):
        return self.session.delete(f"{self.base_url}{path}", **kwargs)


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
        if response.status_code != 201:
            print(f"\nError creating project: Status {response.status_code},"
                  f" Response: {response.text}")
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
            if delete_response.status_code == 204:
                print(f"\nCleaned up project: {project_id}")
            elif delete_response.status_code == 404:
                print(
                    f"\nProject {project_id} not found during cleanup"
                    " (might have been deleted by test or already cleaned)."
                )
            else:
                print(
                    f"\nFailed to cleanup project {project_id}:"
                    f" Status {delete_response.status_code}, Response:"
                    f" {delete_response.text}"
                )
        except Exception as e:
            print(f"\nError during cleanup of project {project_id}: {e}")


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
