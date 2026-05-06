from extensions import db

class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    @staticmethod
    def create(title, description, user_id):
        if not title:
            raise ValueError("Title is required")

        return Todo(
            title=title,
            description=description,
            user_id=user_id
        )
    
    def updateTitle(self, title):
        self.title = title
    
    def updateDesc(self, description):
        self.description = description
    
    def getid(self):
        return self.id
    
    def getuserId(self):
        return self.user_id
    
    def verifyUserbyId(self, id):
        if self.user_id != id:
            return False
        
        return True
    
    def toDict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.desc
        }