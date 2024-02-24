import pytest

import uuid

from app import create_app
from app.ext.db import db
from app.models import *
from flask import Flask


@pytest.fixture()
def app():
    app = create_app("test")

    with app.app_context():
        db.create_all()

        yield app

        db.session.rollback()
        db.drop_all()
    
@pytest.fixture()
def client(app: Flask):
    return app.test_client()

@pytest.fixture()
def pessoa():
    return  {
        "apelido": "fulano",
        "nome": "cicrano",
        "nascimento": "2002-12-02",
        "stack": ["front", "node", "java"]
    }

@pytest.fixture()
def pessoa_id():
    pessoa = Pessoas(
        apelido="fulano",
        nome="cicrano",
        nascimento="2002-12-02",
        stack=["front", "node", "java"]
    )

    db.session.add(pessoa)
    db.session.commit()

    return pessoa.id

def create_pessoas():
    pessoa1 = Pessoas(
        id = uuid.uuid4(),
        apelido="fulano1",
        nome="ana",
        nascimento="2002-12-02",
        stack=["front", "react", "java"]
    )

    pessoa2 = Pessoas(
        id = uuid.uuid4(),
        apelido="fulano do java",
        nome="mariana",
        nascimento="2002-12-02",
        stack=["front", "node"]
    )

    pessoa3 = Pessoas(
        id = uuid.uuid4(),
        apelido="fulana3",
        nome="cicrano3",
        nascimento="2002-12-02",
        stack=["java"]
    )

    db.session.add(pessoa1)
    db.session.add(pessoa2)
    db.session.add(pessoa3)

    db.session.commit()

