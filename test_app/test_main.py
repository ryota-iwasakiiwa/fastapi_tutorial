from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

def test_read_item():
    response = client.get("/items/foo", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero"
    }

def test_read_item_bad_token():
    response = client.get("/items/foo", headers={"X-Token": "xxxx"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Inbalid X-Token header"}

def test_read_item_nonexistent_item():
    response = client.get("/items/xxx", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

def test_create_item():
    input_json = {"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"}
    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json=input_json
    )
    assert response.status_code == 200
    assert response.json() == input_json

def test_create_item_bad_token():
    input_json = {"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"}
    response = client.post(
        "/items/",
        headers={"X-Token": "xxxxxxxx"},
        json=input_json
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Inbalid X-Token header"}

def test_create_item_nonexisting_item():
    input_json = {"id": "foo", "title": "Foo Bar", "description": "The Foo Barters"}
    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json=input_json
    )
    assert response.status_code == 409
    assert response.json() == {"detail": "Item already exists"}