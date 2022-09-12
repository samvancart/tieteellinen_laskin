
output_stack = []
operator_stack = []

operators = ['+','-','*','/','^']
precedences = [1,1,2,2,3]
associativities = [0,0,0,0,1]

operators_dict = [{'value': z[0],'precedence':z[1],'associativity':z[2]} \
    for z in zip(operators,precedences,associativities)]

numbers = ['0','1','2','3','4','5','6','7','9']


def is_stack_empty(stack):
    return len(stack) == 0


def gen_to_dict(gen):
    dict = {}
    for x in gen:
        dict = x
    return dict

def get_top_of_stack(stack):
    if len(stack)==0:
        return {}
    else:
        return stack[len(stack)-1]


def handle_operator(operator):
    operator_gen = (o for o in operators_dict if o['value'] == operator)
    operator_dict = gen_to_dict(operator_gen)
    if len(operator_stack) == 0:
        operator_stack.append(operator_dict)
        return

    top_of_stack = get_top_of_stack(operator_stack)

    while top_of_stack['value'] != '(' \
    and (top_of_stack['precedence'] > operator_dict['precedence'] \
    or (top_of_stack['precedence'] == operator_dict['precedence'] \
    and operator_dict['associativity'] == 0)):
        output_stack.append(top_of_stack['value'])
        operator_stack.pop()
        top_of_stack = get_top_of_stack(operator_stack)
    operator_stack.append(operator_dict)

    return top_of_stack

# handle_operator('+')
# handle_operator('*')
# handle_operator('/')
# handle_operator('^')
# handle_operator('^')

# print('output_stack: ', output_stack)
# print('operator_stack: ',operator_stack)
# print('Top now ',get_top_of_stack(operator_stack))

input_1 = '3+4*2/(1-5)^2^3'
input_2 = '3+4*2'


def shunting_yard(input):
    for token in input:
        top_of_stack = get_top_of_stack(operator_stack)
        if token in numbers:
            output_stack.append(token)
        elif token in operators:
            handle_operator(token)
        elif token == '(':
            operator_stack.append({'value':'(','precedence': 0,'associativity': 0})
        elif token == ')':
            if not is_stack_empty(operator_stack):
                while top_of_stack['value'] != ')':
                    if is_stack_empty(operator_stack):
                        print('Error')
                        return
                    else:
                        output_stack.append(top_of_stack['value'])
                        operator_stack.pop()
                        if is_stack_empty(operator_stack):
                            print('Error')
                            return
                        else:
                            top_of_stack = get_top_of_stack(operator_stack)
                            if top_of_stack['value'] == '(':
                                operator_stack.pop()
                                break
            else:
                 print('Error')
                 return
    while len(operator_stack) > 0:
        top_of_stack = get_top_of_stack(operator_stack)
        output_stack.append(top_of_stack['value'])
        operator_stack.pop()

shunting_yard(input_1)
print('output_stack: ', output_stack)
print('operator_stack: ',operator_stack)

