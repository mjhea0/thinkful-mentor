# Python OOP

In the world of Object Oriented Programming, *things* are represented as objects. Objects, which are created, or instantiated, by defining classes store data (or fields) as well as associated operations (or methods).


1. Defining a class
2. Initilizer

4. Instance Methods
5. Class Methods
6. Static Methods

## Defining a class

Defining a class is simple:

```python
class Dog(object):
```

Start with the reserved `class` keyword, then add the name of the class (using CamelCase notation), and then within the parenthesis, add the class you are sublassing or inheriting from. In the example, we are inheriting from the default `object` class.

## Initilizer

All classes create objects. In order to do this, we must use an `__init__()` function to initialze each object. The function itself must have at least one argument as well as the `self` keyword, which refers to the object. 


```python
class Dog(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Each instance of the `Dog` class will have a `name` and `age` specific to that instance. In other words, each do will have a unique name and age.




-Create a class for dogs
-The dog should have a method called bark which prints "ruff ruff"
-dogs should have an age property and a name property
-create two dogs, Philo and Mikey
-save this file as dogs.py
