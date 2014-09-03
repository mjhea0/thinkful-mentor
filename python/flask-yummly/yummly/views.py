from flask import render_template, request
from yummly import app
from yummly import api


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        errors = []
        ingredient = request.form["ingredient"]  # grab ingredient from the form
        try:
            response = api.get_ingredients(ingredient)  # make api call
        except:  # silencing all errors - bad!
            errors.append("Something went wrong!")
        return render_template(
            "index.html", recipe_response=response, errors=errors
        )
    else:
        return render_template("index.html")
