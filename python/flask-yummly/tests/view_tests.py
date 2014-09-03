# view tests
from yummly import app
import unittest


class RecipeSearchViewTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_main_page_returns_form(self):
        response = self.app.get('/')
        self.assertIn('<form role="form" method="POST">', response.data)


if __name__ == "__main__":
    unittest.main()
