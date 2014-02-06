# Python OOP

In the world of Object Oriented Programming, *things* are represented as objects. Objects, which are created, or instantiated, by defining classes store data (or fields) as well as associated operations (or methods).

## Defining a class

Defining a class is simple:

```python
class Dog(object):
```

Start with the reserved `class` keyword, then add the name of the class (using CamelCase notation), and then within the parenthesis, add the class you are sublassing or inheriting from. In the example, we are inheriting from the default `object` class.

## Class Attributes

ruff ruff 

## Initilizer

All classes create objects. In order to do this, we must use an `__init__()` function to initialze each object. The function itself must have at least one argument as well as the `self` keyword, which refers to the object. 


```python
class Dog(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Each instance of the `Dog` class will have a `name` and `age` specific to that instance. In other words, each do will have a unique name and age.

## Instantiang

Let's create two dogs:

```python
first_dog = Dog("Philo", 5)
print first_dog.name, first_dog.age

second_dog = Dog("Mikey", 6)
print second_dog.name, first_dog.name
```

Notice how we use dot notation to access attributes of each object.

## Scope
