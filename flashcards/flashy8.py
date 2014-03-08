# questions right vs wrong

"""
to do:

1. unit tests
2. timer
3. display questions at the end (that the user got wrong) with their right answer
4. error handling - input (must be number!)
5. summary at the end

"""

from os import system, name
from random import randint
import sys

class FlashCards(object):

    def __init__(self):
        pass

    def cls(self):

        """ clears the screen """

        system(['clear','cls'][name == 'nt'])


    def read_files(self):

        """ 
        opens the question and answer files
        then parses them line by line
        """

        content_list = []

        file1 = open('questions.txt', 'r')
        file2 = open('answers.txt', 'r')

        file1_content = file1.readlines()
        file2_content = file2.readlines()

        content_list.extend([file1_content, file2_content])
        return content_list


    def display_question_answers(self,content):
        
        """
        displays question, list of potential answers (options)
        returns question, options, and user answer in a list
        """

        options = []
        output_set = set()
        output_list=[]


        question = randint(0, len(content[0])-1)

        # grab options
        while len(output_set) < 3:
            test = randint(0, len(content[1])-1)
            output_set.add(test)

        # convert set to list
        options = list(output_set)

        # grab question
        question = options[randint(0,2)]

        output_list.extend([options,question, content[0][question], content[1][options[0]],
                             content[1][options[1]], content[1][options[2]]])

        return output_list

    
    def get_answer(self):

        """ get answer from the user """

        answer = input('\nYour choice: ')
        answer_list = []
        answer_list.extend([answer])
        return answer_list


    def check_answer(self, options_question_answer_list, answer):

        """ determines if user answer is correct """

        if options_question_answer_list[0][answer[0]-1] == options_question_answer_list[1]:
            return "Correct!"
        else:   
            return "Wrong"


    def play_again(self):

        """ ask user if s/he wants to play again """

        again = raw_input('Press Enter to continue (or x then Enter to exit) ...')
        return again


    def calculate_score(self, score, results):

        """ calculates score for each correct answer """

        if results == "Correct!":
            score += 1

        return score


if __name__ == '__main__':

    again = 0
    count = 0
    score = 0
    create = FlashCards()
    while True:
        if again == "x":
            sys.exit() 
        else:
            create.cls()
            data = create.read_files()
            display = create.display_question_answers(data)
            print 'Question: ' + display[2]
            print '1: ' + display[3]
            print '2: ' + display[4]
            print '3: ' + display[5]
            results = create.get_answer()
            correct = create.check_answer(display,results)
            print correct
            score = create.calculate_score(score, correct)
            print "Your score is {}".format(score)
            again = create.play_again ()
            count += 1
