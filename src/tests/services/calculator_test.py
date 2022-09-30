import unittest
from services.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_calculate(self):
        self.assertEqual(self.calculator.calculate('3+4'),
                         '7.0')
        self.assertEqual(self.calculator.calculate('3+4*2'),
                         '11.0')
        self.assertEqual(self.calculator.calculate('3-(-12)'),
                         '15.0')
        self.assertEqual(self.calculator.calculate('3--12'),
                         '15.0')
        self.assertEqual(self.calculator.calculate('2^4'),
                         '16.0')

    def test_handle_operator(self):
        self.assertEqual(self.calculator.handle_operator(['3', '4', '2'], '*'),
                         ['3', '8.0'])
        self.assertEqual(self.calculator.handle_operator(['3', '4'], '+'),
                         ['7.0'])
        self.assertEqual(self.calculator.handle_operator(['3', '2', '3'], '^'),
                         ['3', '8.0'])
        self.assertEqual(self.calculator.handle_operator(['3'], '*'),
                         ['0.0'])
        self.assertEqual(self.calculator.handle_operator([], '*'),
                         ['error'])
        self.assertEqual(self.calculator.handle_operator(['3', '0',], '/'),
                         ['error'])