from http import HTTPStatus

from flask import Blueprint
from flask import jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token

from ...repository.sala_repository import SalaRepository
from ...repository.player_repository import PlayerRepository

player = Blueprint("player", __name__)

sala_repository = SalaRepository()
player_repository = PlayerRepository()


@player.route("/create/<code>", methods=["POST"])
def create_player(code):
    sala = sala_repository.select(code)

    if sala is None:
        return jsonify({"msg": "sala inexistente"}), HTTPStatus.NOT_FOUND
    
    username = request.json.get("username")
    player_repository.add(username, sala)

    additional_claims = {"role": "player"}
    
    access_token = create_access_token(identity=username, additional_claims=additional_claims)
    refresh_token = create_refresh_token(identity=username, additional_claims=additional_claims)

    return jsonify(access_token=access_token, refresh_token=refresh_token), HTTPStatus.OK

from . import actions
