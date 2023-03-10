from app import index, app
import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello_world_message_from_index():
    assert index() == 'Hello there'


def test_hello_world_message_from_client(client):
    response = client.get('/')
    assert response.data.decode('UTF-8') == 'Hello World'
