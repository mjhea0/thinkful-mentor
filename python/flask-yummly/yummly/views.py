from flask import render_template, request
from yummly import app
from yummly import api


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        errors = []
        ingredients = []

        form_data = request.values  # grab form values
        for key, value in form_data.items():
            ingredients.append(value)

        try:
            response = api.get_ingredients(ingredients)  # make api call
        except:  # silencing all errors - bad!
            errors.append("Something went wrong!")
        return render_template(
            "index.html", recipe_response=response, errors=errors
        )
    else:
        return render_template("index.html")
