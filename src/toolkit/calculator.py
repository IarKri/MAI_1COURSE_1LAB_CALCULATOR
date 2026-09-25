from src.toolkit.tokenizer import shunting_yard
from src.toolkit.classes import Stack
from src.toolkit.validator import space_cleaning
from src.toolkit.validator import initial_calculator_validation


def calculator(chars):
    chars = space_cleaning(chars)
    tokens = shunting_yard(chars)


    output=Stack()
    unar_minuses=Stack()
    for token in tokens:
        value, kind = token[0], token[1]
        if kind=="NUMBER":
            if not unar_minuses.is_empty():
                while not unar_minuses.is_empty():
                    unar_minuses.pop()
                    value=-float(value)
                output.push(value)
            else:
                output.push(value)
        elif kind=="UNARY_MINUS":
            if not output.is_empty():
                number_1=-float(output.pop())
                output.push(number_1)
            else:
                unar_minuses.push(-1)
        elif kind=="UNARY_PLUS":
            pass
        else:
            number_2=float(output.pop())
            number_1=float(output.pop())
            if value == '+':
                output.push(number_1+number_2)
            if value == '-':
                output.push(number_1-number_2)
            if value == '*':
                output.push(number_1*number_2)
            if value == '/':
                output.push(number_1/number_2)
            if value == '//':
                if number_2.is_integer() and number_1.is_integer():
                    output.push(number_1//number_2)
                else:
                    raise ValueError("Incorrect value for operation with //")
            if value == '%':
                if number_2.is_integer() and number_1.is_integer():
                    output.push(number_1%number_2)
                else:
                    raise ValueError("Incorrect value for operation wittn %")
    return float(output.pop())

# s='--++  12.0//3+-+--+4//2'
# print(space_cleaning(s))