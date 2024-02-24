from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from ...repository.banco_repository import BancoRepository
from ...repository.player_repository import PlayerRepository
from ...repository.sala_repository import SalaRepository
from ...schemas import PlayerSchema, SalaSchema

from . import banco

sala_repository = SalaRepository()
banco_repository = BancoRepository()
player_repository = PlayerRepository()

@banco.route("/criar_sala", methods=["POST"])
@jwt_required()
def criar_sala():
    identity = get_jwt_identity()

    banco = banco_repository.select(id=identity)
    code = request.json.get("code")

    sala_is_created = sala_repository.add(code, banco)

    if(sala_is_created):
        return jsonify({"msg": "sala criada!"}), 201
    return jsonify({"msg": "essa sala já foi criada!"}), 401

@banco.route("/deletar_sala/<code>", methods=["DELETE"])
@jwt_required()
def deletar_sala(code):
    sala = sala_repository.select(code)

    if(sala is not None):
        sala_repository.delete(code)
        return jsonify({"msg": "sala deletada"}), 200

    return jsonify({"msg": "code invalido"})

@banco.route("/listar_salas", methods=["GET"])
@jwt_required()
def listar_salas():
    sala_schema = SalaSchema()
    salas = sala_repository.select_all()
    
    json_list = [sala_schema.dump(sala) for sala in salas]

    return jsonify(json_list), 200

#Talvez eu deva mover essa rota pra outro lugar, tipo uma rota 'players'
@banco.route("/get_player/<username>", methods=["GET"])
@jwt_required()
def get_player(username):
    player_schema = PlayerSchema()
    player = player_repository.select(username)

    if player is None:
        return jsonify({"msg": "player não cadastrado"})

    player_json = player_schema.dump(player)

    return jsonify(player_json)

@banco.route("/start/<sala_code>", methods=["POST"])
@jwt_required()
def start(sala_code):
    sala = sala_repository.select(sala_code)

    if(len(sala.players) < 2):
        return jsonify({"msg": "jogadores insuficientes"}), 401
    
#criando as rotas crud do banco
    
