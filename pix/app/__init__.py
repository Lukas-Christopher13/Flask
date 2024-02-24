from flask import Flask

from config import config

from .ext.db import db
from .ext.marshmallow import ma
from .ext.jwt_extendend import jwt


def create_app(config_name="development"):
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)

    #docs
    from .ext.swagger_iu import banco_swagger_blueprint
    app.register_blueprint(banco_swagger_blueprint)

    from .ext.swagger_iu import player_swagger_blueprint
    app.register_blueprint(player_swagger_blueprint, name="da")

    #blueprints
    from .modules.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    from .modules.banco import banco as banco_blueprint
    app.register_blueprint(banco_blueprint, url_prefix="/banco")

    from .modules.player import player as player_bluerprint
    app.register_blueprint(player_bluerprint, url_prefix="/player")

    from .modules.sala import sala as sala_blueprint
    app.register_blueprint(sala_blueprint, url_prefix="/sala")

    return app