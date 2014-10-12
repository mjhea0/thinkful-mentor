from bicycle_class import Bicycle, Customers

if __name__ == '__main__':
    """ Create 6 different bicycle models """
    inventory_list = []
    inventory_list = [Bicycle("Roadster", 25, 150.00),
        Bicycle("Mountaineer", 50, 200),
        Bicycle("Horizontal Hipster", 75, 400),
        Bicycle("Speedster", 25, 290),
        Bicycle("Trail Blazer", 45, 425),
        Bicycle("Single Forever Sitdowner", 65, 650)]

    print "Inventory"
    print "-" * 20
    for i in range(len(inventory_list)):
        print inventory_list[i].modelName, inventory_list[i].weight, \
            inventory_list[i].prodCost, inventory_list[i].shopCost

    """ Create three customers. """
    customer_list = []
    customer_list = [Customers("Michael", 500.0),
        Customers("Charles", 1000),
        Customers("Christine", 200)]
    print '\nCustomers'
    print '-' * 20
    for i in range(len(customer_list)):
        print "{0} has {1} dollars for a new bike.".format(
            customer_list[i].cust_name, customer_list[i].cust_funds)

    print '\nCustomers'
    for i in range(len(customer_list)):
        print '-' * 20
        for x in range(len(inventory_list)):
            if inventory_list[x].prodCost < customer_list[i].cust_funds:
                print "{0} can afford the {1}".format(
                    customer_list[i].cust_name, inventory_list[x].modelName)
    print '-' * 20
