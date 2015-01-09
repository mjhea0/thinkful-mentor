# first attempt (brute force)

import random

guess = int(raw_input("What's your guess? "))
answer = random.randrange(1, 101)

while True:
    if guess != answer:
        if guess > answer:
            print "Your guess is too high."
        else:
            print "Your guess is too low."
        guess = int(raw_input("What's your guess? "))
    else:
        print "Correct!"
        break
