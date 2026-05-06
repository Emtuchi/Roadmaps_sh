import uuid
from models.user import user

class AuthService:
    def __init__(self, user_repo):
        self.user_repo = user_repo
        self.tokens = {}

    def register(self, name, email, password):
        if self.user_repo.find_by_email(email):
            return {"message": "Email already exists"}, 400

        User = user.create(name, email, password)
        self.user_repo.save(User)

        token = str(uuid.uuid4())
        self.tokens[token] = user.id

        return {"token": token}, 201
    
    def login(self, email, password):
        user = self.user_repo.find_by_email(email)
        
        if not user:
            return {"message": "Invalid credentials"}, 401
        
        if not user.verify_password(password):
            return {"message": "Invalid credentials"}, 401
        
        token = str(uuid.uuid4())
        self.tokens[token] = user.id
        return {"token": token}, 200

    def authenticate(self, token):
        user_id = self.tokens.get(token)
        if not user_id:
            return None
        return self.user_repo.find_by_id(user_id)