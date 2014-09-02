from flask import render_template, request

from yummly import app
import api


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        recipe_response = []
        ingredients = []
        errors = []

        ingredient = request.form["ingredient"]  # grab ingredient from the form

        try:
            response = api.get_ingredients(ingredient)  # make api call

            for match in response["matches"]:  # loop through json results

                image = match['imageUrlsBySize']['90'].replace('s90-c', 's230-c')  # update url

                recipe_response.extend([
                    match["recipeName"], image, match["id"]
                ])  # grab reciepe name, image, and id
                ingredients.append(match["ingredients"])
                break  # just loop once for now, grabbing the first recipe

            ingredients = ingredients[0]

        except:  # silencing all errors - bad!

            errors.append("Something went wrong!")

        return render_template(
            "index.html",
            recipe_response=response,
            errors=errors
        )

    else:

        return render_template(
            "index.html"
        )
