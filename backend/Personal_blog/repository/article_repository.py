import json
import os
from models.article import Article

class ArticleRepository:
    def __init__(self, file_path):
        self.file_path = file_path
        self._ensure_file()

    def _ensure_file(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def find_all(self):
        with open(self.file_path, "r") as f:
            return [Article.from_dict(a) for a in json.load(f)]

    def save_all(self, articles):
        with open(self.file_path, "w") as f:
            json.dump([a.to_dict() for a in articles], f, indent=4)