from app import db
from app.models.produto import Produto

class ProdutosRepository:
    def insert(self, name, quantidade, fornecedor):
        data_insert = Produto(name=name, quantidade=quantidade, fornecedor=fornecedor)
        db.session.add(data_insert)
        db.session.commit()

    def select(self):
        data = db.session.query(Produto).all()
        return data