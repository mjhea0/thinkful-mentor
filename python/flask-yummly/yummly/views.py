from flask import render_template, request

from yummly import app
import api
import json


@app.route("/", methods=["GET", "POST"])
def index():
    recipe_response = []
    ingredients = []

    if request.method == "POST":
        ingredient = request.form["ingredient"]  # grab ingredient from the form
        response = api.get_ingredients(ingredient)  # make api call
        response_to_json = json.loads(response)  # convert to json from unicode

        matches = response_to_json["matches"]
        for match in matches:
            recipe_response.extend([
                match["recipeName"], match["smallImageUrls"][0], match["id"]
            ])
            ingredients.append(match["ingredients"])
            break  # just loop once for now, grabbing the first recipe

        ingredients = ingredients[0]

    return render_template(
        "index.html",
        recipe_response=recipe_response,
        ingredients=ingredients
    )
