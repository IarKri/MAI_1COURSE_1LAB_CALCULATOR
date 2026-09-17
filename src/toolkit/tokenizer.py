import re

def tokenize(chars):                #вводим токенизатор
    tokens=[]
    pattern = re.compile(r'''
        (?P<NUMBER>\d+\.\d+|\d+)        
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



def rpn_tokenizer(s):
    output=[]
    operators=[]
    ops={'+': 1, '-': 1, '*': 2, '//': 2, '/': 2, '%': 2}
    for token in tokenize(s):
        if token[1] == "NUMBER":
            output.append(token[0])
        else:
            if len(operators):
                if ops[token[0]][0]<ops[operators.pop()[0]][0]:
                    output.append(token[0])
                else:
                    operators.append(token[0])
            else:
                operators.append(token[0])
    while len(operators):
        output.append(operators.pop()[0])
    return output
