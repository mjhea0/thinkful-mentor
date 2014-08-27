from flask import render_template, request, jsonify

from yummly import app
import api
import json


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", recipes=[])


@app.route("/", methods=["POST"])
def recipes():
    ingredient = request.form["ingredient"]  # grab ingredient from the form
    response = api.get_ingredients(ingredient)  # make api call
    response_to_json = json.loads(response)  # convert to json from unicode
    image_url = response_to_json["matches"][0]["smallImageUrls"][0]
    # return jsonify(response_to_json)  # output json!
    return render_template("index.html", image_url=image_url)
