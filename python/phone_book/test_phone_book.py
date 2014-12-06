import unittest
from phone_book import PhoneBook
import os

FILENAME = 'test_pb_data.p'
class PhonebookTest(unittest.TestCase):
    def setUp(self):
        self.pb = PhoneBook(FILENAME)

    def load_some_data(self):
        self.pb.update("Sam", "222 333 4444")
        self.pb.update("Becky", "123 456 7890")
        self.pb.update("Trisquit", "999 888 4444")
        self.pb.update("Ralf", '444 333 2222')
    
    def test_query(self):
        self.load_some_data()
        self.assertEqual(self.pb.query("Sam"), "Sam => 222 333 4444")

    def test_delete(self):
        self.load_some_data()
        self.assertEqual(self.pb.query("Sam"), "Sam => 222 333 4444")
        self.pb.delete("Sam")
        self.assertEqual(self.pb.query("Sam"), "not found")
   
    def test_add(self):
        self.load_some_data()
        self.assertEqual(self.pb.query("Barnabus"), "not found")
        self.pb.update("Barnabus", "1234")
        self.assertEqual(self.pb.query("Barnabus"), "Barnabus => 1234") 
         
    def tearDown(self):
        os.unlink(FILENAME)

if __name__ == "__main__":
    unittest.main()