from ..ext.db import db
from ..models import Sala

class SalaRepository:
    def select(self, code):
        sala = db.session.query(Sala).filter(Sala.code == code).first()
        return sala

    def select_all(self):
        data = db.session.query(Sala).all()
        return data
    
    def add(self, code, banco):
        sala = Sala(code=code, banco=banco)
        try:
            db.session.add(sala)
            db.session.commit()
            return True
        except:
            return False
  
    def delete(self, code):
        db.session.query(Sala).filter(Sala.code == code).delete()
        db.session.commit()

    


   