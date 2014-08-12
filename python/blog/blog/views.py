from flask import render_template

from blog import app
from database import session
from models import Post

import mistune
from flask import request, redirect, url_for

from flask.ext.login import login_required, current_user


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
    posts = posts.order_by(Post.datetime.desc())
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
@login_required
def add_post_get():
    return render_template("add_post.html")


@app.route("/post/add", methods=["POST"])
@login_required
def add_post_post():
    post = Post(
        title=request.form["title"],
        content=mistune.markdown(request.form["content"]),
        author=current_user
    )
    session.add(post)
    session.commit()
    return redirect(url_for("posts"))


@app.route("/post/<postid>")
def post(postid=Post.id):
    post = session.query(Post).filter(Post.id == postid).first()
    return render_template(
        "single_post.html",
        post=post,
        postid=postid,
    )


@app.route("/post/<postid>/edit", methods=["GET"])
def edit_post_get(postid=Post.id):
    return render_template("edit_post.html")


@app.route("/post/<postid>/edit", methods=["POST"])
def edit_post(postid):

    title = request.form["title"]
    content = mistune.markdown(request.form["content"])

    session.query(Post).filter_by(id=postid).update(
        {"title": title, "content": content}
    )

    session.commit()
    return redirect(url_for("posts"))


@app.route("/post/<postid>/delete", methods=["POST"])
def delete_post(postid):
    session.query(Post).filter_by(id=postid).delete()
    session.commit()
    return redirect(url_for("posts"))


@app.route("/login", methods=["GET"])
def login_get():
    return render_template("login.html")

from flask import flash
from flask.ext.login import login_user
from werkzeug.security import check_password_hash
from models import User


@app.route("/login", methods=["POST"])
def login_post():
    email = request.form["email"]
    password = request.form["password"]
    user = session.query(User).filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash("Incorrect username or password", "danger")
        return redirect(url_for("login_get"))

    login_user(user)
    return redirect(url_for("posts"))

# set the secret key.  keep this really secret:
app.secret_key = "l\xcd\xaf\x93\xd5sy\xb4WHu\xdd\x8fW\xe4J LY\x14\x98\x13ft"
