# Decorators

Decorators are a form on Python metaprogramming, using functions to manipulate code. Now, before you can understand decorators, you must first understand: 

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

  print baz(foo(2)) = 4
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

  What happens when you call the `parent()` function? Think about this for a minute.

  ```
  parent()

  # =>
  Printing from the parent() function.
  Printing from the first_child() function.
  Printing from the second_child() function.
  ```




functions can not only accept other functions as arguments - but return functons are well. *This is a decorator*


