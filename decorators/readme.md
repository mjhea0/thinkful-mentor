## Decorators

Decorators are a form on Python metaprogramming, using functions to manipulate code. 

> You can find all the examples from this article [here](https://github.com/mjhea0/thinkful-mentor/tree/master/decorators).

### Before you can understand decorators, you must first understand:

1. How functions work. Essentially, functions simply return a value based on the given arguments.
  ```python
  def foo(bar):
      return bar + 1


  print foo(2) == 3
  ```


2. In Python, functions are [first-class](http://python-history.blogspot.com/2009/02/first-class-everything.html) objects. This means that functions can be passed around, and used as arguments, just like any other value (e.g, string, int, float).
  ```python
  def foo(bar):
      return bar + 1

  def baz(qux):
      return qux + 1


  num = foo(2)
  print baz(num) == 4

  # OR #

  print baz(foo(2)) == 4
  ```

3. Because of the first-class nature of functions in Python, you can define functions inside other functions. Such functions are called nested functions.
  ```python
  def parent():
    print "Printing from the parent() function."

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    print first_child()
    print second_child()
  ```

  What happens when you call the `parent()` function? Think about this for a minute. You should get ...

  ```sh
  Printing from the parent() function.
  Printing from the first_child() function.
  Printing from the second_child() function
  ```

  Try calling the `first_child()`. You should get an error:

  ```sh
  Traceback (most recent call last):
  File "decorator3.py", line 15, in <module>
    first_child()
  NameError: name 'first_child' is not defined
  ```

  What have we learned?

  Whenever you call `parent()`, the sibling functions, `first_child()` and `second_child()` are also called *AND* 
  beacuse of scope, both of the sibling functions are not available (e.g., cannot be called) outside of the parent function.

4. Python also allows you to return functions from other functions. Let's alter the previous function for this example.
  ```python
  def parent(num):

      def first_child():
          return "Printing from the first_child() function."

      def second_child():
          return "Printing from the second_child() function."

      try:
          assert num == 10
          return first_child
      except AssertionError:
          return second_child

  foo = parent(10)
  bar = parent(11)

  print foo
  print bar

  print foo()
  print bar()
  ```

  The output of the first two print statements is:

  ```sh
  <function first_child at 0x1004a8c08>
  <function second_child at 0x1004a8cf8>
  ```

  This simply means that `foo` points to the `first_child()` function, while `bar` points to the `second_child()` function.

  The output of the second two functions confirms this:

  ```sh
  Printing from the first_child() function.
  Printing from the second_child() function.
  ```

  Finally, did you notice that in example three, we excuted the sibling functions within the parent functions - e.g, `second_child()`. Meanwhile in this last example, we did not add parenthesis to the sibling functions - `first_child` - when called so that way we can use them in the future. Make sense?

  
## Now, my friend, you are ready to take on decorators! Let's look at two examples:

1. Example 1:
  ```python
  def my_decorator(some_function):

      def wrapper():

          print "Something is happening before some_function() is called."

          some_function()

          print "Something is happening after some_function() is called."

      return wrapper

  def just_some_function():
     print "Wheee!"


  just_some_function = my_decorator(just_some_function)

  just_some_function()
  ```

  Can you guess what the output will be? Try.

  ```sh
  Something is happening before some_function() is called.
  Wheee!
  Something is happening after some_function() is called.
  ```

  To understand what's going on here, just look back at the four prevous examples. We are literally just applying everything learned. Put simply, decorators wrap a function, modifying its behavior.

  Let's take it one step further and add an if statement.

2. Example 2:
  ```python
  def my_decorator(some_function):

      def wrapper():
          
          num = 10

          if num == 10:
              print "Yes!"
          else:
              print "No!"

          some_function()

          print "Something is happening after some_function() is called."

      return wrapper

  def just_some_function():
     print "Wheee!"

  just_some_function = my_decorator(just_some_function)

  just_some_function()
  ```

  This will output in:

  ```sh
  Yes!
  Wheee!
  Something is happening after some_function() is called.
  ```

## Time for some syntatic sugar!

Python allows you to simplfy the calling of decorators using the `@` symbol:

1. Let's create a module for our decorator:

  ```python
  def my_decorator(some_function):

      def wrapper():
          
          num = 10

          if num == 10:
              print "Yes!"
          else:
              print "No!"

          some_function()

          print "Something is happening after some_function() is called."

      return wrapper

  if __name__ == "__main__":
      my_decorator()
  ```

  Okay. Stay with me. Let's look at how to call the function with the decorator:

  ```python
  from decorator7 import my_decorator

  @my_decorator
  def just_some_function():
     print "Wheee!"

  just_some_function()
  ```

  When you run this example, you should get the same output as in the previous one:

  ```sh
  Yes!
  Wheee!
  Something is happening after some_function() is called.
  ```

  So, `@my_decorator` is just an easier way of saying `just_some_function = my_decorator(just_some_function)`.

### How about a real world example?

  ```python
  import time

  def timing_function(some_function):
      def wrapper():
          t1 = time.time()
          some_function()
          t2 = time.time()
          return "Time it took to run the function: " + str((t2-t1)) + "\n"
      return wrapper

  @timing_function
  def my_function():
      num_list = []      
      for x in (range(0,10000)):
          num_list.append(x)
      print "\nSum of all the numbers: " +str((sum(num_list)))


  print my_function()
  ```

  This returns the time before you run the function as well as the time after. Then we simply subtract the two to see how long it took to run the function.

  Run the function. Work through the code, line by line. Make sure you understand how it works.

  Cheers!


