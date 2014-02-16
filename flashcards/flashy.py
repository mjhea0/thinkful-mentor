import os, random

count = 0
score = 0

file1 = open('questions.txt', 'r')
file2 = open('answers.txt', 'r')

f1content = file1.readlines()
f2content = file2.readlines()

while count < 10:

    question = random.randint(0, len(f1content)-1)

    print "Unit Test:", f1content[question], ''

    options = [random.randint(0, len(f2content)-1),
        random.randint(0, len(f2content)-1),
        random.randint(0, len(f2content)-1)]

    options[random.randint(0,2)] = question

    print '1: ', f2content[options[0]],
    print '\n2: ', f2content[options[1]],
    print '\n3: ', f2content[options[2]],

    answer = input('\nYour choice: ')

    if options[answer-1] == question:
        raw_input('\nCorrect! Hit Enter...')
        score += 1
    else:
        raw_input('\nWrong! Hit Enter...')

    count += 1

    print '\nYour score is:', score
