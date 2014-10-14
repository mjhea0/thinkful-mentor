from flask import render_template

from blog import app
from database import session
from models import Post
import mistune
from flask import request, redirect, url_for


@app.route("/")
#new route created to take us to a specific page of content
@app.route("/page/<int:page>")
def posts(page=1, paginate_by=10):
    """2 args:
    1) page - a page number
    2) paginate_by - indicates how many items should be on each page
    """
    #zero-indexed page
    page_index = page - 1

    #use the count method of a Post query object to find total number of items
    count = session.query(Post).count()

    #the index of the first item we should see
    start = page_index * paginate_by
    #the index of the last itme we should see
    end = start + paginate_by

    #total number of (pages of content)
    total_pages = (count - 1) / (paginate_by) + 1
    #is there a page after the current one
    has_next = page_index < (total_pages - 1)
    #is there a page before the current one
    has_prev = page_index > 0

    #construct a query of Post objects
    posts = session.query(Post)
    #order the posts by the datetime column, getting the most recent posts first
    posts = posts.order_by(Post.datetime.desc())
    #slice the posts query so that we only find
    # posts between the start and end indicies
    posts = posts[start:end]
    #render a template called posts.html, passing in all the posts we want
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
    #create a new Post object
    post = Post(
        title=request.form["title"],
        content=mistune.markdown(request.form["content"]),
    )
    #add post to our session and commit to database
    session.add(post)
    session.commit()
    return redirect(url_for("posts"))


@app.route("/post/<int:id>")
def view_post(id):
    post = session.query(Post).filter_by(id=id)
    return render_template("single_post.html", post=post)
