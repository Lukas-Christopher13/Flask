from app.models import *
from test import TestClassBase


class TestPlayerClass(TestClassBase):
    banco: Banco = None
    sala: Sala = None
    
    player1: Player = None
    player2: Player = None
    player3: Player = None

    def create_players(self):
        pass