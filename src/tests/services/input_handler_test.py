import unittest
from services.input_handler import InputHandler


class TestInputHandler(unittest.TestCase):
        def setUp(self):
                self.input_handler = InputHandler()


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
                self.assertEqual(self.input_handler.str_input_to_list('3.2-(-12.52)'),
                                ['3.2', '-', '(', '-12.52', ')'])
                self.assertEqual(self.input_handler.str_input_to_list('-3.2-(12.52)'),
                                ['-3.2', '-', '(', '12.52', ')'])
        def test_is_number(self):
                self.assertEqual(self.input_handler.is_number('-12'),
                                True)
                self.assertEqual(self.input_handler.is_number('12'),
                                True)
                self.assertEqual(self.input_handler.is_number('-'),
                                False)