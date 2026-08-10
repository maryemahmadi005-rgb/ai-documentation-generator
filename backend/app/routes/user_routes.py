from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.user import User
from werkzeug.security import generate_password_hash

user_bp = Blueprint("users", __name__)


# GET ALL USERS
@user_bp.route("", methods=["GET"])
def get_users():
    users = User.query.all()
    # Dima nsta3mlou to_dict() bech code yabda ndhif
    return jsonify([user.to_dict() for user in users]), 200


# CREATE USER
@user_bp.route("", methods=["POST"])
def create_user():
    data = request.get_json() or {}
    print("DATA RECUE:", data)
    
    if "username" not in data or "email" not in data or "password" not in data:
        return jsonify({"error": "username, email et password sont obligatoires"}), 400
    user = User(
        username=data["username"],
        email=data["email"],
        password_hash=generate_password_hash(
            data["password"]
            ),
            role=data.get("role", "user")
        )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User created",
        "user": user.to_dict()
    }), 201


# UPDATE USER
@user_bp.route("/<int:id>", methods=["PUT"])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json() or {}

    user.username = data.get("username", user.username)
    user.email = data.get("email", user.email)

    if "password_hash" in data:
        user.password_hash = data["password_hash"]

    if "role" in data:
        user.role = data["role"]

    db.session.commit()

    return jsonify({
        "message": "User updated",
        "user": user.to_dict()
    }), 200


# DELETE USER
@user_bp.route("/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get_or_404(id)

    db.session.delete(user)
    db.session.commit()

    return jsonify({
        "message": "User deleted"
    }), 200