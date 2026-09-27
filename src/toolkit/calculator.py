from src.toolkit.tokenizer import shunting_yard
from src.toolkit.classes import Stack



def calculation(chars):
    tokens = shunting_yard(chars)
    output=Stack()
    unar_minuses=Stack()
    for token in tokens:
        value, kind = token[0], token[1]
        if kind=="NUMBER":
            if not unar_minuses.is_empty():
                while not unar_minuses.is_empty():
                    unar_minuses.pop()
                    if value.isdigit():
                        value=-int(value)
                    else:
                        value=-float(value)
                output.push(value)
            else:
                if value.isdigit():
                    value=int(value)
                else:
                    value=float(value)
                output.push(value)
        elif kind=="UNARY_MINUS":
            if not output.is_empty():
                number_1=-(output.pop())
                output.push(number_1)
            else:
                unar_minuses.push(-1)
        elif kind=="UNARY_PLUS":
            pass
        else:
            number_2=output.pop()
            number_1=output.pop()
            if value == '+':
                output.push(number_1+number_2)
            if value == '-':
                output.push(number_1-number_2)
            if value == '*':
                output.push(number_1*number_2)
            if value == '/':
                output.push(number_1/number_2)
            if value == '//':
                if isinstance(number_2, int) and isinstance(number_1, int):
                    output.push(number_1//number_2)
                else:
                    raise ValueError("Incorrect ope")
            if value == '%':
                if isinstance(number_2, int) and isinstance(number_1, int):
                    output.push(number_1%number_2)
                else:
                    raise ValueError("Incorrect value for operation wittn %")
    return float(output.pop())

# s='--++  12.0//3+-+--+4//2'
# print(space_cleaning(s))