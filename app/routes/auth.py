from flask import Blueprint, jsonify, request
from app.utils.jwt import jwt
from app.utils.db import db
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.User import User

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/sign_in', methods=['POST'])
def register():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({'message': 'username and password are required'}), 400
    
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'user created successfully'}), 201

@auth.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({'message': 'username and password are required'}), 400

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'invalid username or password'}), 401

    access_token = create_access_token(identity=user.id)

    return jsonify({'access_token': access_token}), 200

@auth.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()

    return jsonify({'message': f'Hello, {user.username}!'}), 200