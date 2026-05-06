from models.todo import Todo

class TodoService:
    def __init__(self, repo):
        self.repo = repo

    def create(self, title, description, user_id):
        todo = Todo.create(title, description, user_id)
        return self.repo.save(todo)

    def update(self, id, title, description, user_id):
        todo = self.repo.find_by_id(id)

        if not todo:
            return {"message": "Not Found"}, 404

        if todo.user_id != user_id:
            return {"message": "Forbidden"}, 403

        todo.update(title, description)
        self.repo.save(todo)

        return todo, 200

    def delete(self, id, user_id):
        todo = self.repo.find_by_id(id)

        if not todo:
            return 404

        if todo.user_id != user_id:
            return 403

        self.repo.delete(todo)
        return 204

    def get_all(self, user_id, page, limit):
        todos = self.repo.find_by_user(user_id)

        total = len(todos)
        start = (page - 1) * limit
        end = start + limit

        return {
            "data": [
                {
                    "id": t.id,
                    "title": t.title,
                    "description": t.description
                } for t in todos[start:end]
            ],
            "page": page,
            "limit": limit,
            "total": total
        }