from app import db
from sqlalchemy import Column, Integer, String, ForeignKey
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(64), unique=True, index=True)
    username = Column(String(64), unique=True, index=True)
    password_hash = Column(String(500))
    role_id = Column(Integer, ForeignKey('role.id'))

    def __repr__(self) -> str:
        return f'User: {self.username}'
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


from app import loginManager

@loginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))