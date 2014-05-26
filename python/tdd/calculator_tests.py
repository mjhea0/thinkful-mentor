# why does this not work without using nose?

import unittest
from calculator import Calculator

class TddInPythonExample(unittest.TestCase):

    # ran before each test
    def setUp(self):
        self.calc = Calculator()

    # ran after each test
    def tearDown(self):
        pass

    def test_calculator_add_method_returns_correct_result(self):
        self.assertEqual(self.calc.add(2,2), 4)

    def test_calculator_add_method_returns_correct_result_example_two(self):
        self.assertEqual(self.calc.add(3,2), 5)
