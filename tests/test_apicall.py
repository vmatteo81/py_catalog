from fastapi.testclient import TestClient
from sources.Main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_list_prizes_valid():
    response = client.get("/api/catalogs/3/prizes")
    assert response.status_code == 200
    data = response.json()
    assert "total" in data
    assert "prizes" in data
    assert isinstance(data["total"], int)
    assert isinstance(data["prizes"], list)
    assert len(data["prizes"]) > 0
    assert "id" in data["prizes"][0]
    assert "title" in data["prizes"][0]
    assert "description" in data["prizes"][0]
    assert "image" in data["prizes"][0]

def test_list_prizes_with_id_filter():
    response = client.get("/api/catalogs/2/prizes?filter.id=1")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 1
    assert len(data["prizes"]) == 1
    assert data["prizes"][0]["id"] == 1

def test_list_prizes_invalid_filter_value():
    response = client.get("/api/catalogs/1/prizes?filter.id=test")
    assert response.status_code == 422
    data = response.json()
    assert "detail" in data
    error_messages = [detail["msg"] for detail in data["detail"]]
    assert "Input should be a valid integer, unable to parse string as an integer" in error_messages

def test_list_prizes_catalog_not_found():
    response = client.get("/api/catalogs/999/prizes")
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Catalog not found"
