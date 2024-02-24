from app import db
from sqlalchemy import Column, Integer, String
from werkzeug.security import check_password_hash, generate_password_hash

class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(64), unique=True)
    username = Column(String(64), unique=True)
    password_hash = Column(String())

    @property
    def password(self):
        raise AttributeError('password is a not readable atribute!')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    

    