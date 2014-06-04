# oop

"""
to do:

1. unit tests
2. questions right vs questions wrong
3. timer
4. display questions at the end (that the user got wrong) with their right answer
5. make sure you don't repeat options (recursive function)
6. error handling - input (must be number!)

CODE REVIEW:

I would have FlashCards encapsulate it’s data. So the file open would be in
the FlashCards class (probably in the init) or if not in the read_files
function. Currently the files are just text files, but if you were to change
it to a database, they way you have it structured now, your main function
would have to know about how to access the database and thus would have to
know about the back-end storage for the FlashCards. This breaks encapsulation.
Consumers of your class shouldn’t have to know / care about how the 
flashcards are stored… they should just use it.

For display_questions. It’s actually doing doing things. 
Retrieving a question (with possible answers) and prompting the user for a choice.  
So that to me should be two functions.  get_questions and prompt user.  
However I wouldn’t have the FlashCards do any user interaction (i.e. not prints).  
What if you wanted to use FlashCards in a web app?  Then you would have to change 
the get_questions to return html instead of text. 
(or inherit and create an HTMLFlashCards class).  
But then  your class is not just flash cards but also FlashCardsDisplay, 
so it’s covering to much stuff.  If however you FlashCards.display_questsion 
(which should be called get questions) just returns the question and the 
possible answers perhaps in a dictionary i.e. return 
{‘question’ : the_question, ‘answers’: answerList}.  
Then it would be up to the client to decide how to display that data to the user, 
which means you could reuse your class for a web page, 
a terminal, an iPhone or whatever….

3.  Similarly to 2 above you want the FlashCards class to manage it’s own data, 
so it can be self contained and encapsulated which means read_files 
should probably store the content_list in a member variable instead of returning it.  
This way you don’t need to pass back content_list to display_questions and as a 
consumer of the FlashCards class you don’t need to worry about the underlying 
storage / data structure at all.


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

    def display_question(self, content):
        
        """
        displays question, list of potential answers (options)
        returns question, options, and user answer in a list
        """

        question = randint(0, len(content[0])-1)
        print "\nUnit Test:", content[0][question], ''
        options = [randint(0, len(content[1])-1),
        randint(0, len(content[1])-1),
        randint(0, len(content[1])-1)]
        options[randint(0,2)] = question
        print '1: ', content[1][options[0]],
        print '\n2: ', content[1][options[1]],
        print '\n3: ', content[1][options[2]],

        answer = input('\nYour choice: ')

        answers_list = []
        answers_list.extend([options,answer,question])
        return answers_list

    def check_if_correct(self, options_question_answer_list):

        """ determines if user answer is correct """
        if options_question_answer_list[0][options_question_answer_list[1]-1] == options_question_answer_list[2]:
            return '\nCorrect!'
        else:
            return '\nIncorrect!!'

    def play_again(self):
        again = raw_input('\nPress Enter to continue (or x then Enter to exit) ...')
        return again



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
            answers = create.display_question(data)
            correct = create.check_if_correct(answers)
            if correct == '\nCorrect!':
                score += 1
            print '\nYour score is {}'.format(score)
            again = create.play_again()
            count += 1
            create.clear_screen()


