# app.py

from flask import Flask
from repository.article_repository import ArticleRepository
from services.article_service import ArticleService
from controllers.blog_controller import blog_bp, init_routes

app = Flask(__name__)
app.secret_key = "secret"

# setup dependencies
repo = ArticleRepository("data/articles.json")
service = ArticleService(repo)

# inject service into blueprint
init_routes(service)

# register blueprint
app.register_blueprint(blog_bp)

if __name__ == "__main__":
    app.run(debug=True)