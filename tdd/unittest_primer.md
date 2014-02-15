## unittest primer

Testing is important. Python's [unittest](http://docs.python.org/2/library/unittest.html) library, which is part of Python's standard library makes testing easy. 

In this post, we'll look at the basics of the library in order to create and run a simple test.

Let's take a quick look at a basic workflow:

1. Define your class that's subclassed from the `unittest.TestCase` base class
2. Add the two methods `setUp()` and `tearDown()` - which run before and after each method
3. Then add your own methods for testing that start with `test_`
4. Make sure to add an `assert()` function, such as as `assertEqual()` so that *something* is actually tested
5. Add the following code snippet to the bottom of the file:
  ```python
  if __name__ == '__main__':
    unittest.main()
  ```

### Example

In this example, save the first file as *multiply.py*. We will be testing this file. Then save the second file, which is used for testing the first file, as *multiply_test.py*.

#### File for testing

```python
def multiply_nums(n1,n2):
    return n1*n2

def multiply_strings(string, num):
    if type(string) == str:
        return string*num
    else:
        return "Not a string"
```

#### unittest

```python
import unittest
from multiply import multiply_nums, multiply_strings
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass

    def tearDown(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual(multiply_nums(3,4), 12)
 
    def test_strings_a_3(self):
        self.assertEqual(multiply_strings('hi',4), 'hihihihi')

    def test_exception(self):
        self.assertEqual(multiply_strings(1,4), "Not a string")
 
if __name__ == '__main__':
    unittest.main()
```

#### Run the test

```sh
$ python multiply_test.py -v
test_exception (__main__.TestUM) ... ok
test_numbers_3_4 (__main__.TestUM) ... ok
test_strings_a_3 (__main__.TestUM) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

Yay! They all pass!

#### What's going on?

Looking at this method-

```python
def test_numbers_3_4(self):
    self.assertEqual(multiply_nums(3,4), 12)
```

-we created a method that takes the `self` argument. We then used the `assertEqual()` method to assert that the result of the function `multiply_nums(3,4)` is `12` - which is true, obviously. 

### Next Steps

Try changing the assertion so that it doesn't passes just to see what happens. Then try some different `assert()` methods found [here](http://docs.python.org/2/library/unittest.html#unittest.TestCase).
