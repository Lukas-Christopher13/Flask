import unittest

from app.models import *
from app.ext.db import db
from app import create_app


class TestClassBase(unittest.TestCase):
    banco: Banco = None
    sala: Sala = None
    player: Player = None

    def setUp(self):
        self.app = create_app("test")
        self.app.testing = True
        self.client = self.app.test_client()
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.rollback()
        db.drop_all()
        self.app_context.pop()

    def create_player(self):
        self.create_banco()
        self.create_sala()

        self.player = Player(username="test", sala=self.sala)

        db.session.add(self.player)
        db.session.commit()

    def create_sala(self):
        self.create_banco()
        if self.sala is None:
            self.sala = Sala(code="1234", banco=self.banco)

            db.session.add(self.sala)
            db.session.commit()

        return self.sala 

    def create_banco(self):
        if self.banco is None:
            self.banco = Banco(username="test")

            self.banco.set_password("123")

            db.session.add(self.banco)
            db.session.commit()

        return self.banco       