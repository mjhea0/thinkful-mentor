# api calls


import requests
from secret import APP_ID, APP_KEY


def get_ingredients(ingredients):

    ingredient_request = "{0}+{0}+{0}".format(
        ingredients[0],
        ingredients[1],
        ingredients[2]
    )

    res = requests.get(
        "http://api.yummly.com/v1/api/recipes",
        params={'_app_id': APP_ID, '_app_key': APP_KEY, 'q': ingredient_request}
    )
    print res.json()
    return res.json()
