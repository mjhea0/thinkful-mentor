## What does `if __name__ == “__main__”:` do?

Basically all modules have an implicit filename called `__main__`, so when you use the `__name__ == '__main__'` statement, you are basically running that module. There's a bit of black magic happening. Let's look at an example.

### Create two new files:

first.py:
```python    
# first.py

if __name__ == '__main__':
  print 'This print statement is ran from the current module.'
else:
  print 'This print statement is ran from a different module'
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

By setting the `__name__` variable equal to `"__main__"`, we indicate that we're running the statements in the current module (since each module has an rather than importing it. So the first file runs the code within the current module, while teh second file imports the code from the first.




