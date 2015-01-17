right_answer = 77
guess = int(raw_input("Please guess a number between 1-100: "))

while (guess != right_answer):
    if guess > 100 and guess <= 0:
        print "Sorry, has to be between 1-100."
    else:
        if guess == right_answer:
            print "That's right!"
        if guess < right_answer:
            print "Sorry, wrong guess. Guess a higher number."
        if guess > right_answer:
            print "Sorry, wrong guess. Guess a lower number."
    guess = int(input("Please guess a number between 1-100: "))
