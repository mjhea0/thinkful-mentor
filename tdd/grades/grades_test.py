import unittest
from grades import LetterGrades
 
class LetterGradeTest(unittest.TestCase):

    def setUp(self):
        self.letter = LetterGrades()

    # test methods, which start with "test_"

    def test_user_input_is_integer(self):
        results = self.letter.input_numeric_grade(90)
        self.assertEqual(type(results), float)

    def test_int_between_zero_and_one_hundred(self):
        first = self.letter.input_numeric_grade(80)
        second = self.letter.input_numeric_grade(65)
        self.assertIn(first,xrange(0,100))
        self.assertIn(second,xrange(0,100))

    def test_letter_grade_of_A(self):
        results = self.letter.convert_numeric_grade_to_letter_grade(90)
        self.assertEqual(results, "A")

    def test_letter_grade_of_B(self):
        results = self.letter.convert_numeric_grade_to_letter_grade(80.6)
        self.assertEqual(results, "B")

    def function():
        pass

    def function():
        pass




