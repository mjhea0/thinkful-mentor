# Looping over Multiple Lists

## Lecture

It's common to need to iterate over two lists at once. This is where the built-in `zip` function comes in handy. `zip` will create pairs of elements when passed two lists, and will stop at the end of the shorter list. `zip` can handle three or more lists as well!

## Problem

Compare each pair of elements and print the larger of the two.

```python
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
	# Add your code here!
```

## Answer

```python
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    if a > b:
        print a
    else:
        print b
```

## Output

```
$ python test.py
3
9
17
15
30
```

## Explanation

1. First, you must understand the `zip` function before you can even start this problem. So start analyzing the output of the following:

```
>>> list_a = [3, 9, 17, 15, 19]
>>> list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
>>> test = zip(list_a, list_b)
>>> print test
[(3, 2), (9, 4), (17, 8), (15, 10), (19, 30)]
```

Essentially, `zip` returns a list of tuples from any number of sequences, where the first tuple contains the first item from each sequence, the second tuple contains the second item from each sequence, and so forth.

2. Next, look at the logic in the `for` loop. The loop outputs the greater value in each tuple.

