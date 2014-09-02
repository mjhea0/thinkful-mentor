# tests
from yummly import app
from yummly.secret import APP_ID, APP_KEY

import unittest
import requests


class RecipeSearchTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_main_page_returns_form(self):
        response = self.app.get('/')
        self.assertIn('<form role="form" method="POST">', response.data)

    def test_recipe_response_without_stubing(self):
        ingredient = "apples"

        response = requests.get(
            "http://api.yummly.com/v1/api/recipes",
            params={'_app_id': APP_ID, '_app_key': APP_KEY, 'q': ingredient}
        )

        self.assertIn("Recipe search powered", response.content)


if __name__ == "__main__":
    unittest.main()
