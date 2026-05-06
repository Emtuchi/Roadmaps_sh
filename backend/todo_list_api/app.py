from flask import Flask
from extensions import db
from config import config

from repositories.user_repo import UserRepository
from repositories.todo_repo import TodoRepository
from services.auth_service import AuthService
from services.todo_service import TodoService
from controllers.auth_controller import create_auth_bp
from controllers.todo_controller import create_todo_bp

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

user_repo = UserRepository()
todo_repo = TodoRepository()

auth_service = AuthService(user_repo)
todo_service = TodoService(todo_repo)

auth_bp = create_auth_bp(auth_service)
todo_bp = create_todo_bp(todo_service, auth_service)

with app.app_context():
    db.create_all()

# register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(todo_bp)

if __name__ == "__main__":
    app.run(debug=True)