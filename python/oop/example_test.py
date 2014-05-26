import unittest
from example import Add

class TestAdd(unittest.TestCase):

    def setUp(self):
        number = 16
        self.create = Add(number)

    def test_add_one(self):
        self.assertEqual(self.create.add_one(), 17)


if __name__ == '__main__':
    unittest.main()

