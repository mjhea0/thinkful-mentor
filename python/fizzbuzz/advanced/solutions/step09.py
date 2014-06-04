import unittest
from step8 import fizzbuzz


class FizzBuzzTest(unittest.TestCase):

    def test_should_return_the_number(self):
        self.assertEqual(fizzbuzz(1)[0], 1)
        self.assertEqual(fizzbuzz(2)[1], 2)

    def test_multiple_3_should_return_fizz(self):
        self.assertEqual(fizzbuzz(3)[2], "Fizz")
        self.assertEqual(fizzbuzz(9)[8], "Fizz")

    def test_multiple_5_should_return_buzz(self):
        self.assertEqual(fizzbuzz(5)[4], "Buzz")
        self.assertEqual(fizzbuzz(10)[9], "Buzz")

    def test_multiple_3_and_5_should_return_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15)[14], "FizzBuzz")
        self.assertEqual(fizzbuzz(30)[29], "FizzBuzz")


if __name__ == '__main__':
    unittest.main()
