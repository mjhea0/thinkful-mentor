## Problem

For this project, we'll imagine that you've been hired by a business analyst to build a system that models the bicycle industry. You need to be able to model bicycles, which have a fixed cost to produce, bike shops, which sell bicycles with an added margin on top, and customers, who have different budgets for buying a bicycle.

### Requirements

#### Design Python classes

You should create classes to represent each of the following parts of our model:

##### Bicycle

1. Have a model name
1. Have a weight
1. Have a cost to produce

##### Bike Shops

1. Have a name
1. Have an inventory of different bicycles
1. Sell bicycles with a margin over their cost
1. Can see how much profit they have made from selling bikes

##### Customers

1. Have a name
1. Have a fund of money to buy a bike
1. Can buy and own a new bicycle

### Write a script to test your classes

The script should:

1. Import your classes from a separate file.
1. Create a bicycle shop that has 6 different bicycle models in stock. The shop should charge its customers 20% over the cost of the bikes.
1. Create three customers. One customer has a budget of $200, the second $500, and the third $1000.
1. Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget. Make sure you price the bikes in such a way that each customer can afford at least one.
1. Print the initial inventory of the bike shop for each bike it carries.

1. Have each of the three customers purchase a bike then print the name of the bike the customer purchased, the cost, and how much money they have left over in their bicycle fund.
1. After each customer has purchased their bike, the script should print out the bicycle shop's remaining inventory for each bike, and how much profit they have made selling the three bikes.

## Approach

Approach each requirement individually. Start with setting up the attributes, testing as you go, and then create the actions (e.g., methods).

##### Bicycle

1. Have a model name
1. Have a weight
1. Have a cost to produce

Class:

```python
class Bicycle(object):
    """
    Bicycles have a model name, a weight, and a cost to produce.
    """
    def __init__(self, model_name, weight, cost_to_produce):
        self.model_name = model_name
        self.weight = weight
        self.cost_to_produce = cost_to_produce

    def __repr__(self):
        return "{0} weighs {1} pounds and costs ${2} to produce.".format(
            self.model_name, self.weight, self.cost_to_produce)
```

Test:

```python
from bike_model import Bicycle


if __name__ == '__main__':

    """Create 6 different bicycle models"""
    first_bike = Bicycle("Speedy", 20, 200)
    second_bike = Bicycle("Blazer", 40, 300)
    third_bike = Bicycle("Hip", 35, 650)
    fourth_bike = Bicycle("Downhill", 20, 720)
    fifth_bike = Bicycle("Hop", 45, 475)
    sixth_bike = Bicycle("Skip", 30, 250)

    print first_bike
```

##### Bike Shops

1. Have a name
1. Have an inventory of different bicycles

Class:

```python
class BikeShop(object):
    """
    Bike Shops have a name and an inventory.
    """
    def __init__(self, shop_name, shop_inventory):
        self.shop_name = shop_name
        self.shop_inventory = shop_inventory
```

Test:

```python
"""Create a bicycle shop that has six different bicycle models in stock"""
inventory_list = [
    first_bike, second_bike, third_bike, fourth_bike, fifth_bike, sixth_bike
]

bike_shop = BikeShop("Bikes on Broadway", inventory_list)
print "\nShop name: {0}.".format(bike_shop.shop_name)

"""Print the initial inventory of the bike shop for each bike it carries."""
print "\nInventory"
print "-" * 20
for bike in range(len(inventory_list)):
    print inventory_list[bike]
```

##### Customers

1. Have a name
1. Have a fund of money to buy a bike

Class:

```python
class Customer(object):
    """
    Customers have a name and fund of money.
    """
    def __init__(self, customer_name, customer_funds):
        self.customer_name = customer_name
        self.customer_funds = customer_funds

    def __repr__(self):
        return "{0} has ${1}.".format(
            self.customer_name, self.customer_funds)
```

Test:

```python
"""Create three customers"""
first_customer = Customer("Joe", 200)
second_customer = Customer("Michael", 500)
third_customer = Customer("Danny", 1000)

customer_list = [first_customer, second_customer, third_customer]

print '\nCustomers'
print '-' * 20
for customer in range(len(customer_list)):
    print customer_list[customer]

"""
Print the name of each customer
and a list of the bikes offered by the bike
shop that they can afford given their budget.
Make sure you price the bikes in such a way
that each customer can afford at least one.
"""

print '\nWhich bikes can they afford?'
for customer in range(len(customer_list)):
    print '-' * 20
    for bike in range(len(inventory_list)):
        if inventory_list[bike].cost_to_produce <= \
                customer_list[customer].customer_funds:
            print "{0} can afford the {1}".format(
                customer_list[customer].customer_name,
                inventory_list[bike].model_name
            )
print '-' * 20
```

##### Customers

1. Can buy and own a new bicycle
