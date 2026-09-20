import re

def tokenize(chars):                #вводим токенизатор
    tokens=[]
    pattern = re.compile(r'''
        (?P<NUMBER>[+\-]?\d+\.\d+|[+\-]?\d+)        
      | (?P<OPERATOR>//|[+\-*/%]+)           
      | (?P<SPACE>\s+)              
      | (?P<MISMATCH>.)             #чтобы поднять ошибку для неверных символов	
    ''', re.VERBOSE)
    for token in pattern.finditer(chars):
            value = token.group()                   
            type = token.lastgroup                  #типизация токена
            if type == 'SPACE':
                continue                            #переход к следующей итерации
            if type == 'MISMATCH':
                raise SyntaxError("Неверный символ")
            tokens.append((value, type))                 # кортеж        
    return tokens

def rpn(chars):
    output=[]
    operators=[]
    ops={'+': 1, '-': 1, '*': 2, '//': 2, '/': 2, '%': 2}
    for token in tokenize(chars):
        if token[1]=='NUMBER':
            output.append(token[0])
        else:
            while len(operators) and ops[operators[-1]] >= ops[token[0]]:
                output.append(operators.pop())
            operators.append(token[0])
    while operators:
        output.append(operators.pop())   
    return output            

    # return output

s='-12*123//3.14-52'
print(rpn(s))
