from flask import Blueprint, request, jsonify
from database.db import users_table

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    users_table.insert(data)
    return jsonify({"message": "User created"}), 201

@users_bp.route('/users', methods=['GET'])
def list_users():
    return jsonify(users_table.all())
