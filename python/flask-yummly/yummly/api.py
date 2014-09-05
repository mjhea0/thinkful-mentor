# api calls


import requests
from secret import APP_ID, APP_KEY


def get_ingredients(ingredients_list):

    res = requests.get(
        "http://api.yummly.com/v1/api/recipes",
        params={
            '_app_id': APP_ID,
            '_app_key': APP_KEY,
            'q': ingredients_list,
            'maxResult': 100
        }
    )

    return res.json()
