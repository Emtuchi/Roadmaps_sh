from models.article import Article

class ArticleService:
    def __init__(self, repo):
        self.repo = repo

    def list_articles(self):
        return self.repo.find_all()

    def get_article(self, article_id):
        for article in self.repo.find_all():
            if article.id == article_id:
                return article
        return None

    def create_article(self, title, content):
        articles = self.repo.find_all()

        article = Article(title, content)
        articles.append(article)

        self.repo.save_all(articles)
        return article

    def update_article(self, article_id, title, content):
        articles = self.repo.find_all()

        for article in articles:
            if article.id == article_id:
                article.update(title, content)

        self.repo.save_all(articles)

    def delete_article(self, article_id):
        articles = [
            a for a in self.repo.find_all()
            if a.id != article_id
        ]

        self.repo.save_all(articles)

    def login(self, username, password):
        return username == "admin" and password == "1234"