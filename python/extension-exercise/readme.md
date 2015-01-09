## Extension exercise

If you found those two exercises fairly straightforward then you should have a go at trying to write out some simple instructions to solve the following problem in as few guesses as possible:

I'm thinking of a number between 0 and 100. Try to write an algorithm which will find out what number I'm thinking of. You can have as many guesses as you like, and after each guess I'll tell you whether you were too high, or too low.

Hint: Try to think about what the optimal first guess would be to narrow the problem down. Then what would your second guess be?

### Logic


Number - 80

#### Iteration 1
- Starting array = 1...100
- Test - 50 (incorrect)
- "Higher"
- New array = 51...100

#### Iteration 2
- Starting array = 51...100
- Test - 75 (incorrect)
- "Higher"
- New array = 76..100

#### Iteration 3
- Starting array = 76..100
- Test - 75 (incorrect)
- "Higher"
- New array = 76..100

### Logic Part 2

array = xrange(1,11)

1. ask user for a guess
1. guess = 5


ask user

while True:

    if guess == right_answer:
        print "yay"
        return False
    else:
        if guess > right_answer:
            print "too high"
        else:
            print "too low"
        ask user
        return True

