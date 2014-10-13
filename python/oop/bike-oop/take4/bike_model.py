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


class BikeShop(object):
    """
    Bike Shops have a name and an inventory.
    """
    def __init__(self, shop_name, shop_inventory):
        self.shop_name = shop_name
        self.shop_inventory = shop_inventory


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
