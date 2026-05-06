from models.user import user
from extensions import db

class UserRepository:

    def save(self, user):
        db.session.add(user)
        db.session.commit()
        return user

    def find_by_email(self, email):
        return user.query.filter_by(email=email).first()

    def find_by_id(self, id):
        return user.query.get(id)