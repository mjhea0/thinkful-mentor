# tests
import os
import unittest
from yummly import app, api
from secret import APP_KEY, APP_ID

import requests
import responses # mocking requests



class RecipeSearchTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def load_fixture(*args, **kwargs):
        with open('tests/test.json', 'r') as f:
            response = f.read()
            return response

    def test_recipe_response(self):
        ingredient = "apples"
        response = requests.get(
            "http://api.yummly.com/v1/api/recipes",
            params={'_app_id': APP_ID, '_app_key': APP_KEY, 'q': ingredient}
        )
        self.assertIn("Recipe search powered", response.content)

    @responses.activate
    def test_recipe_response_with_stubbing(self):
        ingredient = "apples"

        responses.add(
            responses.GET,
            "http://api.yummly.com/v1/api/recipes",
            body=self.load_fixture(),
            status=202,
            content_type='application_json'
        )

        response = requests.get(
            "http://api.yummly.com/v1/api/recipes",
            params={'_app_id': APP_ID, '_app_key': APP_KEY, 'q': ingredient}
        )
            

if __name__ == "__main__":
    unittest.main()






        