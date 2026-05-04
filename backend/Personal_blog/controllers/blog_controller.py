from flask import Blueprint, render_template, request, redirect, session

blog_bp = Blueprint("blog", __name__)

# service will be injected from app.py
service = None


def init_routes(article_service):
    global service
    service = article_service


# -------- GUEST --------

@blog_bp.route("/")
def home():
    articles = service.list_articles()
    return render_template("home.html", articles=articles)


@blog_bp.route("/article/<id>")
def article(id):
    article = service.get_article(id)
    return render_template("article.html", article=article)


# -------- AUTH --------

@blog_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        result = service.login(username, password)

        if result:
            session["admin"] = True
            return redirect("/admin")

    return render_template("login.html")


# -------- ADMIN --------

@blog_bp.route("/admin")
def dashboard():
    if not session.get("admin"):
        return redirect("/login")

    return render_template(
        "dashboard.html",
        articles=service.list_articles()
    )


@blog_bp.route("/add", methods=["GET", "POST"])
def add():
    if not session.get("admin"):
        return redirect("/login")

    if request.method == "POST":
        service.create_article(
            request.form["title"],
            request.form["content"]
        )
        return redirect("/admin")

    return render_template("add.html")


@blog_bp.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    if not session.get("admin"):
        return redirect("/login")

    if request.method == "POST":
        service.update_article(
            id,
            request.form["title"],
            request.form["content"]
        )
        return redirect("/admin")

    article = service.get_article(id)
    return render_template("edit.html", article=article)


@blog_bp.route("/delete/<id>")
def delete(id):
    if not session.get("admin"):
        return redirect("/login")

    service.delete_article(id)
    return redirect("/admin")