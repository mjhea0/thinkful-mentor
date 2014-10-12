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