from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import *
from config import Config

app = Flask(__name__)
app.config.from_object(Config())

db = SQLAlchemy()
db.init_app(app)

bootstrap = Bootstrap5()
migrate = Migrate(app, db)

def create_app():
    
    bootstrap.init_app(app)

    from .views import home_page
    app.register_blueprint(home_page)

    return app
