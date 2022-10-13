from services.rpn import Rpn


class InputStack:
    """Class to handle ui input."""

    def __init__(self):
        self.rpn = Rpn()
        self.input_stack = []

    def get_input_stack(self):
        return self.input_stack

    def get_input_stack_as_str(self):
        return ''.join(self.input_stack)

    def add_to_input_stack(self, value):
        if not isinstance(value, str):
            value = 'error'
        extra_token = ''
        if value in self.rpn.get_functions():
            extra_token = '('
        if value == 'var':
            extra_token = '='
        self.input_stack.append(value + extra_token)

    def clear_input_stack(self):
        self.input_stack = []

    def delete_from_input_stack(self):
        if self.input_stack:
            self.input_stack.pop()

    def handle_var(self):
        self.clear_input_stack()
        self.add_to_input_stack('var')
