
import unittest
from discount import Calculator


class Calc(unittest.TestCase):

    def test_calculate_ten_percent_discount(self):
        calc = Calculator()
        result = calc.calc_discount(100, 10, "percentage")
        self.assertEqual(10, result)

    def test_calculate_fifteen_dolar_discount(self):
        calc = Calculator()
        result = calc.calc_discount(100, 15, "dollar")
        self.assertEqual(15, result)

    def test_five_dollar_discount_test(self):
        calc = Calculator()
        result = calc.calc_discount(250, 5, 'dollar')
        self.assertEqual(5, result)

    def test_raise_error(self):
        calc = Calculator()
        self.assertRaises(ValueError, calc.calc_discount, 250, 5, '$')

    def test_floating_point_percentage_discount_test(self):
        calc = Calculator()
        result = calc.calc_discount(100.0, 10.0, 'percentage')
        self.assertEqual(10.0, result)

    def test_floating_point_absolute_discount_test(self):
        calc = Calculator()
        result = calc.calc_discount(250.0, 5.0, 'dollar')
        self.assertEqual(5.0, result)

    def test_percentage_greater_than_100(self):
        calc = Calculator()
        self.assertRaises(
            ValueError, calc.calc_discount, 250, 200, 'percentage')

    def test_discount_greater_than_total(self):
        calc = Calculator()
        self.assertRaises(ValueError, calc.calc_discount, 250, 300, 'dollar')
