from rpn import Rpn
from calculator import Calculator
def main():
    calculator = Calculator()
    input = '3+4*2/(1-5)^2^3'
    input1 = '((1)*2)'
    input3 = 'sin(max(2,3)/3*pi)'
    input4 = '(3+4)'
    input5 = '3+4*2'
    input2 = '++3--+4'
    list_input1 = ['3','+','4']
    my_rpn = Rpn()
    # print(my_rpn.str_input_to_list(input2))
    # print(my_rpn.get_reverse_polish(input4))
    print(my_rpn.get_reverse_polish(input5))
    print(calculator.calculate(input5))
if __name__ == "__main__":
    main()