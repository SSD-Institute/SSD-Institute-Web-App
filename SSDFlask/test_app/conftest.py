import pytest
from app import app

@pytest.fixture
def client():
   app.server.config.update({"TESTING": True})
   with app.server.test_client() as client:
      yield client