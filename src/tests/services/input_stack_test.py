from services.input_stack import InputStack
import unittest
from services.input_stack import InputStack


class TestInputStack(unittest.TestCase):
    def setUp(self):
        self.input_stack = InputStack()

    def test_get_input_stack(self):
        self.input_stack.add_to_input_stack('3')
        self.assertEqual(self.input_stack.get_input_stack(),
                         ['3'])
        self.input_stack.clear_input_stack()
        self.assertEqual(self.input_stack.get_input_stack(),
                         [])

    def test_get_input_stack_as_str(self):
        # Append to stack.
        self.input_stack.add_to_input_stack('3')
        self.input_stack.add_to_input_stack('+')
        self.input_stack.add_to_input_stack('4')
        self.assertEqual(self.input_stack.get_input_stack_as_str(),
                         '3+4')
        # Delete from stack and stack is not empty.
        self.input_stack.delete_from_input_stack()
        self.input_stack.delete_from_input_stack()
        self.assertEqual(self.input_stack.get_input_stack_as_str(),
                         '3')
        self.input_stack.add_to_input_stack('*')
        # Append function.
        self.input_stack.add_to_input_stack('sin')
        self.assertEqual(self.input_stack.get_input_stack_as_str(),
                         '3*sin(')
        self.input_stack.add_to_input_stack('5')
        self.input_stack.add_to_input_stack(')')
        self.assertEqual(self.input_stack.get_input_stack_as_str(),
                         '3*sin(5)')
        # Clear stack.
        self.input_stack.clear_input_stack()
        self.assertEqual(self.input_stack.get_input_stack_as_str(),
                         '')
        # Append var.
        self.input_stack.handle_var()
        self.assertEqual(self.input_stack.get_input_stack_as_str(),
                         'var=')
        self.input_stack.clear_input_stack()
        # Value other than type(str).
        self.input_stack.add_to_input_stack(['error'])
        self.assertEqual(self.input_stack.get_input_stack_as_str(),
                         'error')
        self.input_stack.clear_input_stack()
        self.input_stack.add_to_input_stack(None)
        self.assertEqual(self.input_stack.get_input_stack_as_str(),
                         'error')
        # Delete from empty stack.
        self.input_stack.delete_from_input_stack()
        self.input_stack.delete_from_input_stack()
        self.assertEqual(self.input_stack.get_input_stack_as_str(),
                         '')
