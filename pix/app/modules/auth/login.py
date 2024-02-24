from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token

from ...repository.banco_repository import BancoRepository
from ...repository.player_repository import PlayerRepository
from ...repository.sala_repository import SalaRepository

from . import auth

banco_repository = BancoRepository()
player_repository = PlayerRepository()
sala_repositroy = SalaRepository()

@auth.route("/banco-login", methods=["POST"])
def banco_login():
    username = request.json.get("username")
    password = request.json.get("password")

    banco = banco_repository.select(username=username)

    username_and_password_is_valid = (banco is not None) and (banco.check_password(password))

    if username_and_password_is_valid:
        additional_claims = {"role": "banco"}
        access_token = create_access_token(identity=banco.id, additional_claims=additional_claims)
        refresh_token = create_refresh_token(identity=banco.id, additional_claims=additional_claims)

        return jsonify(
            access_token=access_token, 
            refresh_token=refresh_token
        ), HTTPStatus.OK
    
    return jsonify({"msg": "username or password invalid"}), HTTPStatus.UNAUTHORIZED

#Subistituir por um retorna sala
@auth.route("/sala-code", methods=["POST"])
def enter_sala():
    sala_code = request.json.get("code")
    sala = sala_repositroy.select(sala_code)

    if sala is None:
        return jsonify({"msg": "sala inexistente"}), HTTPStatus.NOT_FOUND
    
    return jsonify({"code": f"{sala.code}"})
