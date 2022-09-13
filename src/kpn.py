class Kpn:
    def __init__(self):
        self.operators = ['+','-','*','/','^']
        self.precedences = [1,1,2,2,3]
        self.associativities = [0,0,0,0,1]

        self.operators_dict = [{'value': z[0],'precedence':z[1],'associativity':z[2]} \
            for z in zip(self.operators,self.precedences,self.associativities)]

        self.output_stack = []
        self.operator_stack = []
        self.numbers = ['0','1','2','3','4','5','6','7','9']


    def is_stack_empty(self,stack):
        return len(stack) == 0


    def gen_to_dict(self,gen):
        dict = {}
        for x in gen:
            dict = x
        return dict

    def get_top_of_stack(self,stack):
        if len(stack)==0:
            return {}
        else:
            return stack[len(stack)-1]


    def handle_operator(self,operator):
        operator_gen = (o for o in self.operators_dict if o['value'] == operator)
        operator_dict = self.gen_to_dict(operator_gen)
        if len(self.operator_stack) == 0:
            self.operator_stack.append(operator_dict)
            return

        top_of_stack = self.get_top_of_stack(self.operator_stack)

        while top_of_stack['value'] != '(' \
        and (top_of_stack['precedence'] > operator_dict['precedence'] \
        or (top_of_stack['precedence'] == operator_dict['precedence'] \
        and operator_dict['associativity'] == 0)):
            self.output_stack.append(top_of_stack['value'])
            self.operator_stack.pop()
            top_of_stack = self.get_top_of_stack(self.operator_stack)
        self.operator_stack.append(operator_dict)

        return top_of_stack

    def get_operators_dict(self):
        return self.operators_dict

    def get_reverse_polish(self, input):
        return self.shunting_yard(input)

    def shunting_yard(self,input):
        for token in input:
            top_of_stack = self.get_top_of_stack(self.operator_stack)
            if token in self.numbers:
                self.output_stack.append(token)
            elif token in self.operators:
                self.handle_operator(token)
            elif token == '(':
                self.operator_stack.append({'value':'(','precedence': 0,'associativity': 0})
            elif token == ')':
                if not self.is_stack_empty(self.operator_stack):
                    while top_of_stack['value'] != ')':
                        if self.is_stack_empty(self.operator_stack):
                            print('Error')
                            return
                        else:
                            self.output_stack.append(top_of_stack['value'])
                            self.operator_stack.pop()
                            if self.is_stack_empty(self.operator_stack):
                                print('Error')
                                return
                            else:
                                top_of_stack = self.get_top_of_stack(self.operator_stack)
                                if top_of_stack['value'] == '(':
                                    self.operator_stack.pop()
                                    break
                else:
                    print('Error')
                    return
        while len(self.operator_stack) > 0:
            top_of_stack = self.get_top_of_stack(self.operator_stack)
            self.output_stack.append(top_of_stack['value'])
            self.operator_stack.pop()

        return self.output_stack

def main():
    input = '3+4*2/(1-5)^2^3'
    my_kpn = Kpn()
    print(my_kpn.get_reverse_polish(input))
    
if __name__ == "__main__":
    main()