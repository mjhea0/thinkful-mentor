class ShoppingCart(object):

    items_in_cart = {}
    total_amount = 0

    def __init__(self, customer_name):
        self.customer_name = customer_name

    def get_total_items(self):
        for i in self.items_in_cart:
            self.total_amount += self.items_in_cart[i]
        return "The total items in the cart is {}.".format(self.total_amount)

    def add_item(self, item, price):
        self.items_in_cart[item] = price
        return "Added {} to cart Yay!.".format(item)

    def empty_cart(self):
        self.items_in_cart = {}
        return self.items_in_cart

class Items(object):

    def __init__(self, item, item_price):
        self.item = item
        self.item_price = item_price

class Fruit(Items):
    food_group = "fruit"

class Vegetable(Items):
    food_group = "Vegetables"


# go_shopping = ShoppingCart('Mike')

# banana = Fruit('banana', 1)
# print go_shopping.add_item(banana.item, banana.item_price)
# print "State of cart: ", go_shopping.items_in_cart

# cucumber = Vegetable('cucumber', 1)
# print go_shopping.add_item(cucumber.item, cucumber.item_price)
# print "State of cart: ", go_shopping.items_in_cart

# print go_shopping.get_total_items()

# print "Empty the cart: ", go_shopping.empty_cart()
