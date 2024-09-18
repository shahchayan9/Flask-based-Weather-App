import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_weather(client):
    response = client.get('/weather?city=London')
    assert response.status_code == 200
    data = response.get_json()
    assert 'city' in data
    assert 'current_time' in data
    assert 'description' in data
    assert 'icon' in data
    assert 'temperature' in data