# add functions

"""
to do:

1. oop
2. tests
3. questions right vs questions wrong
4. timer
5. display questions at end with their right answer
6. make sure you don't repeat options (recursive function)

"""

import os, random, sys

def clear_screen():
    """ clears the screen """
    os.system(['clear','cls'][os.name == 'nt'])

def read_files():

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

def display_question(content):
    
    """
    displays question, list of potential answers (options)
    returns question, options, and user answer in a list
    """

    question = random.randint(0, len(content[0])-1)
    print "\nUnit Test:", content[0][question], ''
    options = [random.randint(0, len(content[1])-1),
    random.randint(0, len(content[1])-1),
    random.randint(0, len(content[1])-1)]
    options[random.randint(0,2)] = question
    print '1: ', content[1][options[0]],
    print '\n2: ', content[1][options[1]],
    print '\n3: ', content[1][options[2]],

    answer = input('\nYour choice: ')

    answers_list = []
    answers_list.extend([options,answer,question])
    return answers_list

def answer_question(options_question_answer_list):

    """ determines if user answer is correct """

    if options_question_answer_list[0][options_question_answer_list[1]-1] == options_question_answer_list[2]:
        again = raw_input('\nCorrect!\nPress Enter to continue (or x then Enter to exit) ...')
        print '\nYour score is: {}\n'.format(calculate_score())
    else:
        again = raw_input('\nWrong!\nPress Enter to continue (or x then Enter to exit) ...')
    return again

def calculate_score():

    """calculates score"""

    score = 0
    score += 1
    return score


if __name__ == '__main__':

    again = 0
    count = 0
    while True:
        if again == "x":
            sys.exit() 
        else:
            clear_screen()
            data = read_files()
            answers =display_question(data)
            again = answer_question(answers)
            count += 1
