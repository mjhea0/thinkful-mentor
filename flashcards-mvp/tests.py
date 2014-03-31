import unittest
from app import app, db, generate_options

class FlashCardsTest(unittest.TestCase):

    def test_answer_list_is_unique(self):
        self.assertEqual(len(set(generate_options())),3) 

    def test_every_question_has_an_answer(self):
        self.assertEqual(len(set(generate_options())),3) 


if __name__ == '__main__':
    unittest.main()
