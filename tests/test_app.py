from fastapi.testclient import TestClient

from src import app as app_module


def test_unregister_participant_from_activity():
    client = TestClient(app_module.app)
    original_participants = app_module.activities["Chess Club"]["participants"].copy()

    try:
        response = client.delete(
            "/activities/Chess%20Club/participants/michael@mergington.edu"
        )

        assert response.status_code == 200
        assert "michael@mergington.edu" not in app_module.activities["Chess Club"]["participants"]
    finally:
        app_module.activities["Chess Club"]["participants"] = original_participants
