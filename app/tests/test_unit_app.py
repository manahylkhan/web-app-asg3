import pytest
from app import create_app
from models import db


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()


def test_home(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b'Simple Flask app' in res.data


def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200
    data = res.get_json()
    assert data['status'] == 'healthy'


def test_post_message(client):
    res = client.post('/messages', json={'text': 'CI test'})
    assert res.status_code == 201
    data = res.get_json()
    assert data['text'] == 'CI test'


def test_post_empty_message(client):
    res = client.post('/messages', json={'text': ''})
    assert res.status_code == 400


def test_get_messages(client):
    client.post('/messages', json={'text': 'test1'})
    client.post('/messages', json={'text': 'test2'})
    res = client.get('/messages')
    assert res.status_code == 200
    data = res.get_json()
    assert len(data) == 2
