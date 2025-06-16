import pytest  # noqa: F401


class TestProjects:
    def test_create_project_positive(self, api_client, create_project):
        payload = {
            "title": "Test Positive",
        }
        project_id = create_project(payload)

        get_response = api_client.get(f"/projects/{project_id}")
        assert get_response.status_code == 200, (
            f"GET after CREATE failed: {get_response.text}"
        )
        assert get_response.json().get("title") == payload["title"], (
            "Title mismatch after creation. GET Response:"
            f" {get_response.text}"
        )

    def test_create_project_negative_missing_required_field(self, api_client):
        payload = {}
        response = api_client.post("/projects", json=payload)
        assert response.status_code == 400, (
            f"Expected status 400, got {response.status_code}."
            f" Response: {response.text}"
        )
        assert (
                "title" in response.text.lower() or
                "bad request" in response.text.lower()
        ), (
            f"Expected error, got {response.text}"
        )

    def test_get_project_positive(self,
                                  api_client, create_project):
        project_title = "Test Project To Get"
        payload = {"title": project_title}
        project_id = create_project(payload)

        response = api_client.get(f"/projects/{project_id}")
        assert response.status_code == 200, (
            f"Expected status 200, got {response.status_code}."
            f" Response: {response.text}"
        )
        response_json = response.json()
        assert response_json("id") == project_id
        assert response_json("title") == project_title

    def test_get_project_negative_invalid_id(self, api_client):
        invalid_id = "nonExistentUUID1234567890"
        response = api_client.get(f"/projects/{invalid_id}")
        assert response.status_code == 404, (
            f"Expected status 404, got {response.status_code}."
            f" Response: {response.text}"
        )
        assert (
                "not found" in response.text.lower() or
                "error" in response.json()
        ), (
            f"Expected not found error, got {response.text}"
        )

    def test_update_project_positive(self, api_client, create_project):
        initial_title = "Project To Update Initial"
        payload_create = {"title": initial_title}
        project_id = create_project(payload_create)

        updated_title = "Updated Project Title Final"
        payload_update = {"title": updated_title}
        response = api_client.put(f"/projects/{project_id}",
                                  json=payload_update)
        assert response.status_code == 200, (
            f"Expected status 200, got {response.status_code}."
            f" Response: {response.text}"
        )

        get_response = api_client.get(f"/projects/{project_id}")
        assert get_response.status_code == 200, (
            f"GET after PUT failed: {get_response.text}"
        )
        assert get_response.json().get("title") == updated_title, (
            f"Title not updated. Response: {get_response.text}"
        )

    def test_update_project_negative_invalid_id(self, api_client):
        invalid_id = "nonExistentUpdateID12345"
        payload_update = {"title": "Error"}
        response = api_client.put(f"/projects/{invalid_id}",
                                  json=payload_update)
        assert response.status_code == 404, (
            f"Expected status 404, got {response.status_code}."
            f" Response: {response.text}"
        )
        assert (
                "not found" in response.text.lower() or
                "error" in response.json()
        ), (
            f"Expected not found error, got {response.text}"
        )
