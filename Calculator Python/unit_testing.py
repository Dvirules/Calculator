import unittest
from Operators.operator import *
from Operators.plus import *
from Operators.minus import *
from Operators.multiplication import *
from Operators.division import *
from Operators.power import *


class UnitTesting(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(Plus().calculate(1, 2), 1 + 2, "Plus operator does not function as expected")

    def test_minus(self):
        self.assertEqual(Minus().calculate(1, -2), 1 - (-2), "Minus operator does not function as expected")

    def test_multiplication(self):
        self.assertEqual(Multiplication().calculate(-4, 5), -4 * 5, "Multiplication operator does not function as expected")

    def test_division(self):
        self.assertEqual(Division().calculate(10, 3), 10 / 3, "Division operator does not function as expected")

    def test_Power(self):
        self.assertEqual(Power().calculate(2, 3), pow(float(2), float(3)), "Power operator does not function as expected")

    if __name__ == '__main__':
        unittest.main()