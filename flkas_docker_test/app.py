from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

db = SQLAlchemy()
app = Flask(__name__)

class Pessoa(db.Model):
    __tablename__ = "pessoas"

    id = Column(Integer, primary_key=True)
    nome = Column(String(length=32))

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:lukas@postgresdb/postgres"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    pessoa = Pessoa(nome="fulano")
    db.session.add(pessoa)
    db.session.commit()

    return "hello world"

