from flask import Flask

from config import config

from .ext.db import db


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    from .pessoa import pessoa as pessoa_blueprint
    app.register_blueprint(pessoa_blueprint)

    return app
