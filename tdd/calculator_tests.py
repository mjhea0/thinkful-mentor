import unittest
from calculator import Calculator
 
class TddInPythonExample(unittest.TestCase):
 
   def test_calculator_add_method_returns_correct_result(self):
      calc = Calculator()
      result = calc.add(2,2)
      self.assertEqual(4, result)
