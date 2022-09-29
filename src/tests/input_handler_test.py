import unittest
from input_handler import Input_handler


class TestInput_handler(unittest.TestCase):
        def setUp(self):
                self.input_handler = Input_handler()


        def test_str_input_to_list(self):
                self.assertEqual(self.input_handler.str_input_to_list('3+4'),
                                ['3', '+', '4'])
                self.assertEqual(self.input_handler.str_input_to_list('3564562+445*6+sin(40)'),
                                ['3564562', '+', '445', '*', '6', '+', 'sin', '(', '40', ')'])
                self.assertEqual(self.input_handler.str_input_to_list('++3--+4'),
                                ['3', '+', '4'])
                self.assertEqual(self.input_handler.str_input_to_list('+--++3+(---++4)'),
                                ['3', '+', '(','-4',')'])          
                self.assertEqual(self.input_handler.str_input_to_list('(3+(4))'),
                                ['(', '3', '+', '(', '4', ')', ')'])
                self.assertEqual(self.input_handler.str_input_to_list('20*30'),
                                ['20', '*', '30'])
                self.assertEqual(self.input_handler.str_input_to_list('3-(-12)'),
                                ['3', '-', '(', '-12', ')'])
        def test_is_number(self):
                self.assertEqual(self.input_handler.is_number('-12'),
                                True)
                self.assertEqual(self.input_handler.is_number('12'),
                                True)
                self.assertEqual(self.input_handler.is_number('-'),
                                False)