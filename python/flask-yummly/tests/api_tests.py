# api tests
from yummly import app
from yummly.secret import APP_ID, APP_KEY

import unittest
import requests
import responses  # mocking requests


class RecipeSearchAPITests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def load_fixture(*args, **kwargs):
        with open('tests/test.json', 'r') as f:
            response = f.read()
            return response

    def test_recipe_response_without_stubing(self):
        ingredient = "apples"

        response = requests.get(
            "http://api.yummly.com/v1/api/recipes",
            params={'_app_id': APP_ID, '_app_key': APP_KEY, 'q': ingredient}
        )

        self.assertIn("Recipe search powered", response.content)

    @responses.activate
    def test_recipe_response_with_stubing(self):
        ingredient = "apples"

        responses.add(
            responses.GET,
            "http://api.yummly.com/v1/api/recipes",
            body=self.load_fixture(),
            status=202,
            content_type='application/json'
        )

        response = requests.get(
            "http://api.yummly.com/v1/api/recipes",
            params={'_app_id': APP_ID, '_app_key': APP_KEY, 'q': ingredient}
        )

        self.assertIn("Recipe search powered", response.content)


if __name__ == "__main__":
    unittest.main()
