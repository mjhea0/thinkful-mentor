## What does `if __name__ == “__main__”:` do?

Basically all modules have an implicit filename called `__main__`, so `__name__` will be equal to `__main__` when you run the module from the command line. There's a bit of black magic happening. Let's look at an example.

### Create two new files:

first.py:
```python    
# first.py

if __name__ == '__main__':
  print('This print statement is ran from the current module.')
else:
  print('This print statement is ran from a different module.')
```

second.py:
```python
#second.py

import first
```
        
### Now run the files:

```
$ python first.py
This print statement is ran from the current module.

$ python second.py
This print statement is ran from a different module
```

### What's going on?

Behind the scenes, the `__name__` variable is set equal to `"__main__"`, indicating that we're running the statements in the current file rather than importing it. So the first file runs the code within the current module, while the second file imports the code from the first.

### More info

https://www.reddit.com/r/learnpython/comments/9wcan5/where_do_you_use_if_name_main/e9jkvu0/:

At least in theory every Python .py file should have a structure something like this:

```python
#! /usr/bin/env python

def some_function():
    [... code meant to be imported or invoked by other code ...]

def main():
    [... code meant to be run when the file itself is executed ...]

if __name__ == "__main__":
    main()
```

The purpose of the `__name__` guard in this structure is to ensure that the main function is only called when the file is executed, ie via python ./file.py. That allows some_function to be imported from the file without invoking the main function.

Obviously there are some files that have no execution component, such as pure libraries. These then have no need for the guard, unless you specifically want to use it to invoke some self-test code.

There are also some files that have no library component and shall never be imported, but only executed... these too can skip the guard, although the usual practice is to include it so that nothing bad happens if someone accidentally imports the file.

This all works for one specific reason; when directly executed the `__name__` variable in the file being executed will always contain the `__main__ `value.



