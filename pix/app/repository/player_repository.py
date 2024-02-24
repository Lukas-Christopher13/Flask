from ..ext.db import db
from ..models import Player

class PlayerRepository:
    def select(sefl, username):
        player = db.session.query(Player).filter(Player.username == username).first()
        return player

    def select_all(self):
        data = db.session.query(Player).all()
        return data
    
    def add(self, username, sala):
        player = Player(username=username, sala=sala)
        
        db.session.add(player)
        db.session.commit()

    def delete(self, username):
        db.session.query(Player).filter(Player.username == username).delete()
        db.session.commit()

    def add_money(self, username, amount):
        db.session.query(Player) \
            .filter(Player.username == username) \
            .update(money=Player.money + amount)
        
        db.session.commit()
            
