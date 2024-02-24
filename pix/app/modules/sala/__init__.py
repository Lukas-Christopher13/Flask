from http import HTTPStatus
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from ...schemas import SalaSchema
from ...repository.sala_repository import SalaRepository


sala = Blueprint("sala", __name__)

sala_repository = SalaRepository()

@sala.route("/", methods=["GET"])
@jwt_required()
def get_salas():
    pass

@sala.route("/", methods=["POST"])
@jwt_required()
def create_salas():
    pass

@sala.route("/<code>", methods=["GET"])
#@jwt_required()
def get_sala(code):
    sala = sala_repository.select(code)

    if sala is None:
        return jsonify({"msg": "sala not found"}), HTTPStatus.NOT_FOUND
    
    sala_schema = SalaSchema()
    sala_json = sala_schema.dump(sala)

    return jsonify(sala_json)

@sala.route("/<code>", methods=["PUT"])
@jwt_required()
def update_sala(code):
    pass

@sala.route("/<code>", methods=["DELETE"])
@jwt_required()
def delete_sala(code):
    pass
