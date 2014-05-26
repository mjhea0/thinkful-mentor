# Interlude: Debugging in Python

When solving complicated coding problems, it's important to use an interactive debugger for examining executed code line by line. Python provides such a tool called [pdb](http://docs.python.org/2/library/pdb.html) (or “Python DeBugger”) within the standard library, which suports breakpoints and stack inspection.

It's important to not that the debugger is not only useful for debugging code, but for *understanding* complicated code as well.

Let's look at a simple example.

1. Save the following code as pdb_ex.py:
	```python
	import sys

	random1=['1','2','3','4','5','6','7','8','9','10','11','12'] 
	random2=['1','2','3','4','5','6','7','8','9','10','11','12'] 

	from random import choice 
	while True: 
	    print "To exit this game type 'exit'" 
	    answer = raw_input("What is " + choice(random2) + " times " + choice(random1) + "? ") 

	    # exit
	    if answer == "exit":
	        print "Now exiting game!"
	        sys.exit() 

	    # determine if number is correct
	    elif answer == int(choice(random2))*int(choice(random1)):
	        print "Correct!"
	    else:
	       print "Wrong!"
	```

	Run it. See the problem? There's either an issue with the multiplication or the logic within IF statement. 

	Let's debug!


2. Import the pdb module:
	```python
	import pdb
	```

3. Next, add `pdb.set_trace()` within the function to set your first breakpoint:
  ```python
	import pdb
	import sys

	random1=['1','2','3','4','5','6','7','8','9','10','11','12'] 
	random2=['1','2','3','4','5','6','7','8','9','10','11','12'] 

	from random import choice 
	while True: 
	    print "To exit this game type 'exit'"
	    pdb.set_trace()
	    answer = raw_input("What is " + choice(random2) + " times " + choice(random1) + "? ") 

	    # exit
	    if answer == "exit":
	        print "Now exiting game!"
	        sys.exit() 

	    # determine if number is correct
	    elif answer == int(choice(random2))*int(choice(random1)):
	        print "Correct!"
	    else:
	       print "Wrong!"
	```

4. When you run the code you should see the following output:
  ```sh
  $ python pdb_ex.py
	To exit this game type 'exit'
	> /Users/michaelherman/Documents/repos/github/thinkful-mentor/debugger/pdb_ex2.py(11)<module>()
	-> answer = raw_input("What is " + choice(random2) + " times " + choice(random1) + "? ")
	(Pdb)
	```

  Essentially, when the Python interpreter runs the `pdb.set_trace()` line, the program stops and you'll see the next line in the program as well as a prompt (or console), waiting for your input.

  From here you can start stepping through your code to see what happens line by line. Check out the list of commands you have access to [here](http://docs.python.org/2/library/pdb.html#debugger-commands). There's quite a lot of commands, which is daunting - but on a day-to-day basis, you'll only use a few common commands:
    - `n` step forward one line
    - `p <variable name>` prints the current value of the provided variable
    - `l` displays the entire program along with where the current break point is
    - `q` exits the debugger and the program
    - `c` exits the debugger and the program continues to run
    - `b <line #>` adds a breakpoint at a specific line #

  > If you don't remember the list of commands you can always type `?` or `help` to see the entire list.

  Let's debug this together.

5. First, see what the value of `answer` is:
  ```sh
	(Pdb) n
	What is 7 times 8? 56
	> /Users/michaelherman/Documents/repos/github/thinkful-mentor/debugger/pdb_ex2.py(14)<module>()
	-> if answer == "exit":
	(Pdb) p answer
	'56'
	```

6. Next, let's continue through the program to see if that value (56) changes:
  ```sh
	(Pdb) n
	> /Users/michaelherman/Documents/repos/github/thinkful-mentor/debugger/pdb_ex2.py(19)<module>()
	-> elif answer == int(choice(random2))*int(choice(random1)):
	(Pdb) n
	> /Users/michaelherman/Documents/repos/github/thinkful-mentor/debugger/pdb_ex2.py(22)<module>()
	-> print "Wrong!"
	(Pdb) p answer
	'56'
	```

	So, the answer does not change. There must be something wrong with the program logic in the IF statement, starting with the elif.

7. Update the code for testing:
  ```python
  import pdb
	import sys

	random1=['1','2','3','4','5','6','7','8','9','10','11','12'] 
	random2=['1','2','3','4','5','6','7','8','9','10','11','12'] 

	from random import choice 
	while True: 
	    print "To exit this game type 'exit'"
	    pdb.set_trace()
	    answer = raw_input("What is " + choice(random2) + " times " + choice(random1) + "? ") 

	    # exit
	    if answer == "exit":
	        print "Now exiting game!"
	        sys.exit() 

	    test = int(choice(random2))*int(choice(random1))
	    # # determine if number is correct
	    # elif answer == int(choice(random2))*int(choice(random1)):
	    #     print "Correct!"
	    # else:
	    #    print "Wrong!"
	```

	We just took the value we are using to test our `answer` against and set it to a variable. 

8. Debug time:
  ```sh
	$ python pdb_ex.py
	To exit this game type 'exit'
	> /Users/michaelherman/Documents/repos/github/thinkful-mentor/debugger/pdb_ex2.py(11)<module>()
	-> answer = raw_input("What is " + choice(random2) + " times " + choice(random1) + "? ")
	(Pdb) n
	What is 3 times 4? 12
	> /Users/michaelherman/Documents/repos/github/thinkful-mentor/debugger/pdb_ex2.py(14)<module>()
	-> if answer == "exit":
	(Pdb) n
	> /Users/michaelherman/Documents/repos/github/thinkful-mentor/debugger/pdb_ex2.py(18)<module>()
	-> test = int(choice(random2))*int(choice(random1))
	(Pdb) n
	> /Users/michaelherman/Documents/repos/github/thinkful-mentor/debugger/pdb_ex2.py(8)<module>()
	-> while True:
	(Pdb) p test
	70

	There's our answer. The value in the elif varies from the `answer`. Thus, the elif will always return "Wrong!".

9. Refactor:
  ```python
	import pdb
	import sys

	random1=['1','2','3','4','5','6','7','8','9','10','11','12'] 
	random2=['1','2','3','4','5','6','7','8','9','10','11','12'] 

	from random import choice 
	while True: 
	    print "To exit this game type 'exit'"
	    num1 = choice(random2)
	    num2 = choice(random1)
	    answer = raw_input("What is " + num1 + " times " + num2 + "? ") 

	    # exit
	    if answer == "exit":
	        print "Now exiting game!"
	        sys.exit() 

	    # determine if number is correct
	    elif (int(answer)) == (int(num1) * int(num2)):
	        print "Correct!"
	        break;
	    else:
	       print "Wrong!"
  ```

  Ultimately, the program was generating new numbers for comparison within the elif causing the user input to be wrong each time.

### Homework

- Watch [this](https://www.youtube.com/watch?v=bZZTeKPRSLQ) video on debugging.

