from sqlalchemy import Boolean, Column, Integer, String, orm
from sqlalchemy.dialects import postgresql

from .ext.data_base import db


class User(db.Model):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(64))
    email = Column(String, unique=True)
    password_hash = Column(String(512))
    adm = Column(Boolean)

class Cartela(db.Model):
    __tablename__ = "cartela"

    id = Column(Integer, primary_key=True)
    cartela = Column(postgresql.ARRAY(Integer), unique=True)
    cartela_batida = Column(Boolean, default=False)

    #to do ralachiso chip

    def __init__(self) -> None:
        self.cartela = self.__criar_cartela()    
        
    def __criar_cartela(self):
        cartela_factory = CartelaFactory()
        return cartela_factory.criar_matriz_da_cartela()
    
    def __eq__(self, other) -> bool:
        for linha in range(5):
            for coluna in range(5):
                if self.cartela[linha][coluna] != other.cartela[linha][coluna]:
                    return False
        return True

from random import sample


#rerfatorar
class CartelaFactory:
    NUM_BOLAS = 75
    TAMANHO = 5

    RANGE_B = (1, 15)
    RANGE_I = (16, 30)
    RANGE_N = (31, 45)
    RANGE_G = (46, 60)
    RANGE_O = (61, 75)

    def __init__(self) -> None:
        self.matriz = []
        self.range = [self.RANGE_B, self.RANGE_I, self.RANGE_N, self.RANGE_G, self.RANGE_O]

    def criar_matriz_da_cartela(self):
        for intervalo in self.range:
            self.matriz.append(self.criar_linha(intervalo))
        return self.matriz

    def criar_linha(self, intervalo):
        linha = sample(range(intervalo[0], intervalo[1]), self.TAMANHO)
        linha.sort()
        return linha

