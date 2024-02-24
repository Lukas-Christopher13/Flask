from flask import Blueprint

auth_ = Blueprint('auth', __name__)

from . import views