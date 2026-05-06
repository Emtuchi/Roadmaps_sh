from flask import Blueprint, request, jsonify

def create_auth_bp(auth_service):

    auth_bp = Blueprint("auth", __name__)

    @auth_bp.route("/register", methods=["POST"])
    def register():
        data = request.get_json()

        result, status = auth_service.register(
            data["name"],
            data["email"],
            data["password"]
        )

        return jsonify(result), status

    @auth_bp.route("/login", methods=["POST"])
    def login():
        data = request.get_json()

        result, status = auth_service.login(
            data["email"],
            data["password"]
        )

        return jsonify(result), status

    return auth_bp