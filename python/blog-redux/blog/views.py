import mistune
from flask import request, redirect, url_for, render_template

from blog import app
from database import session
from models import Post


@app.route("/")
@app.route("/page/<int:page>")
def posts(page=1, paginate_by=10):
    # Zero-indexed page
    page_index = page - 1

    count = session.query(Post).count()

    start = page_index * paginate_by
    end = start + paginate_by

    total_pages = (count - 1) / paginate_by + 1
    has_next = page_index < total_pages - 1
    has_prev = page_index > 0

    posts = session.query(Post)
    posts = posts.order_by(Post.datetime.asc())
    posts = posts[start:end]

    return render_template(
        "posts.html",
        posts=posts,
        has_next=has_next,
        has_prev=has_prev,
        page=page,
        total_pages=total_pages
    )


@app.route("/post/add", methods=["GET"])
def add_post_get():
    return render_template("add_post.html")


@app.route("/post/add", methods=["POST"])
def add_post_post():
    post = Post(
        title=request.form["title"],
        content=mistune.markdown(request.form["content"])
    )
    session.add(post)
    session.commit()
    return redirect(url_for("posts"))


@app.route("/post/<int:post_id>", methods=["GET"])
def view_post(post_id):
    posts = session.query(Post)
    posts = posts.filter(Post.id == post_id)
    posts = posts.all()
    return render_template("posts.html", posts=posts)
