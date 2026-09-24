from tokenizer import shunting_yard
from classes import Stack
from validator import space_cleaning


def calculator(chars):
    chars = space_cleaning(chars)
    tokens = shunting_yard(chars)

    output=Stack()
    unar_minuses=Stack()
    for token in tokens:
        value, kind = token[0], token[1]
        if kind=="NUMBER":
            while not unar_minuses.is_empty:
                value=float(value)*(-1)
            output.push(value)
        elif kind=="UNARY_MINUS":
            if output.is_empty:
                unar_minuses.push(-1)
            else:
                number_1=float(output.pop())
                output.push(number_1*(-1))

        
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
                if number_2==int(number_2) and number_1==int(number_1):
                    output.push(number_1//number_2)
                else:
                    raise ValueError("Неверный тип данных для целочисленного деления")
            if value == '%':
                if number_2==int(number_2) and number_1==int(number_1):
                    output.push(number_1%number_2)
                else:
                    raise ValueError("Неверный тип данных для вычисления остатка от деления")
    return float(output.pop())

s='123.3*4//2'
print(calculator(s))
# print(shunting_yard(s))
#if '.' not in str(number_1) and '.' not in str(number_2):
#работа нескольких идущих подряд + и -