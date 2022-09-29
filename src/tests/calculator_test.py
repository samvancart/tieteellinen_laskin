import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_calculate(self):
        self.assertEqual(self.calculator.calculate('3+4'),
                         '7')
        self.assertEqual(self.calculator.calculate('3+4*2'),
                         '11')
        self.assertEqual(self.calculator.calculate('3-(-12)'),
                         '15')
        self.assertEqual(self.calculator.calculate('3--12'),
        '15')

    