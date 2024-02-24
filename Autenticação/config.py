import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'a random string'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:lukas@localhost:5432/flask_data_base'
    