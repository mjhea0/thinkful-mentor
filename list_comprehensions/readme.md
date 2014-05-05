# Python List Comprehensions

Python supports a concept called "list comprehensions", which can be a bit confusing at first - but once mastered, it can be used to construct lists in a natural, easy way.

## Part 1: Intro

Let’s start with looking at simple list. It's common to construct a new list based on values from an existing list after they, say, are filtered. 

```python
def create_list(alpha_list):
    beta_list = []
    for letter in alpha_list:
        if filter(letter):
            beta_list.append(letter)
    return beta_list


def filter(letter):
    return letter >= 'B'


alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
print create_list(alpha_list)
```

In this example, we are creating a new list, `beta_list` of letters greater than or equal to 'B' by iterating through the `alpha_list` and applying the appropriate filter on the list.

When you run this code you should see:

```
['B', 'C', 'D', 'E', 'F', 'G', 'H']
```

How do we do this with a list comprehension: 

```python
# intro - ex2


def create_list(alpha_list):
    # Read statements, left to right
    return [letter for letter in alpha_list if filter(letter)]


def filter(letter):
    return letter >= 'B'


alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
print create_list(alpha_list)
```

Run the code. You should see the same output. Now read it outloud, left to write: "return the letter for each letter in `alpha_list` if it's greater than or equal to 'B'". Simple, right?