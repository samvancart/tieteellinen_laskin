import unittest
from services.input_handler import InputHandler


class TestInputHandler(unittest.TestCase):
    def setUp(self):
        self.input_handler = InputHandler()

    def test_get_position(self):
        self.assertEqual(self.input_handler.get_position('--3'),
                         2)
        self.assertEqual(self.input_handler.get_position('3'),
                         1)

    def test_str_input_to_list(self):
        self.assertEqual(self.input_handler.str_input_to_list('3+4'),
                         ['3', '+', '4'])
        self.assertEqual(self.input_handler.str_input_to_list('3564562+445*6+sin(40)'),
                         ['3564562', '+', '445', '*', '6', '+', 'sin', '(', '40', ')'])
        self.assertEqual(self.input_handler.str_input_to_list('++3--+4'),
                         ['3', '+', '4'])
        self.assertEqual(self.input_handler.str_input_to_list('+--++3+(---++4)'),
                         ['3', '+', '(', '-4', ')'])
        self.assertEqual(self.input_handler.str_input_to_list('(3+(4))'),
                         ['(', '3', '+', '(', '4', ')', ')'])
        self.assertEqual(self.input_handler.str_input_to_list('20*30'),
                         ['20', '*', '30'])
        self.assertEqual(self.input_handler.str_input_to_list('3-(-12)'),
                         ['3', '-', '(', '-12', ')'])
        self.assertEqual(self.input_handler.str_input_to_list('3.2-(-12.52)'),
                         ['3.2', '-', '(', '-12.52', ')'])
        self.assertEqual(self.input_handler.str_input_to_list('-3.2-(12.52)'),
                         ['-3.2', '-', '(', '12.52', ')'])
        self.assertEqual(self.input_handler.str_input_to_list(''),
                         ['error'])

    def test_is_number(self):
        numbers = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'pi',
            '-0', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9', '-pi',
            '0.8', '1.8', '2.8', '3.8', '4.8', '5.8', '6.8', '7.8', '8.8', '9.8',
            '-0.8', '-1.8', '-2.8', '-3.8', '-4.8', '-5.8', '-6.8', '-7.8', '-8.8', '-9.8',
        ]
        for number in numbers:
            self.assertEqual(self.input_handler.is_number(number),
                             True)

        self.assertEqual(self.input_handler.is_number('-12'),
                         True)
        self.assertEqual(self.input_handler.is_number('12'),
                         True)
        self.assertEqual(self.input_handler.is_number('-'),
                         False)
