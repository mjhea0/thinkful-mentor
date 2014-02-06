# Python OOP

Object-oriented programming (OOP) is a programming paradigm that organizes your code eloquently into classes and objects.

## Defining a class

Defining a class is simple:

```python
class Dog(object):
```

Start with the `class` keyword, add the name of the class (using CamelCase notation), and then within the parenthesis, add the class you are sublassing or inheriting from. In this example, we are inheriting from the default `object` class.

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


## Real world Example

```python
class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name
		
    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."
		
    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."

my_cart = ShoppingCart("Michael")
my_cart.add_item("bread", 10)

```


## Inheritence

Inheritance is the process by which one class takes on the attributes and methods of another.

```python
class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id
	
    def display_cart(self):
        print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()
```

## Superclass




## Example

```python
class Triangle(object):
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False
            
class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle        
    
my_triangle = Triangle(10, 90, 80)

print my_triangle.number_of_sides
print my_triangle.check_angles()
```



