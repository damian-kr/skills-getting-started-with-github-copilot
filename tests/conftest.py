from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture()
def client():
    """Create a test client with reset in-memory activity state for each test."""
    original_activities = deepcopy(activities)

    activities.clear()
    activities.update(deepcopy(original_activities))

    with TestClient(app) as test_client:
        yield test_client

    activities.clear()
    activities.update(deepcopy(original_activities))
