import pytest
from app import create_app
from models import db, Message


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
    yield app


def test_message_model(app):
    with app.app_context():
        m = Message(text='hello')
        db.session.add(m)
        db.session.commit()
        assert Message.query.count() == 1
        assert Message.query.first().text == 'hello'
        db.drop_all()
