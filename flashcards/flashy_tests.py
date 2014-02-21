import unittest
from flashy import FlashCards

class TestFlaskCards(unittest.TestCase):

    def setUp(self):
        file1 = open('questions.txt', 'r')
        file2 = open('answers.txt', 'r')
        self.creation = FlashCards(file1, file2)

    def tearDown(self):
        pass

    def test_read_files(self):
        results = [['base assert allowing you to write your own assertions\n', 
        'check a and b are equal\n', 'check a and b are not equal\n', 
        'check that a is in the item b\n', 'check that a is not in the item b\n', 
        'check that the value of a is False\n', 'check the value of a is True\n', 
        'check that a is of type "TYPE"\n', 'check that when a is called with args that it raises ERROR\n'], 
        ['assert\n', 'assertEqual(a, b)\n', 'assertNotEqual(a, b)\n', 
        'assertIn(a, b)\n', 'assertNotIn(a, b)\n', 'assertFalse(a)\n', 
        'assertTrue(a)\n', 'assertIsInstance(a, TYPE)\n', 'assertRaises(ERROR, a, args)\n']]
        self.assertEqual(self.creation.read_files(), results)

    def test_display_question(self):
        self.assertEqual(self.creation.display_question("test"), "test")


if __name__ == '__main__':
    unittest.main()
