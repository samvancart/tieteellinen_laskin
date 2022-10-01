import unittest
from services.rpn import Rpn


class TestRpn(unittest.TestCase):
    def setUp(self):
        self.rpn = Rpn()

    def test_get_numbers(self):
        self.assertEqual(self.rpn.get_numbers(),
                         ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'pi'])

    def test_get_operators_dict(self):
        self.assertEqual(self.rpn.get_operators_dict(),
                         [{'value': '+', 'precedence': 1, 'associativity': 0},
                          {'value': '-', 'precedence': 1, 'associativity': 0},
                          {'value': '*', 'precedence': 2, 'associativity': 0},
                          {'value': '/', 'precedence': 2, 'associativity': 0},
                          {'value': '^', 'precedence': 3, 'associativity': 1}])

    def test_get_operators(self):
        self.assertEqual(self.rpn.get_operators(),
                         ['+', '-', '*', '/', '^'])

    def test_get_functions(self):
        self.assertEqual(self.rpn.get_functions(),
                         ['sin', 'cos', 'tan', 'sqrt', 'min', 'max'])

    def test_get_reverse_polish(self):
        self.assertEqual(self.rpn.get_reverse_polish('3+4'),
                         ['3', '4', '+'])
        self.assertEqual(self.rpn.get_reverse_polish('(3+4)'),
                         ['3', '4', '+'])
        self.assertEqual(self.rpn.get_reverse_polish('++3--+4'),
                         ['3', '4', '+'])
        self.assertEqual(self.rpn.get_reverse_polish('3+4*2'),
                         ['3', '4', '2', '*', '+'])
        self.assertEqual(self.rpn.get_reverse_polish('3+4*2/2'),
                         ['3', '4', '2', '*', '2', '/', '+'])
        self.assertEqual(self.rpn.get_reverse_polish('3+4*2/(1-5)^2^3'),
                         ['3', '4', '2', '*', '1', '5', '-', '2', '3', '^', '^', '/', '+'])
        self.assertEqual(self.rpn.get_reverse_polish('((1)*2)'),
                         ['1', '2', '*'])
        self.assertEqual(self.rpn.get_reverse_polish('sin(max(2,3)/3*pi)'),
                         ['2', '3', 'max', '3', '/', 'pi', '*', 'sin'])
        self.assertEqual(self.rpn.get_reverse_polish('3'),
                         ['3'])
        self.assertEqual(self.rpn.get_reverse_polish('-3'),
                         ['-3',])
        self.assertEqual(self.rpn.get_reverse_polish('3-(-12)'),
                         ['3', '-12', '-', ])
        self.assertEqual(self.rpn.get_reverse_polish('20*30'),
                         ['20', '30', '*'])
        self.assertEqual(self.rpn.get_reverse_polish('3-(-5-5)'),
                         ['3', '-5', '5', '-', '-'])
        self.assertEqual(self.rpn.get_reverse_polish('()'),
                         [])
        self.assertEqual(self.rpn.get_reverse_polish('((()))'),
                         [])

         # Errors found at validation
        self.assertEqual(self.rpn.get_reverse_polish('((1)*)2'),
                         None)
        self.assertEqual(self.rpn.get_reverse_polish('1**2'),
                         None)
        self.assertEqual(self.rpn.get_reverse_polish('3-(-5(-5))'),
                         None)
        self.assertEqual(self.rpn.get_reverse_polish('3+4*2/(1-5(^2^3'),
                         None)

        # Errors found at shunting_yard
        self.assertEqual(self.rpn.get_reverse_polish('(3+4'),
                         ['error'])
        self.assertEqual(self.rpn.get_reverse_polish('3+4)'),
                         ['error'])
        self.assertEqual(self.rpn.get_reverse_polish('3+4*2/1-5)^2)^3'),
                        ['error'])
        self.assertEqual(self.rpn.get_reverse_polish('3+4*2/(1-5^2^3'),
                         ['error'])
        self.assertEqual(self.rpn.get_reverse_polish('())'),
                         ['error'])
        self.assertEqual(self.rpn.get_reverse_polish('(()'),
                         ['error'])