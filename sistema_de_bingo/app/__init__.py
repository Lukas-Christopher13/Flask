from flask import Flask

from config import config

from .ext.data_base import db
from .ext.admin import admin
from .user.admin import admin_config


def create_app(config_name="developmnet"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    admin.init_app(app)

    #admin
    admin_config()
    
    #blueprints
    from .views import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix="/user")

    return app