# cspell: words autouse, autoflush

import os

from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists, drop_database
from api.db import get_db

from api.db import Base
from api.main import app


@pytest.fixture(scope="function", autouse=True)
def client():
    DB_URL = "%s://%s:%s@%s/%s" % (
        os.environ["DB_DRIVER"],
        os.environ["DB_USER"],
        os.environ["DB_PASSWORD"],
        os.environ["DB_HOST"],
        os.environ["DB_NAME"] + "_test",
    )

    db_engine = create_engine(DB_URL, echo=True)

    if database_exists(DB_URL):
        drop_database(DB_URL)

    create_database(DB_URL)

    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

    Base.metadata.create_all(bind=db_engine)

    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    test_client = TestClient(app)

    yield test_client

    drop_database(DB_URL)


def test_create_item(client):
    # Arrange(準備)

    # Act(実行)
    response = client.post(
        "/item",
        json={"name": "バナナ", "price": 1000},
    )

    # Assert(検証)
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "バナナ", "price": 1000}


def test_read_item(client):
    # Arrange(準備)
    client.post(
        "/item",
        json={"name": "バナナ", "price": 1000},
    )

    # Act(実行)
    response = client.get("/item/1")

    # Assert(検証)
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "バナナ", "price": 1000}


def test_update_item(client):
    # Arrange(準備)
    create_response = client.post(
        "/item",
        json={"name": "バナナ", "price": 1000},
    )

    # Act(実行)
    update_response = client.put(
        "/item/1",
        json={"name": "バナナ", "price": 2000},
    )

    # Assert(検証)
    assert update_response.status_code == 200

    response = client.get("/item/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "バナナ", "price": 2000}


def test_delete_item(client):
    # Arrange(準備)
    client.post(
        "/item",
        json={"name": "バナナ", "price": 1000},
    )

    # Act(実行)
    delete_response = client.delete(
        "/item/1",
    )

    # Assert(検証)
    assert delete_response.status_code == 200

    response = client.get("/item/1")
    assert response.status_code == 404
