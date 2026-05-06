from models.todo import Todo
from extensions import db

class TodoRepository:

    def save(self, todo):
        db.session.add(todo)
        db.session.commit()
        return todo

    def find_by_id(self, id):
        return Todo.query.get(id)

    def delete(self, todo):
        db.session.delete(todo)
        db.session.commit()

    def find_by_user(self, user_id):
        return Todo.query.filter_by(user_id=user_id).all()