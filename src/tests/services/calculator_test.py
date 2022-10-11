import unittest
from services.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_calculate(self):
        # single number or function
        self.assertEqual(self.calculator.calculate('4'),
                         '4.0')
        self.assertEqual(self.calculator.calculate('pi'),
                         '3.141592653589793')
        self.assertEqual(self.calculator.calculate('-42'),
                         '-42.0')
        self.assertEqual(self.calculator.calculate('-pi'),
                         '-3.141592653589793')
        self.assertEqual(self.calculator.calculate('4.3'),
                         '4.3')
        self.assertEqual(self.calculator.calculate('-62.6'),
                         '-62.6')
        self.assertEqual(self.calculator.calculate('sin(3)'),
                         '0.052335956242943835')
        self.assertEqual(self.calculator.calculate('-sin(3)'),
                         '-0.052335956242943835')
        self.assertEqual(self.calculator.calculate('sqrt(16)'),
                         '4.0')
        self.assertEqual(self.calculator.calculate('-sqrt(16)'),
                         '-4.0')
        self.assertEqual(self.calculator.calculate('tan(6)'),
                         '0.10510423526567647')
        self.assertEqual(self.calculator.calculate('-tan(6)'),
                         '-0.10510423526567647')
        # addition
        self.assertEqual(self.calculator.calculate('3+4'),
                         '7.0')
        self.assertEqual(self.calculator.calculate('3.8+4.5'),
                         '8.3')
        self.assertEqual(self.calculator.calculate('-32.8+4.5'),
                         '-28.299999999999997')
        self.assertEqual(self.calculator.calculate('pi+8.2'),
                         '11.341592653589792')
        # subtraction
        self.assertEqual(self.calculator.calculate('4-3'),
                         '1.0')
        self.assertEqual(self.calculator.calculate('5.8-4.5'),
                         '1.2999999999999998')
        self.assertEqual(self.calculator.calculate('-32.8-8.6'),
                         '-41.4')
        self.assertEqual(self.calculator.calculate('pi-85.2'),
                         '-82.0584073464102')
        # multiplication
        self.assertEqual(self.calculator.calculate('4*3'),
                         '12.0')
        self.assertEqual(self.calculator.calculate('5.8*4.5'),
                         '26.099999999999998')
        self.assertEqual(self.calculator.calculate('-22.8*-8.6'),
                         '196.07999999999998')
        self.assertEqual(self.calculator.calculate('pi*73.2'),
                         '229.96458224277288')
        # division
        self.assertEqual(self.calculator.calculate('12/3'),
                         '4.0')
        self.assertEqual(self.calculator.calculate('54.8/4.5'),
                         '12.177777777777777')
        self.assertEqual(self.calculator.calculate('-22.8/-8.6'),
                         '2.6511627906976747')
        self.assertEqual(self.calculator.calculate('64/pi'),
                         '20.371832715762604')
        self.assertEqual(self.calculator.calculate('6/.2'),
                         '30.0')
        self.assertEqual(self.calculator.calculate('81/0'),
                         'error')
        # exponentiation
        self.assertEqual(self.calculator.calculate('12^3'),
                         '1728.0')
        self.assertEqual(self.calculator.calculate('54.8^4.5'),
                         '66759413.585069165')
        self.assertEqual(self.calculator.calculate('-22.8^-8'),
                         '1.3693713080107839e-11')
        self.assertEqual(self.calculator.calculate('64^pi'),
                         '472369.37932353455')
        self.assertEqual(self.calculator.calculate('6^.2'),
                         '1.4309690811052556')
        self.assertEqual(self.calculator.calculate('81^0'),
                         '1.0')
        #  Python's exponent function '**' returns a complex number when
        #  a number k where k < 0 is raised to a fractional power.
        self.assertEqual(self.calculator.calculate('-3^1.56'),
                         'error')
        self.assertEqual(self.calculator.calculate('-15^sqrt(6)'),
                         'error')

        # combinations
        self.assertEqual(self.calculator.calculate('3+4*2'),
                         '11.0')
        self.assertEqual(self.calculator.calculate('(3+4)*2'),
                         '14.0')
        self.assertEqual(self.calculator.calculate('3-(-12)'),
                         '15.0')
        self.assertEqual(self.calculator.calculate('60.0*(-2)+3'),
                         '-117.0')
        self.assertEqual(self.calculator.calculate('3--12'),
                         '15.0')
        self.assertEqual(self.calculator.calculate('2^4-2'),
                         '14.0')
        self.assertEqual(self.calculator.calculate('2^(4-2)'),
                         '4.0')
        self.assertEqual(self.calculator.calculate('5^8'),
                         '390625.0')
        self.assertEqual(self.calculator.calculate('8^8/2'),
                         '8388608.0')
        self.assertEqual(self.calculator.calculate('2^-3'),
                         '0.125')
        self.assertEqual(self.calculator.calculate('2^--3'),
                         '8.0')
        self.assertEqual(self.calculator.calculate('4/-2'),
                         '-2.0')
        self.assertEqual(self.calculator.calculate('4*-2'),
                         '-8.0')
        self.assertEqual(self.calculator.calculate('sqrt(4)'),
                         '2.0')
        self.assertEqual(self.calculator.calculate('6+sqrt(4)'),
                         '8.0')
        self.assertEqual(self.calculator.calculate('6.3*sqrt(4.5)'),
                         '13.364318164425747')
        self.assertEqual(self.calculator.calculate('sqrt4'),
                         ['error'])
        self.assertEqual(self.calculator.calculate('4sqrt('),
                         ['error'])
        self.assertEqual(self.calculator.calculate('pisin('),
                         ['error'])
        self.assertEqual(self.calculator.calculate('sqrt('),
                         ['error'])
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
        self.assertEqual(self.calculator.handle_operator(['error'], ''),
                         ['error'])

    def test_handle_pi(self):
        self.assertEqual(self.calculator.handle_pi(['3', 'pi', ]),
                         ['3', '3.141592653589793'])
        self.assertEqual(self.calculator.handle_pi(['-pi', '3']),
                         ['-3.141592653589793', '3'])

    def test_evaluate_pi(self):
        self.assertEqual(self.calculator.evaluate_pi('pi'),
                         3.141592653589793)
        self.assertEqual(self.calculator.evaluate_pi('-pi'),
                         -3.141592653589793)

    def test_handle_function(self):
        self.assertEqual(self.calculator.handle_function(['4'], 'sqrt'),
                         ['2.0'])
        self.assertEqual(self.calculator.handle_function(['4'], 'sin'),
                         ['0.0697564737441253'])
        self.assertEqual(self.calculator.handle_function([], 'sqrt'),
                         ['error'])
