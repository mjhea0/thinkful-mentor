# api calls


import requests
import json

APP_ID = 'test'
APP_KEY = 'test'


def get_ingredients(self):
    res = requests.get(
        "http://api.yummly.com/v1/api/metadata/ingredient",
        params={'_app_id': APP_ID, '_app_key': APP_KEY}
    )
    response = res.text
    ingredients = json.loads(response)
    for ingredient in ingredients:
        print ingredient
