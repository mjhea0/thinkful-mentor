# Primer on Object-Oriented Programming in Python

Object-oriented programming (OOP) is a programming paradigm that organizes your code eloquently into classes and objects.

## Defining a class

Defining a class is simple:

```python
class Dog(object):
    # class attributes and methods go here
```

Start with the `class` keyword, add the name of the class (using CamelCase notation), and then within the parenthesis, add the class you are sublassing or inheriting from. In this example, we are inheriting from the default `object` class.

In essence, classes are blueprints for the associated instances, attributes, and methods.

## Instance Attributes

All classes create objects, and all objects contain characteristics called attributes. Use the `__init__()` function to initialze an object's attributes (commonly referred to as instance attributes). The function itself must have at least one argument as well as the `self` keyword, which refers to the object itself. 

```python
class Dog(object):

	# Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Each instance of the `Dog` class will have a `name` and `age` specific to that instance. In other words, each dog will have a unique name and age.

## Class Attributes

While instance attributes are specific to each object, class attributes are the same for all instances.

```python
class Dog(object):

	# Class Attribute
	species = 'mammal'

	# Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

So while each dog will have a unique name and age, every dog is a mammal.


## Instantiating

Let's create (or instantiate) two dogs:

```python
class Dog(object):

	# Class Attribute
	species = 'mammal'

	# Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

# access the instance attributes
print philo.name, philo.age
print mikey.name, mikey.age
```

Notice how we use dot notation to access attributes of each object.

## Instance Methods

Instance methods are functions defined inside a class and are used to perform operations with the attributes of our objects. Like initializers, the first argument is always `self`.

```python
class Dog(object):

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return self.name, self.age

    # instance method
    def speak(self, sound):
        return "%s says %s" % (self.name, sound)

# Instantiate the Dog object
mikey = Dog("Mikey", 6)

# call our instance method
print mikey.description()
print mikey.speak("Gruff Gruff")
```

## Class Methods

Like class attributes, class methods are applied to each instance. They always take the keyword `cls` as the first argument.

```python
class Dog(object):

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return self.name, self.age

    # instance method
    def speak(self, sound):
        return "%s says %s" % (self.name, sound)

    # class method
    def get_species(cls):
        return cls.species


# Instantiate the Dog object
mikey = Dog("Mikey", 6)

# call our class method
print mikey.get_species()
```

## Inheritence

Inheritance is the process by which one class takes on the attributes and methods of another. Newly formed classes are called derived (or sub) classes, and the classes that we derive from are called base classes. It's important to note that derived classes override or extend the functionality of base classes.

```python
examples!!!!
```

