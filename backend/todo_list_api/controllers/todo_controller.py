from flask import Blueprint, request, jsonify
from middleware.middleware import authenticate

def create_todo_bp(todo_service, auth_service):

    todo_bp = Blueprint("todo", __name__)

    @todo_bp.route("/todos", methods=["POST"])
    def create_todo():
        user = authenticate(request, auth_service)

        if not user:
            return jsonify({"message": "Unauthorized"}), 401

        data = request.get_json()

        todo = todo_service.create(
            data["title"],
            data["description"],
            user.id
        )

        return jsonify({
            "id": todo.id,
            "title": todo.title,
            "description": todo.description
        }), 201

    @todo_bp.route("/todos", methods=["GET"])
    def get_todos():
        user = authenticate(request, auth_service)

        if not user:
            return jsonify({"message": "Unauthorized"}), 401

        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 10))

        return jsonify(todo_service.get_all(user.id, page, limit))

    @todo_bp.route("/todos/<int:id>", methods=["PUT"])
    def update_todo(id):
        user = authenticate(request, auth_service)

        if not user:
            return jsonify({"message": "Unauthorized"}), 401

        data = request.get_json()

        result, status = todo_service.update(
            id,
            data["title"],
            data["description"],
            user.id
        )

        return jsonify(result), status

    @todo_bp.route("/todos/<int:id>", methods=["DELETE"])
    def delete_todo(id):
        user = authenticate(request, auth_service)

        if not user:
            return jsonify({"message": "Unauthorized"}), 401

        status = todo_service.delete(id, user.id)

        return "", status

    return todo_bp