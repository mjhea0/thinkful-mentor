import unittest

from shop import ShoppingCart, Items, Fruit, Vegetable

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.go_shopping = ShoppingCart('Mike')
        self.banana = Fruit('banana', 1)
        self.cucumber = Vegetable('cucumber', 3)

    def test_get_total_items(self):
        self.go_shopping.add_item(self.banana.item, self.banana.item_price)
        self.go_shopping.add_item(self.cucumber.item, self.cucumber.item_price)
        self.assertEqual(len(self.go_shopping.items_in_cart),2)

    def test_add_item_to_cart(self):
        self.go_shopping.add_item(self.banana.item, self.banana.item_price)
        self.assertEqual(self.go_shopping.items_in_cart, {'banana':1})

    def test_empty_shopping_cart(self):
        self.go_shopping.add_item(self.banana.item, self.banana.item_price)
        self.go_shopping.add_item(self.cucumber.item, self.cucumber.item_price)
        self.go_shopping.empty_cart()
        self.assertEqual(len(self.go_shopping.items_in_cart),0)

if __name__ == '__main__':
    unittest.main()
