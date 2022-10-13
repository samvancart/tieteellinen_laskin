from services.input_handler import InputHandler


class Rpn:
    """Class to transform a mathematical expression into Reverse Polish Notation."""

    def __init__(self):
        self.operators = ['+', '-', '*', '/', '^']
        self.precedences = [1, 1, 2, 2, 3]
        self.associativities = [0, 0, 0, 0, 1]

        self.operators_dict = [{'value': z[0], 'precedence':z[1], 'associativity':z[2]}
                               for z in zip(self.operators, self.precedences, self.associativities)]

        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'pi',
                        '-0', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9', '-pi']
        self.functions = ['sin', 'cos', 'tan', 'sqrt', 'min', 'max', '-sin',
                          '-cos', '-tan', '-sqrt', '-min', '-max']

        self.input_handler = InputHandler()

    def get_numbers(self):
        return self.numbers

    def get_operators(self):
        return self.operators

    def get_functions(self):
        return self.functions

    def get_operators_dict(self):
        return self.operators_dict

    def gen_to_dict(self, gen):
        dictionary = {}
        for dict_object in gen:
            dictionary = dict_object
        return dictionary

    def get_top_of_stack(self, stack):
        if len(stack) == 0:
            return {}
        return stack[len(stack)-1]

    def get_reverse_polish(self, str_input):
        """Validates input, calls method to transform string to list and calls shunting_yard method.

        Args:
            str_input: The input string.

        Returns: List, return value of shunting_yard method or None if validations fail.
        """
        if not self.input_handler.validate_input(self.input_handler.get_regex_list(), str_input):
            return None
        input_list = self.input_handler.str_input_to_list(str_input)
        return self.shunting_yard(input_list)

    def shunting_yard(self, input_list):
        """Main method to transform input list into reverse polish notation.

        Args:
            str_input: List, the mathematical expression.

        Returns:
            List, the mathematical expression in Reverse Polish Notation,
            [error] if there are errors.

        """
        output_stack = []
        operator_stack = []
        for token in input_list:
            top_of_stack = self.get_top_of_stack(operator_stack)
            if self.input_handler.is_number(token):
                output_stack.append(token)
            elif token in self.functions:
                operator_stack.append(
                    {'value': token, 'precedence': -1, 'associativity': 0})
            elif token in self.operators:
                self.handle_operator(token, output_stack, operator_stack)
            elif token == '(':
                operator_stack.append(
                    {'value': '(', 'precedence': 0, 'associativity': 0})
            elif token == ')':
                output_stack = self.handle_closing_bracket(
                    output_stack, operator_stack, top_of_stack)

        if 'error' in output_stack:
            return ['error']
        while len(operator_stack) > 0:
            top_of_stack = self.get_top_of_stack(operator_stack)
            if top_of_stack['value'] == '(':
                return ['error']
            output_stack.append(top_of_stack['value'])
            operator_stack.pop()

        return output_stack

    def handle_operator(self, operator, output_stack, operator_stack):
        """Helper method that handles the str_input token when it is an operator (+,-,*, etc).

        Args:
            operator: The operator to be handled.
            output_stack: The output_stack in its current state.
            operator_stack: The operator_stack in its current state.

            Returns:
                New operator_stack state if operator_stack was empty,
                else top of the operator_stack.
        """
        operator_gen = (
            o for o in self.operators_dict if o['value'] == operator)
        operator_dict = self.gen_to_dict(operator_gen)
        if len(operator_stack) == 0:
            operator_stack.append(operator_dict)
            top_of_stack = self.get_top_of_stack(operator_stack)
            return operator_stack

        top_of_stack = self.get_top_of_stack(operator_stack)
        while top_of_stack and top_of_stack['value'] != '(' \
            and (top_of_stack['precedence'] > operator_dict['precedence']
                 or (top_of_stack['precedence'] == operator_dict['precedence']
                     and operator_dict['associativity'] == 0)):
            output_stack.append(top_of_stack['value'])
            operator_stack.pop()
            top_of_stack = self.get_top_of_stack(operator_stack)
        operator_stack.append(operator_dict)

        return top_of_stack

    def handle_closing_bracket(self, output_stack, operator_stack, top_of_stack):
        """Helper method that handles the str_input token when it is a closing bracket.

        Args:
            output_stack: The output_stack in its current state.
            operator_stack: The operator_stack in its current state.
            top_of_stack: First item in operator stack.

            Returns:
                List, new state of output_stack.
        """
        while top_of_stack and top_of_stack['value'] != '(':
            output_stack.append(top_of_stack['value'])
            operator_stack.pop()
            top_of_stack = self.get_top_of_stack(operator_stack)
        if not top_of_stack or not top_of_stack['value'] == '(':
            output_stack = ['error']
            return output_stack
        operator_stack.pop()
        if operator_stack:
            top_of_stack = self.get_top_of_stack(operator_stack)
            if top_of_stack['value'] in self.functions:
                output_stack.append(top_of_stack['value'])
                operator_stack.pop()

        return output_stack
