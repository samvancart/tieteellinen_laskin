from services.rpn import Rpn
from services.input_handler import InputHandler
import math

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
            return ['error']
        if len(stack)==1:
            result = self.handle_function([stack[0]])
            return [str(float(eval(result[0])))]
        else:
            operations_y = stack[-1]
            stack.pop()
            operations_x = stack[-1]
            stack.pop()
        try:
            operations_x, operations_y = self.handle_function([operations_x, operations_y])
            result = self.operations[operator](float(operations_x),float(operations_y))
            stack.append(str(result))
        except:
            stack.append('error')
        return stack

    def get_rpn_list(self, str_input):
        if not str_input:
            return None
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
        elif len(stack) == 1:
            stack = self.handle_operator(stack, rpn_list[0])
        return stack[0]

    def handle_function(self, item_list):
        items=[]
        for item in item_list:
            if item in ('pi','-pi'):
                as_string = item[0:-2]+'math.pi'
                as_number = eval(as_string)
                items.append(str(as_number))
            else:
                items.append(item)
        return items