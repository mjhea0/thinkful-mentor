import unittest
from fizz import Fizzer

class FizzBuzz(unittest.TestCase):

    def setUp(self):
        self.buzzer = Fizzer()

    def test_number_is_mulitple_of_three(self):
        result = self.buzzer.fizzbuzz(3)
        self.assertEqual(result,'fizz')

    def test_number_is_multiple_of_five(self):
        result = self.buzzer.fizzbuzz(25)
        self.assertEqual(result,'buzz')

    def test_number_is_multiple_of_three_and_five(self):
        result = self.buzzer.fizzbuzz(15)
        self.assertEqual(result,'fizzbuzz')

    def test_number_not_multiple_of_three_or_five(self):
        result = self.buzzer.fizzbuzz(22)
        self.assertEqual(result,22)


if __name__ == '__main__':
    unittest.main()