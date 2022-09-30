from services.rpn import Rpn
from services.input_handler import InputHandler


class Calculator:
    """Class for calculating mathematical expressions given in Reverse Polish Notation."""

    def __init__(self):
        self.rpn = Rpn()
        self.input_handler = InputHandler()
        self.operations = {
            '+': lambda x, y: x+y,
            '-': lambda x, y: x-y,
            '*': lambda x, y: x*y,
            '/': lambda x, y: x/y,
            '^': lambda x, y: x**y
        }


    def handle_operator(self, stack, operator):
        if len(stack) == 0:
            return None
        if len(stack)==1:
            operations_y = float(stack[-1])
            operations_x = 0
            stack.pop()
        else:
            operations_y = float(stack[-1])
            stack.pop()
            operations_x = float(stack[-1])
            stack.pop()
        try:
            result = self.operations[operator](operations_x,operations_y)
            stack.append(str(result))
        except:
            stack.append('error')
        return stack

    def get_rpn_list(self, str_input):
        return self.rpn.get_reverse_polish(str_input)

    def calculate(self, str_input):
        rpn_list = self.get_rpn_list(str_input)
        if not rpn_list:
            return ['error']
        stack = []
        operators = self.rpn.get_operators()
        # functions = self.rpn.get_functions()

        for token in rpn_list:
            if self.input_handler.is_number(token):
                stack.append(token)
            elif token in operators:
                stack = self.handle_operator(stack, token)
        if not stack:
            return ['error']
        return stack[0]
