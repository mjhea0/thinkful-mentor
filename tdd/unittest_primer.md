## unittest primer

Testing is important. Python's [unittest](http://docs.python.org/2/library/unittest.html) library, wich is part of Python's standard library makes testing easy. 

In this post, we'll look at the basics of the library to create and run a simple test.

Let's take a quick look at a basic workflow:
1. Define your class that's subclassed from the `unittest.TestCase` base class
2. Add the two methods `setUp()` and `tearDown()` - which run before and after each method
3. Then add your own methods for testing that start with `test_`
4. Make sure to add an [`assert()`](http://docs.python.org/2/library/unittest.html#unittest.TestCase) function, such as as `assertEqual()` so that *something* is actually tested
5. Add the following code snippet to the bottom of the file:
  ```python
  if __name__ == '__main__':
    unittest.main()
  ```

### Example

In this example, save the first file as *multiply.py*. We will be testing this file. Then save the second file, which is used for testing the first file, as *multiply_test.py*.

#### File for testing

```python
def multiply(n1,n2):
    return n1*n2
```

#### unittest

```python
import unittest
import multiply
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass

    def tearDown(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual( multiply(3,4), 12)
 
    def test_strings_a_3(self):
        self.assertEqual( multiply('a',3), 'aaa')
 
if __name__ == '__main__':
    unittest.main()
```

