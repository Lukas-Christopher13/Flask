from . import auth
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

@auth.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identify = get_jwt_identity()
    access_token = create_access_token(identity=identify)
    return jsonify(access_token=access_token)
