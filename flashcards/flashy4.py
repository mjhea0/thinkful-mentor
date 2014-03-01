# oop

"""
to do:

1. unit tests
2. questions right vs questions wrong
3. timer
4. display questions at the end (that the user got wrong) with their right answer
5. make sure you don't repeat options (recursive function)
6. error handling - input (must be number!)

"""

from os import system, name
from random import randint
import sys

class FlashCards(object):

    def __init__(self, answers_file, questions_file):
        self.questions_file = questions_file
        self.answers_file = answers_file

    def clear_screen(self):
        """ clears the screen """
        system(['clear','cls'][name == 'nt'])

    def read_files(self):
        """ 
        opens the question and answer files
        then parses them line by line
        """

        content_list = []

        file1_content = self.questions_file.readlines()
        file2_content = self.answers_file.readlines()

        content_list.extend([file1_content, file2_content])
        return content_list

    def display_question_and_answers(self, content):
        """
        displays question, list of potential answers (options)
        returns question, options, and user answer from a list
        """

        output_list = []

        question = randint(0, len(content[0])-1)
        options = [randint(0, len(content[1])-1),
        randint(0, len(content[1])-1),
        randint(0, len(content[1])-1)]
        options[randint(0,2)] = question

        output_list.extend([
            [content[0][question]],
            [[content[1][options[0]]],
            [content[1][options[1]]],
            [content[1][options[2]]] 
            ]])
        return output_list 


    def get_answer(self):
        """ get answer from the user """

        answer = input('\nYour choice: ')
        return answer

    def check_if_correct(self, options_question_answer_list):
        """ determines if user answer is correct """
        print options_question_answer_list[0]
        if options_question_answer_list[0][options_question_answer_list[1]-1] == options_question_answer_list[2]:
            return '\nCorrect!'
        else:
            return '\nIncorrect!!'

    def play_again(self):
        """ ask user if s/he wants to play again """

        again = raw_input('\nPress Enter to continue (or x then Enter to exit) ...')
        return again

    def calculate_score(self, score):
        """ calculates score for each correct answer """

        if correct == '\nCorrect!':
            score += 1
        print '\nYour score is {}'.format(score)
        return score


if __name__ == '__main__':
    count = 0
    score = 0
    again = 0
    file1 = open('questions.txt', 'r')
    file2 = open('answers.txt', 'r')
    create = FlashCards(file1, file2)
    data = create.read_files()
    create.clear_screen()
    while True:
        if again == "x":
            sys.exit() 
        else:
            answers = create.display_question_and_answers(data)
            print "Question: {}".format((", ".join(answers[0])))
            print "Options:"
            x = 1
            for answer in answers[1]:
                print "{}) {}".format(x, (", ".join(answer)).rstrip())
                x += 1
            results = create.get_answer()
            # correct = create.check_if_correct(results)
            # score = create.calculate_score(score)
            again = create.play_again()
            count += 1
            create.clear_screen()


