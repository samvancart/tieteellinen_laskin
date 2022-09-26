import rpn


class Calculator:
    """Class for calculating mathematical expressions given in Reverse Polish Notation."""

    def __init__(self):
        self
        self.rpn = rpn.Rpn()
        self.operations = {
            '+': lambda x, y: x+y,
            '-': lambda x, y: x-y,
            '*': lambda x, y: x*y,
            '/': lambda x, y: x/y,
            '^': lambda x, y: x^y 
        }


    def handle_operator(self, stack, operator):
        if len(stack) == 0:
            return None
        elif len(stack)==1:
            y = int(stack[-1])
            x = 0
            stack.pop()
        else:
            print(stack)
            y = int(stack[-1])
            stack.pop()
            x = int(stack[-1])
            stack.pop()
        result = self.operations[operator](x,y)
        stack.append(str(result))
        return stack

    def get_rpn_list(self, str_input):
        return self.rpn.get_reverse_polish(str_input)

    def calculate(self, str_input):
        rpn_list = self.get_rpn_list(str_input)
        stack = []
        numbers = self.rpn.get_numbers()
        operators = self.rpn.get_operators()
        functions = self.rpn.get_functions()

        for token in rpn_list:
            if self.rpn.is_number(token):
                stack.append(token)
            elif token in operators:
                stack = self.handle_operator(stack, token)
        

        return stack[0]
