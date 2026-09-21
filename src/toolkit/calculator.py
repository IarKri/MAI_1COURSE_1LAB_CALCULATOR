from tokenizer import to_RPN

def calculator(chars):
    tokens = to_RPN(chars)
    output=[]
    for token in tokens:
        value, kind = token[0], token[1]
        if kind=="NUMBER":
            output.append(value)
        elif kind=="UNARY_MINUS":
            number_1=float(output.pop())
            output.append(number_1*(-1))
        else:
            number_2=float(output.pop())
            number_1=float(output.pop())
            if value == '+':
                output.append(number_1+number_2)
            if value == '-':
                output.append(number_1-number_2)
            if value == '*':
                output.append(number_1*number_2)
            if value == '/':
                output.append(number_1/number_2)
            if value == '//':
                output.append(number_1//number_2)
            if value == '%':
                output.append(number_1%number_2)
    return output

s='-12*3+123//-123'
print(calculator(s))