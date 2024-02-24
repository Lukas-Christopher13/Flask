from flask import Blueprint

api = Blueprint('api', __name__)

from . import autentication, comment, errors, posts, users
