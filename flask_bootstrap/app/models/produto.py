from sqlalchemy import Column, Integer, String
from app import db

class Produto(db.Model):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)
    fornecedor = Column(String, nullable=False)
