from app import db
from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from ..api_1_0 import api
from ..models import User
from ..serializer import user_schema

@api.route('/auth/register', methods=['POST'])
def register():
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']

    user = User(email=email, username=username)
    user.password = password

    db.session.add(user)
    db.session.commit()

    result = user_schema.dump(
        User.query.filter_by(email=email).first()
    )

    return result, 201

@api.route('/auth/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']

    user: User = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({'error': 'invalid email'}), 401
    if not user.verify_password(password):
        return jsonify({'error': 'invalid password'}), 401
    
    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)


@api.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


