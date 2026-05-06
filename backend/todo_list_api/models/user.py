from extensions import db
import hashlib

class user(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(256))
    
    todos = db.relationship("Todo", backref="user", lazy=True)

    @staticmethod
    def create(name, email, password):
        user.validate(name, email, password)
        return user(
            name=name,
            email=email,
            password_hash=user.hash_password(password)
        )
    
    @staticmethod
    def validate(name, email, password):
        if not name or not email or not password:
            raise ValueError("All fields required")

        if "@" not in email:
            raise ValueError("Invalid email")

        if len(password) < 4:
            raise ValueError("Password too short")
    
    def toDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
    
    def getemail(self):
        return self.email
    
    def getid(self):
        return self.id
    
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        return self.password_hash == user.hash_password(password)