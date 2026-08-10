from flask import Blueprint, request, jsonify
from app.models.user import User
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token


auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route(
    "/login",
    methods=["POST"]
)
def login():

    data = request.get_json() or {}


    email = data.get("email")
    password = data.get("password")


    user = User.query.filter_by(
        email=email
    ).first()


    if not user:
        return jsonify({
            "error":"Email ou mot de passe incorrect"
        }),401



    if not check_password_hash(
        user.password_hash,
        password
    ):
        return jsonify({
            "error":"Email ou mot de passe incorrect"
        }),401



    token = create_access_token(
        identity=user.id
    )


    return jsonify({

        "token": token,

        "user": user.to_dict()

    }),200