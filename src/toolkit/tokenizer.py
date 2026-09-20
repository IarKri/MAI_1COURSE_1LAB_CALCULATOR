import re

def tokenize(chars):               #вводим токенизатор
    tokens=[]
    pattern = re.compile(r'''
        (?P<NUMBER>\d+\.\d+|\d+)
      | (?P<MINUS>-)               
      | (?P<OPERATOR>//|[+*/%]+)           
      | (?P<SPACE>\s+)              
      | (?P<MISMATCH>.)             #чтобы поднять ошибку для неверных символов
    ''', re.VERBOSE)

    for token in pattern.finditer(chars):
        value = token.group()                   
        type = token.lastgroup                 #типизация токена
        if type == 'SPACE':
            continue                            #переход к следующей итерации
        if type == 'MISMATCH':
            raise SyntaxError("Неверный символ")
        tokens.append((value, type))                 # кортеж        
    return tokens

def rpn(tokens):
    tokens=(tokenize(tokens))
    for char in range(len(tokens)):
        if tokens[char][1] == "MINUS" and (char == 0 or tokens[char-1][1] == "OPERATOR"):
            tokens[char] = (('-u',"UNARY MINUS")) 

    output=[]
    operators=[]

    ops={'+':1, '-':1, '*':2, '//':2, '/':2, '%':2, '-u':3}
    for token in tokens:
        value, type = token[0], token[1]
        if type == "NUMBER":
            output.append(value)
        else:
            while operators and ops[operators[-1]]>=ops[value]:
                    output.append(operators.pop())
            operators.append(value)



    while operators:
        output.append(operators.pop())   
    return output 

s='-12*3+123//--123'
print(rpn(s))

