import re

#pattern 
def tokenize(chars):               
    tokens=[]
    pattern = re.compile(r'''
        (?P<NUMBER>\d+\.\d+|\d+)
      | (?P<MINUS>-)               
      | (?P<OPERATOR>//|[+*/%]+)           
      | (?P<SPACE>\s+)              
      | (?P<MISMATCH>.)             
    ''', re.VERBOSE)

    #typed tokens
    for token in pattern.finditer(chars):
        value = token.group()                   
        kind = token.lastgroup                 
        if kind == 'SPACE':
            continue                            
        if kind == 'MISMATCH':
            raise SyntaxError("Неверный символ")
        tokens.append((value, kind))                       
    return tokens

#transforming_to_RPN
def to_RPN(tokens):
    tokens=(tokenize(tokens))
    for char in range(len(tokens)):
        if tokens[char][1] == "MINUS" and (char == 0 or tokens[char-1][1] == "OPERATOR"):           
            tokens[char] = (('-u',"UNARY_MINUS")) 

    output=[]         
    operators=Stack()

    ops={'+':1, '-':1, '*':2, '//':2, '/':2, '%':2, '-u':3}
    for token in tokens:
        value, kind = token[0], token[1]
        if kind == "NUMBER":
            output.append((value, kind))
        else:
            while operators and ops[(operators.last)]>=ops[value]:
                output.append(operators.pop())
            operators.append(value)

    while operators:
        output.append(operators.pop())   
    return output 

s='-12*3+123//-123'
print(to_RPN(s))

######Добваить унарный плюс
######Сделать operators - объектом класса, разобрать с ошибкой operators[-1] в строке 41 (недопустимо [-1] т.к. не введен нужный метод)