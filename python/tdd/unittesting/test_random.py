import unittest
import random


class RandomTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_count(self):
        word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.assertEqual(random.count(word), 62)

    def test_count_alpha(self):
        word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.assertEqual(random.count_alpha(word), 52)

    def test_count_numeric(self):
        word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.assertEqual(random.count_numeric(word), 10)

    def test_count_vowels(self):
        word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.assertEqual(random.count_vowels(word), 10)

    def test_is_phonenumber(self):
        number = "720-400-4531"
        self.assertTrue(random.is_phonenumber(number))


if __name__ == '__main__':
    unittest.main()
