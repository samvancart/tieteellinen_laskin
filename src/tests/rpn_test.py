import unittest
from rpn import Rpn


class TestRpn(unittest.TestCase):
    def setUp(self):
        self.rpn = Rpn()

    def test_get_numbers(self):
        self.assertEqual(self.rpn.get_numbers(),
                         ['0', '1', '2', '3', '4', '5', '6', '7', '9', 'pi'])

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
        self.assertEqual(self.rpn.get_reverse_polish('3+4*2'),
                         ['3', '4', '2', '*', '+'])
        self.assertEqual(self.rpn.get_reverse_polish('3+4*2/2'),
                         ['3', '4', '2', '*', '2', '/', '+'])
        self.assertEqual(self.rpn.get_reverse_polish('3+4*2/(1-5)^2^3'),
                         ['3', '4', '2', '*', '1', '5', '-', '2', '3', '^', '^', '/', '+'])
        self.assertEqual(self.rpn.get_reverse_polish('((1)*2)'),
                         ['1', '2', '*'])
        self.assertEqual(self.rpn.get_reverse_polish('((1)*)2'),
                         None)
        self.assertEqual(self.rpn.get_reverse_polish('1**2'),
                         None)
        self.assertEqual(self.rpn.get_reverse_polish('sin(max(2,3)/3*pi)'),
                         ['2', '3', 'max', '3', '/', 'pi', '*', 'sin'])

        self.assertEqual(self.rpn.get_reverse_polish('3'),
                         ['3'])
        self.assertEqual(self.rpn.get_reverse_polish('-3'),
                         ['3', '-'])
        self.assertEqual(self.rpn.get_reverse_polish('3-(-12)'),
                         ['3', '12', '+',])
        self.assertEqual(self.rpn.get_reverse_polish('20*30'),
                         ['20', '30', '*'])

        # Make method clean_input for special case
        # self.assertEqual(self.kpn.get_reverse_polish('+++1'),
        #     ['1'])
        # Check if needs to throw syntax error for empty parenthesis
        self.assertEqual(self.rpn.get_reverse_polish('()'),
                         [])
        self.assertEqual(self.rpn.get_reverse_polish('((()))'),
                         [])

        """Test for mismatched parenthesis"""
        self.assertEqual(self.rpn.get_reverse_polish('(3+4'),
                         None)
        self.assertEqual(self.rpn.get_reverse_polish('3+4)'),
                         None)
        self.assertEqual(self.rpn.get_reverse_polish('3+4*2/1-5)^2)^3'),
                         None)
        self.assertEqual(self.rpn.get_reverse_polish('3+4*2/(1-5^2^3'),
                         None)
        self.assertEqual(self.rpn.get_reverse_polish('3+4*2/(1-5(^2^3'),
                         None)
        self.assertEqual(self.rpn.get_reverse_polish('())'),
                         None)
        self.assertEqual(self.rpn.get_reverse_polish('(()'),
                         None)

    def test_str_input_to_list(self):
        self.assertEqual(self.rpn.str_input_to_list('3+4'),
                         ['3', '+', '4'])
        self.assertEqual(self.rpn.str_input_to_list('3564562+445*6+sin(40)'),
                         ['3564562', '+', '445', '*', '6', '+', 'sin', '(', '40', ')'])
        self.assertEqual(self.rpn.str_input_to_list('++3--+4'),
                         ['+', '+', '3', '-', '-', '+', '4'])
        self.assertEqual(self.rpn.str_input_to_list('(3+(4))'),
                         ['(', '3', '+', '(', '4', ')', ')'])
        self.assertEqual(self.rpn.str_input_to_list('20*30'),
                         ['20', '*', '30'])
        self.assertEqual(self.rpn.str_input_to_list('3-(-12)'),
                         ['3', '-', '(', '-', '12', ')'])

    def test_clean_input(self):
        self.assertEqual(self.rpn.clean_input(['3', '+', '-', '4']),
                         ['3', '-', '4'])
        self.assertEqual(self.rpn.clean_input(['3', '-', '-', '4']),
                         ['3', '+', '4'])
        self.assertEqual(self.rpn.clean_input(['3', '-', '(', '-', '12', ')']),
                         ['3', '+', '(', '12', ')'])
