from flask import Flask

from .ext.db import db

from config import config


app = Flask(__name__)

def create_app(config_name="develpmente"):

    app.config.from_object(config[config_name])

    db.init_app(app)

    from .modules.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app