class Bicycle(object):
    def __init__(self, model_name, bike_weight, bike_cost):
        self.model_name = model_name
        self.bike_weight = bike_weight
        self.bike_cost = bike_cost


class BikeShop(Bicycle):
    def __init__(self, shop_name, inventory):
        self.shop_name = shop_name
        self.inventory = inventory
        self.profit = 0

    def get_shop_name(self):
        return self.shop_name

    def get_inventory(self):
        return self.inventory


class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.own_bike = None


if __name__ == '__main__':

    # bike models for inventory
    hybrid = Bicycle("hybrid", 20, 400)
    bmx = Bicycle("bmx", 10, 80)
    road = Bicycle("road", 15, 560)
    mountain = Bicycle("mountain", 30, 320)
    racing = Bicycle("racing", 10, 640)
    cruiser = Bicycle("cruiser", 40, 160)

    initial_inventory = [hybrid, bmx, road, mountain, racing, cruiser]

    shop = BikeShop("Freddys Bicycles", initial_inventory)

    # customers
    josh = Customer("Josh", 1000)
    john = Customer("John", 500)
    joan = Customer("Joan", 200)

    customersList = [josh, john, joan]

    print "Welcome to {}!".format(shop.get_shop_name())
    print "Current Inventory:"
    print "Model - Weight - Cost"
    for bike in shop.get_inventory():
        print "{0} {1} ${2}".format(bike.model_name, bike.bike_weight, bike.bike_cost)

#    for buyer in customerList:
#      if bike price <=  buyer.budget:
#           print "Here are the bikes within your budget: ".format(bike)
#      choose one bike and make it = customer.own_bike
#      print "{0} just purchased {1} at {2} and have {3} left over".format(customer, bike price, remaining budget)
