from ..ext.db import db
from ..models import Banco

class BancoRepository:
    def select(self, id=None, username=None):
        if(username is None):
            banco = db.session.query(Banco).filter(Banco.id == id).first()
            return banco

        banco = db.session.query(Banco).filter(Banco.username == username).first()
        return banco

    def select_all(self):
        data = db.session.query(Banco).all()
        return data
    
    def add(self, username, password):
        banco = Banco(username=username)
        banco.set_password(password)

        db.session.add(banco)
        db.session.commit()
    
    def delete(self, id):
        db.session.query(Banco).filter(Banco.id == id).delete()
        db.session.commit()
    
    def update(self, id, username):
        db.session.query(Banco).filter(Banco.id == id).update({"username": username})
