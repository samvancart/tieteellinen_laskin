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
        self.assertEqual(self.calculator.calculate('8^9'),
                         '134217728.0')
        self.assertEqual(self.calculator.calculate('5^8'),
                         '390625.0')
        self.assertEqual(self.calculator.calculate('8^8'),
                         '16777216.0')
        self.assertEqual(self.calculator.calculate('2^-3'),
                         '0.125')
        self.assertEqual(self.calculator.calculate('2^--3'),
                         '8.0')
        self.assertEqual(self.calculator.calculate('4/-2'),
                         '-2.0')
        self.assertEqual(self.calculator.calculate('4*-2'),
                         '-8.0')
        self.assertEqual(self.calculator.calculate('4'),
                         '4.0')
        self.assertEqual(self.calculator.calculate('pi'),
                         '3.141592653589793')
        self.assertEqual(self.calculator.calculate(''),
                         ['error'])

    def test_handle_operator(self):
        self.assertEqual(self.calculator.handle_operator(['3', '4', '2'], '*'),
                         ['3', '8.0'])
        self.assertEqual(self.calculator.handle_operator(['3', '4'], '+'),
                         ['7.0'])
        self.assertEqual(self.calculator.handle_operator(['3', '2', '3'], '^'),
                         ['3', '8.0'])
        self.assertEqual(self.calculator.handle_operator(['3'], '*'),
                         ['3.0'])
        self.assertEqual(self.calculator.handle_operator([], '*'),
                         ['error'])
        self.assertEqual(self.calculator.handle_operator(['3', '0', ], '/'),
                         ['error'])

    def test_handle_function(self):
        self.assertEqual(self.calculator.handle_function(['3', 'pi', ]),
                         ['3', '3.141592653589793'])
        self.assertEqual(self.calculator.handle_function(['-pi', '3']),
                         ['-3.141592653589793', '3'])
