from flask import render_template, request, jsonify

from yummly import app
from yummly import api
import random


@app.route("/", methods=["GET", "POST"])
def index():

    """
    1. grab ingredient list from form
    2. pass ingredients list to `get_ingredients()`
    3. grab random result
    3. return results to the template
    """

    if request.method == "POST":
        ingredient_list = request.form.get('ingredient_list')
        recipe = []

        try:
            response = api.get_ingredients(ingredient_list)
            recipe = random.choice(response["matches"])
            ingredients = []
            for i in recipe['ingredients']:
                ingredients.append(i)

            result = {
                "recipe_id": recipe["id"],
                "recipe_name": recipe["recipeName"],
                "recipe_pic": recipe['imageUrlsBySize']['90'].replace(
                    's90-c', 's230-c'),
                "recipe_rating": recipe['rating'],
                "recipe_flavors": recipe['flavors'],
                "recipe_ingredients": ingredients
            }
            code = 200

        except:  # silencing all errors
            result = {"sorry": "Sorry, no results! Please try again."}
            code = 500

        return jsonify(result), code

    else:

        return render_template("index.html")
