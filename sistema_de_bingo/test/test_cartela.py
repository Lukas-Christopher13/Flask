import unittest
from app.models import Cartela


CARTELA_1 = [
        [1, 2, 3, 4, 5],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]

CARTELA_2 = [
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]

class TestCartela(unittest.TestCase):
    def setUp(self):
        self.cartela = Cartela()
        self.cartela_igual = Cartela()
        self.cartela_diferente = Cartela()

        self.cartela.cartela = CARTELA_1
        self.cartela_igual.cartela = CARTELA_1
        self.cartela_diferente.cartela = CARTELA_2

    def test_cartelas_iguais(self):
        self.assertTrue(self.cartela == self.cartela_igual)
    
    def test_cartelas_diferentes(self):
        self.assertFalse(self.cartela == self.cartela_diferente)

