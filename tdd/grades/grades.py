"""
Problem: Given a grade. For example, 89 - return B+. 
Return letter grade from numerical grade.
"""

# classes = noun
# medthods = advetives/verbs

class LetterGrades(object):

    """given a numeric grade return letter grade"""

    def input_numeric_grade(self,num_grade):
        return float(num_grade)

    def convert_numeric_grade_to_letter_grade(self,num_grade):
        if num_grade >= 90:
            return "A"
        elif num_grade >= 80:
            return "B"


# letter = LetterGrades()
# print letter.input_numeric_grade(80)
