from fastapi.testclient import TestClient

from app.main import app
from app.db import Base, engine


client = TestClient(app)


def setup_module(module):
    Base.metadata.create_all(bind=engine)


def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == 200


def test_index():
    r = client.get("/")
    assert r.status_code == 200


def test_api_sample():
    r = client.get("/api/v1/sample")
    assert r.json()["message"] == "ok"
