# Advanced Fizzbuzz

## Assignment

1. Write a program that prints the numbers from 1 to 100. 

1. For multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

1. Refactor it so that it uses a function, called `fizzbuzz()`, that takes a number as its argument, then use this argument as the upper limit of the range. So, instead of a range from 1 to 100, the range starts at 1 and ends at the user supplied number. Make sure to provide a [main routine](http://stackoverflow.com/questions/419163/what-does-if-name-main-do), `if __name__ == '__main__':`.

1. Create a separate file to test your code with unit tests. Think about some possible errors. Test for them. 

1. One potential error is that the user supplies a string instead of an integer as the function's argument. If you didn't write a test for this, write it now, then update your code so that if a string is supplied, the code ends and outputs some message to the user, indicating that a string should be supplied. Make sure your tests takes this added functionality into account. Also, since this is a completely new feature, write a new function for this. 

1. Refactor your code once again so that the function's argument is obtained by asking the user. Use a separate function for this. Continue to ask the user until s/he provides an integer. Update your test(s) as needed. 

1. Let's add one more function that takes two integers as arguments and returns true if the first number is evenly divisible by the second, otherwise it returns false. Refactor the `fizzbuzz()` function so that it calls this function for each case (e.g, multiple of 3, 5, 15) instead of performing the logic itself.

1. How are your tests? Still passing?

1. Finally, you probably used the modulus operator, '%', to to test if a number is a multiple of 3, 5, or 15. Refactor your code so you are not using that operator.

1. Make sure you have 4 total functions that are named appropriately. Add docstrings to each. Make sure all your tests pass. Then PUSH your code to Github. 

## Concepts

Github, Command Line, Code Editor, Data Types, Exceptions Handling, Functions, Unit Tests, TDD

Control Flow, Data Structures



