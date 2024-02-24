from . import player

from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import jwt_required

from ...repository.player_repository import PlayerRepository

player_repository = PlayerRepository()

@player.route("/pagar/<username>", methods=["POST"])
@jwt_required()
def pagar(username):
    player = player_repository.select(username)
    amount = request.json.get("amount")

    if player is None:
        return jsonify({"msg": "esse player não existe"}), HTTPStatus.UNAUTHORIZED
    
    player_repository.add_money(username, amount)
    
    return jsonify({"msg": "valor recebido"}), HTTPStatus.OK

@player.route("/receber/<username>", methods=["POST"])
@jwt_required()
def pagar_(username):
    pass

#amount



