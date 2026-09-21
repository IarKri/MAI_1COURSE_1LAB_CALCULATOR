from tokenizer import to_RPN
from classes import Stack
from validator import minusminus_plusplus

def calculator(chars):
    tokens = minusminus_plusplus(chars)
    tokens = to_RPN(tokens)
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
    return output.pop()

s='--12*3++123//-123'
print(calculator(s))