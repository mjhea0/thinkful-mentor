import unittest

from shop import ShoppingCart, Items, Fruit, Vegetable

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.go_shopping = ShoppingCart('Mike')
        self.banana = Fruit('banana', 1)

    def test_get_total_items(self):
        pass

    def test_add_item_to_cart(self):
        self.go_shopping.add_item(self.banana.item, self.banana.item_price)
        self.assertEqual(self.go_shopping.items_in_cart, {'banana':1})

    def test_empty_shopping_cart(self):
        pass
        

if __name__ == '__main__':
    unittest.main()
