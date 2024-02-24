import unittest

from app.models import CartelaFactory

class TestCarTelaFactory(unittest.TestCase):

    def setUp(self) -> None:
        self.cartela_factory = CartelaFactory()

    def test_cria_linha(self):
        linha = self.cartela_factory.criar_linha((1, 15))

        self.assertIsNotNone(linha)

    def test_criar_cartela(self):
        cartela = self.cartela_factory.criar_matriz_da_cartela()

        self.assertIsNotNone(cartela)

