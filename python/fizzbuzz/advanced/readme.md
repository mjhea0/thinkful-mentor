# Advanced Fizzbuzz

## Assignment

Steps ...

1. Write a program that prints the numbers from 1 to 100. 

1. For multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

1. Refactor the code so that it uses a function, called `fizzbuzz()`, that takes a number as its argument. Then use this argument as the upper limit of the range. So, instead of a range from 1 to 100, the range starts at 1 and ends at the user-supplied number. Make sure to provide a [main routine](http://stackoverflow.com/questions/419163/what-does-if-name-main-do), `if __name__ == '__main__':`.

1. Refactor again. This time, update the function so that instead of printing the output, all numbers and strings are added to a single list. Return the entire list, which you should then loop through within the main routine and then print the numbers. 

1. Create a separate file to test your code with unit tests. Name this file *tests.py*.

1. One potential error is that the user supplies a string instead of an integer as the `fizzbuzz()` function's argument. What happens in this situation? Run your code and find out. Then update your code so that if a string is supplied, the code enters a loop where the user is asked to supply a new number. This loop should continue to loop, asking for a new value, and only end once an integer is provided. Since this is a completely new feature, write a new function for this. This function should be called from `fizzbuzz()`.

1. Refactor your code once again so that the function's argument is obtained by asking the user for a number. Use a separate function for this. How will this affect your main routine? Where is the best place to call this function?

1. Update your main routine so that you first call the function to get the value from the user. The return value is then past to a function for validation, which you've already written. Make sure you remove the function call from `fizzbuzz()` where you first set up the validation in Step 6.

1. Run your tests again to make sure they didn't break.

1. Let's add one more function that takes two integers as arguments and returns true if the first number is evenly divisible by the second, otherwise it returns false. Refactor the `fizzbuzz()` function so that it calls this function for each case (e.g, multiple of 3, 5, 15) instead of performing the logic itself.

1. How are your tests? Still passing?

1. Finally, you probably used the modulus operator, '%', to to test if a number is a multiple of 3, 5, or 15. Refactor your code so you are not using that operator.

1. Make sure you have 4 total functions that are named appropriately. Add docstrings to each. Make sure all your tests pass. Then PUSH your code to Github. 

## Concepts

1. This assignment covered the following concepts - Data Types, Exception Handling, Functions, Unit Tests, Data Structures, and Algorithms

1. In the final iteration of your program, look for each concept. Add a comment next to each and label them appropriately. Add any additional comments that you find necessary that will help you understand each concept.

1. What did we not covered? Control Flow (`if`-`elif`-`else` statements) and Test Driven Development. Homework!

## Homework

1. Update the program so that the user can supply a command line argument for the upper limit. If none is provided, then the user is asked for the upper limit. 
1. What happens if the user enters a number of 0 or a floating point? Handle each accordingly.
1. Wait a week. Do this entire program over again but this time utilize test driven development. Write a test. Watch it fail. Write just enough code for it to pass. Rinse then repeat.
1. Replace the `fizzbuzz` function with this:

	```python
	def fizzbuzz(upper_limit):
		if is_divisible(num, 15):
			return "FizzBuzz"
		if is_divisible(num, 3):
			return "Fizz"
		if is_divisible(num, 5):
			return "Buzz"
		return num
	```

	Update the program so that all of the tests still pass. 

1. Share your code on [Code Review Stack Exchange](http://codereview.stackexchange.com/). Ask for feedback as well as an additional stretch goal. 