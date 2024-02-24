from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

loginManager = LoginManager()
loginManager.session_protection = 'strong'
loginManager.login_view = 'auth.login'

bootstrap = Bootstrap5()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    db.init_app(app)
    bootstrap.init_app(app)
    loginManager.init_app(app)

    migrate = Migrate(app, db)

    from .auth import auth_ as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app