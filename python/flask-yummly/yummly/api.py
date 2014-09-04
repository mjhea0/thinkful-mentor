# api calls


import requests
from secret import APP_ID, APP_KEY


def get_ingredients(search_value):

    print search_value

    res = requests.get(
        "http://api.yummly.com/v1/api/recipes",
        params={'_app_id': APP_ID, '_app_key': APP_KEY, 'q': search_value}
    )

    print res.json()
    return res.json()
