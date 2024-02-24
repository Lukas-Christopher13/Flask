from test import TestClassBase

from app.ext.db import db
from app.models import Banco, Sala, Player

class TestBancoClass(TestClassBase):
    banco: Banco = None
    sala: Sala = None
    player: Player = None

    def get_autorization_header(self):
        token = self.get_banco_jwt()
        return {
            "Authorization": f"Bearer {token}"
        }

    def get_banco_jwt(self):
        self.create_banco()

        response = self.client.post("/auth/banco-login", json={
            "username": "test",
            "password": "123"
        })

        jwt = response.get_json()
        return jwt["access_token"]

    def create_salas(self):
        self.create_banco()

        sala1 = Sala(code="1111", banco=self.banco)
        sala2 = Sala(code="2222", banco=self.banco)
        sala3 = Sala(code="3333", banco=self.banco)

        db.session.add(sala1)
        db.session.add(sala2)
        db.session.add(sala3)
        
        db.session.commit()

