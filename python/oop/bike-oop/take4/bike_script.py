from bike_model import Bicycle, BikeShop, Customer


if __name__ == '__main__':

    """Create six different bicycle models"""
    first_bike = Bicycle("Speedy", 20, 200)
    second_bike = Bicycle("Blazer", 40, 300)
    third_bike = Bicycle("Hip", 35, 650)
    fourth_bike = Bicycle("Downhill", 20, 720)
    fifth_bike = Bicycle("Hop", 45, 475)
    sixth_bike = Bicycle("Skip", 30, 250)

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
    purchase_list = []
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
