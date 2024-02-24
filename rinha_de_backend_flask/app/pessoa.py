from http import HTTPStatus

from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError

from .models import PessoasModel
from .pessoas_repository import PessoasRepository

pessoa = Blueprint("pessoa", __name__)

pessoa_repository = PessoasRepository()
 
@pessoa.route("/pessoas", methods=["POST"])
def create_pessoas():
    try:
        apelido = request.json["apelido"]
        nome = request.json["nome"]
        nascimento = request.json["nascimento"]
        stack = request.json["stack"]

        pessoa_repository.create(
            apelido=apelido,
            nome=nome,
            nascimento=nascimento,
            stack=stack
        )

        return jsonify({"msg": "pessoa criada"}), HTTPStatus.CREATED
    
    except ValidationError:
        return jsonify({"msg": "tipo invalido"}), HTTPStatus.BAD_REQUEST

    except IntegrityError:
        return jsonify({"msg": "erro ao criar pessoa"}), HTTPStatus.UNPROCESSABLE_ENTITY
    
    except Exception as e:
        return jsonify({"msg": "erro ao criar pessoa"}), HTTPStatus.INTERNAL_SERVER_ERROR

@pessoa.route("/pessoas/<id>", methods=["GET"])
def get_pessoas(id):
    try:
        pessoa = pessoa_repository.get_pessoa(id)

        if pessoa is None:
            return jsonify({"msg": "pessoa não encontrada"}), HTTPStatus.NOT_FOUND

        pessoa_validate = PessoasModel.model_validate(pessoa)
        pessoa_dict = pessoa_validate.model_dump()

        return jsonify(pessoa_dict)
    
    except Exception as e:
        return HTTPStatus.INTERNAL_SERVER_ERROR

@pessoa.route("/pessoas", methods=["GET"])
def find_pessoas_by_termo():
    try:
        termo = request.args.get("t")
        
        if termo is None:
            return jsonify({"msg": "informe o parametro 't'"}), HTTPStatus.BAD_REQUEST

        pessoas = pessoa_repository.get_pessoa_by_termo(termo)

        pessoas_dict = []

        for pessoa in pessoas:
            pessoa_validate = PessoasModel.model_validate(pessoa)
            pessoas_dict.append(pessoa_validate.model_dump())
        
        return jsonify(pessoas_dict)

    except Exception as e:
        return HTTPStatus.INTERNAL_SERVER_ERROR

@pessoa.route("/contagem-pessoas", methods=["GET"])
def count_pessoas():
    num_registros = pessoa_repository.count()

    return f"{num_registros}"
