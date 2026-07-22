from fastapi.testclient import TestClient

from src import app as app_module


client = TestClient(app_module.app)


def test_unregister_participant_removes_email_from_activity():
    initial_payload = client.get("/activities").json()
    activity_name = "Chess Club"
    participant_email = initial_payload[activity_name]["participants"][0]

    response = client.delete(
        f"/activities/{activity_name}/participants/{participant_email}"
    )

    assert response.status_code == 200
    updated_payload = client.get("/activities").json()
    assert participant_email not in updated_payload[activity_name]["participants"]
