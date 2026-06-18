from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Mexico", "Peru", "Portugal", "Spain", "United States"]


def test_cities_for_country():
    response = client.get("/countries/Portugal/cities")
    assert response.status_code == 200
    assert sorted(response.json()) == ["Lisbon", "Porto"]

def test_cities_invalid_country():
    response = client.get("/countries/InvalidCountry/cities")
    assert response.status_code == 404