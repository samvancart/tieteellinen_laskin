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
            '^': lambda x, y: x**y,
            'sqrt': lambda x, y: math.sqrt(x),
            '-sqrt': lambda x, y: math.sqrt(x)*(-1.0)
        }


    def calculate(self, str_input):
        """Evaluates the given mathematical expression.
        
        Args:
            str_input: The mathematical expression as a string.

        Returns:
            The result of the evaluation as a string.
        """
        rpn_list = self.get_rpn_list(str_input)
        # print('rpn_list', rpn_list)
        if not rpn_list:
            return ['error']
        stack = []
        operators = self.rpn.get_operators()
        functions = self.rpn.get_functions()
        last_token = ''
        for token in rpn_list:
            if self.input_handler.is_number(token):
                stack.append(token)
            elif token in operators:
                stack = self.handle_operator(stack, token)
                last_token = token
            elif token in functions:
                stack = self.handle_function(stack, token)
                last_token = token
        if not stack:
            return ['error']
        if len(stack) == 1 and last_token not in functions:
            stack = self.handle_operator(stack, rpn_list[0])
        return stack[0]

    def handle_operator(self, stack, operator):
        """Handles expression that includes an operator.

        Args:
            stack: The list of tokens to evaluate.
            operator: The operator as a string.

        Returns:
            List, the new state of the list of tokens.
        """
        if len(stack) == 0:
            return ['error']
        if len(stack) == 1:
            result = self.handle_pi([stack[0]])
            return [str(float(eval(result[0])))]
        else:
            token_y = stack[-1]
            stack.pop()
            token_x = stack[-1]
            stack.pop()
        stack = self.handle_operation(
            [token_x, token_y], operator, stack)
        return stack

    def handle_function(self, stack, function):
        """Handles expression that includes a function.

        Args:
            stack: The list of tokens to evaluate.
            function: The fuction as a string.

        Returns:
            List, the new state of the list of tokens.
        """
        if len(stack) == 0:
            return ['error']

        token_x = self.handle_pi([stack[-1]])
        stack.pop()
        stack = self.handle_operation(
            token_x, function, stack)
        return stack

    def handle_operation(self, token_list, operator, stack):
        """Handles calculation.
        
        Args:
            token_list: List of tokens to evaluate.
            operator: The operator or function as string.
            stack: The current state of the list of tokens.

        Returns:
            List, the new state of the list of tokens.
        """
        # print('operations_list', token_list)
        try:
            token_list = self.handle_pi(token_list)
            if len(token_list) == 1:
                result = self.operations[operator](float(token_list[0]), 0.0)
            else:
                result = self.operations[operator](
                    float(token_list[0]), float(token_list[1]))
            stack.append(str(result))
        except:
            stack.append('error')
        return stack


    def get_rpn_list(self, str_input):
        if not str_input:
            return None
        return self.rpn.get_reverse_polish(str_input)

    

    def handle_pi(self, item_list):
        items = []
        for item in item_list:
            if item in ('pi', '-pi'):
                as_string = item[0:-2]+'math.pi'
                as_number = eval(as_string)
                items.append(str(as_number))
            else:
                items.append(item)
        return items
