import pytest

from flask import Flask

from app import create_app
from app.ext.db import db
from app.modules.home.models import *

@pytest.fixture()
def app():
    app = create_app("develpmente")

    with app.app_context():
        db.create_all()
        
    yield app

    #db.drop_all()

@pytest.fixture()
def cliente(app: Flask):
    return app.test_client()
