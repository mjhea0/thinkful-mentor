from flask import render_template, request, jsonify, make_response
from yummly import app
from yummly import api
import random


@app.route("/", methods=["GET", "POST"])
def index():
    """
    1. grab ingredient list
    2. pass ingredients list to `get_ingredients()`
    3. grab random result
    3. return results to the template
    """
    if request.method == "POST":
        ingredient_list = request.values.get('ingredient')
        try:
            response = api.get_ingredients(ingredient_list)
            recipe = random.choice(response["matches"])
            print recipe
            result = {
                "recipe_id": recipe["id"],
                "recipe_name": recipe["recipeName"],
                "recipe_pic": recipe['imageUrlsBySize']['90'].replace(
                    's90-c', 's230-c'
                )
            }
            code = 200
        except:  # silencing all errors - bad!
            result = {"sorry": "Something went terribly wrong!"}
            code = 404
        return make_response(jsonify(result), code)
    else:
        return render_template("index.html")
