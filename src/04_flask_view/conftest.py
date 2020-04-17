import pytest

from app import app


@pytest.fixture
def client():
    client = app.test_client()
    yield client
