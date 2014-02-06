# Python OOP

In the world of Object Oriented Programming, *things* are represented as objects. Objects, which are created, or instantiated, by defining classes store data (or fields) as well as associated operations (or methods).

## Defining a class

Defining a class is simple:

```python
class Dog(object):
```

Start with the reserved `class` keyword, then add the name of the class (using CamelCase notation), and then within the parenthesis, add the class you are sublassing or inheriting from. In the example, we are inheriting from the default `object` class.

## Class Attributes (member variables)

ruff ruff 

is_alive = "True"

## Initilizer

All classes create objects. In order to do this, we must use an `__init__()` function to initialze each object. The function itself must have at least one argument as well as the `self` keyword, which refers to the object. 


```python
class Dog(object):
	is_alive = "True"

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

## Methods


```python
class Dog(object):
	is_alive = "True"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print self.name
        print self.age
```

second_dog = Dog("Mikey", 6)
print second_dog.description



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



