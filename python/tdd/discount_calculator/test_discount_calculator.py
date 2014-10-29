import unittest
from discount_calculator import calculate_discount


class DiscountCalculatorTests(unittest.TestCase):

    def testProperDiscount(self):
        discounted_total = calculate_discount(200, 10, 30)
        self.assertEqual(discounted_total, 150)

    def testZeroItemCost(self):
        discounted_total = calculate_discount(0, 10, 30)
        self.assertEqual(discounted_total, 0)

    def testItemCostBelowZero(self):
        discounted_total = calculate_discount(-5, 10, 30)
        self.assertEqual(discounted_total, 0)

    def testDiscountedTotalBelowZero(self):
        discounted_total = calculate_discount(5, 10, 30)
        self.assertEqual(discounted_total, 0)

    def test_negative_discount(self):
        self.assertEqual(200, calculate_discount(200, -25, 0))
        self.assertEqual(17.99, calculate_discount(17.99, 0, -20))

if __name__ == "__main__":
    unittest.main()
