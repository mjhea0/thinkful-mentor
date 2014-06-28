# This module contains the script that shows an example run of the models
from model import BicycleManufacturer, BicycleShop, Customer


if __name__ == "__main__":
    manufacturer1 = BicycleManufacturer("Manufacturer 1", 0.1)
    manufacturer2 = BicycleManufacturer("Manufacturer 2", 0.2)

    shop = BicycleShop("Freecycle", 0.2, [manufacturer1, manufacturer2])

    shop.get_inventory()

    customer1 = Customer("Customer 1", 200)
    customer2 = Customer("Customer 2", 500)
    customer3 = Customer("Customer 3", 1000)

    customerList = [customer1, customer2, customer3]

    print "\n"
    print "====" * 5
    print "Welcome to {0}".format(shop.get_name())
    print "====" * 5
    print "\nCurrent Inventory:"
    print "-----" * 5
    for bike in shop.get_inventory():
        print "{0}".format(bike)

    for customer in customerList:
        print "\n{0}".format(customer)
        temp = []
        for bike in shop.get_inventory():
            if(bike.get_cost() <= customer.get_funds()):
                temp.append(bike)
        print "You can buy the following bikes:"
        for i in range(len(temp)):
            print "{0} - {1}".format((i+1), temp[i])

        choice = int(raw_input("Which bike #? ")) - 1
        shop.sell_bike(customer, temp[choice])
        print "Bought {0} ${1} left".format(
            customer.get_bike(), customer.get_funds()
        )

    print "\nShop's profit: ${0} !!!!!!".format(shop.get_profit())
