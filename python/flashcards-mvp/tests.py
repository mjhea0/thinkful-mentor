import unittest
from app import app, db, get_options, get_question, Answer

class FlashCardsTest(unittest.TestCase):

    def test_answer_list_is_unique(self):
        question = get_question()
        self.assertEqual(len(set(get_options(question))),3) 

    def test_answer_is_among_options(self):
        question = get_question()
        test = []
        for option in get_options(question):
            q = db.session.query(Answer).filter(Answer.description == str(option)).first()
            test.append(q.question_id)
        self.assertTrue(question.question_id in test)


if __name__ == '__main__':
    unittest.main()
