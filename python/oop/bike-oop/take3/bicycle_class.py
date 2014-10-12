class Bicycle(object):
    """
    Bicycles have a model name, a weight, and a cost to produce.
    """
    def __init__(self, modelName, weight, prodCost):
        self.modelName = modelName
        self.weight = weight
        self.prodCost = prodCost
        self.shopCost = prodCost * 1.20


class BikeShops(object):
    """
    Bike Shops have a name, an inventory.
    Bike shops also sell bikes for a profit and can report that profit.
    """
    def __init__(self, shop_name, shop_inventory, shop_markup):
        self.shop_name = shop_name
        self.shop_inventory = shop_inventory
        self.shop_markup = shop_markup


class Customers(object):
    def __init__(self, cust_name, cust_funds):
        super(Customers, self).__init__()
        self.cust_name = cust_name
        self.cust_funds = cust_funds
