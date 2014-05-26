import unittest
from sql_plotly import create_db, search_db, call_plotly

class TestPlotlyAPI(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_search_db(self):
        create_db("tester_db")
        self.assertEqual(search_db("tester_db"), [['Bobby', 'Michael', 'John'], [10, 20, 20]])

    def test_call_plotly(self):
        pass

if __name__ == '__main__':
    unittest.main()
