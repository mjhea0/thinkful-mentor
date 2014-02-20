import unittest
from vending_oop import VendingMachine
import operator

class TestVendingMachine(unittest.TestCase):

    def setUp(self):
        self.vending = VendingMachine(156700)
        self.stock = {'root beer': 10, 'coca-cola': 10, 'sprite': 30}
        self.sorted_stock = sorted(self.stock.items(), key=lambda x: x[1])

    def test_replenish_test(self):
        self.vending.replenish('sprite',20)
        self.assertEqual(self.sorted_stock,[('coca-cola', 10), ('root beer', 10), ('sprite', 30)])

    def test_sell(self):
        self.vending.sell('sprite')
        self.assertEqual(self.sorted_stock,[('coca-cola', 10), ('root beer', 10), ('sprite', 30)])

if __name__ == '__main__':
	unittest.main()
