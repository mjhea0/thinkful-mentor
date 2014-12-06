import unittest
import pickler
import os

class PicklerTest(unittest.TestCase):
    def setUp(self):
        self.filename = "pickle_test.p"

    def tearDown(self):
        if os.path.isfile(self.filename):
            os.unlink(self.filename)
       
    def test_pickler(self):
        data = [1, 2, 3, 4, 5]
        pickler.do_pickle(data, self.filename)
        result = pickler.unpickle(self.filename)
        self.assertEqual(data, result)

if __name__ == '__main__':
    unittest.main()