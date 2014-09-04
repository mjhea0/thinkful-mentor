from flask import render_template, request
from yummly import app
from yummly import api


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        errors = []

        value = request.values.get('ingredient')  # grab ingredient from form
        cuisines = request.form.getlist('cuisine')  # grab cuisines from form
        cuisines = ', '.join(cuisines).replace(", ", "+")

        if cuisines:
            value = "{0}&allowedCuisine[]={1}".format(value, cuisines)

        try:
            response = api.get_ingredients(value)  # make api call
        except:  # silencing all errors - bad!
            errors.append("Something went wrong!")
        return render_template(
            "index.html", recipe_response=response, errors=errors
        )
    else:
        return render_template("index.html")
