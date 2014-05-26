import unittest
from multiply import multiply_nums, multiply_strings
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass

    def tearDown(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual(multiply_nums(3,4), 12)
 
    def test_strings_a_3(self):
        self.assertEqual(multiply_strings('hi',4), 'hihihihi')

    def test_exception(self):
        self.assertEqual(multiply_strings(1,4), "Not a string")
 
if __name__ == '__main__':
    unittest.main()
