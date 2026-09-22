from toolkit.tokenizer import shunting_yard
from toolkit.classes import Stack
from toolkit.tokenizer import tokenize
from toolkit.validator import minusminus_plusplus

def calculator(chars):
    tokens = minusminus_plusplus(chars)
    tokens = shunting_yard(tokens)
    output=Stack()
    for token in tokens:
        value, kind = token[0], token[1]
        if kind=="NUMBER":
            output.push(value)
        elif kind=="UNARY_MINUS":
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
                output.push(number_1//number_2)
            if value == '%':
                output.push(number_1%number_2)
    return float(output.pop())

# s='-  - 12 *3++ 123//--12 + 8%4 + 0.000000001  -2.5'

# print(shunting_yard(s))