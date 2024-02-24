from test import TestClassBase

from app.ext.db import db
from app.models import *


class TestAuthClass(TestClassBase):
    banco: Banco = None
    sala: Sala = None

    def get_banco_tokens(self):
        if self.banco is None:
            self.create_banco()
        
        response = self.client.post("/auth/banco-login", json={
            "username": "test",
            "password": "123"
        })

        return response.get_json()
    
    def get_player_token(self):
        self.create_sala()
        sala_code = self.sala.code

        response = self.client.post(
            f"/player/create/{sala_code}",
            json={
                "username": "test"
            })
        
        return response.get_json()

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