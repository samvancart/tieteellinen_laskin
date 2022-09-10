output_stack = []
operator_stack = []

operators = ['+','-','*','/','^','(',')']
precedences = [1,1,2,2,3,0,0]
associativities = [0,0,0,0,1,0,0]

operator_dict = [{'value': z[0],'precedence':z[1],'associativity':z[2]} for z in zip(operators,precedences,associativities)]

numbers = ['0','1','2','3','4','5','6','7','9']


# token = '/'
# operator = (o for o in operator_dict if o['value'] == token)
# operator = (v for v in operator_dict)
# o = {}
# for x in operator:
#     o = x
# print(operator)
# print(o)

def gen_to_dict(gen):
    dict = {}
    for x in gen:
        dict = x
    return dict

# operator_stack.append(operator_dict[2])
# if not '(' in operator_stack[0]['value']:
#     print('NO: ',operator_stack)
# else:
#     print('YES: ', operator_stack)
operator_stack.append({'value':'-','precedence': 1,'associativity': 0})
operator_stack.append({'value':'+','precedence': 1,'associativity': 0})

while not operator_stack[len(operator_stack)-1]['value'] == '(':
    print('no')
    operator_stack.pop()
    if len(operator_stack)==0:
        break
else:
    print(operator_stack)
    print('yes')

input_1 = '3+4×2÷(1−5)^2^3'


# def shunting_yard(input):
#     for token in input:
#         if token in numbers:
#             output_stack.append(token)
#         elif token in operators:
#             operator_gen = (o for o in operator_dict if o['value'] == token)
#             operator_dict = gen_to_dict(operator_gen)
#             while not '(' in operator_stack[0]['value'] \
#             and (operator_stack[0]['precedence'] > operator_dict['precedence'] \
#             or (operator_stack[0]['precedence'] == operator_dict['precedence'] \
#             and operator_dict['associativity'] == 0)):
#                 output_stack.append(operator_stack[0]['value'])
#                 operator_stack.pop()
#                 operator_stack.append(operator_dict)
#         elif token == '(':
#             operator_stack.append({'value':'(','precedence': 0,'associativity': 0})
#         elif token == ')':
#             while not operator_stack[0]['(']:
#                 if operator_stack[0] == None:


# shunting_yard(input_1)
