import uuid
from datetime import datetime

class Article:
    def __init__(self, title, content, date=None, article_id=None):
        if not title:
            raise ValueError("Title is required")

        self.id = article_id or str(uuid.uuid4())
        self.title = title
        self.content = content
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def update(self, title, content):
        if not title:
            raise ValueError("Title is required")

        self.title = title
        self.content = content

    def to_dict(self):
        return vars(self)

    @staticmethod
    def from_dict(data):
        return Article(
            data["title"],
            data["content"],
            data["date"],
            data["id"]
        )