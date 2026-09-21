import re
from classes import Stack

#tokenizing 
def tokenize(chars):               
    tokens=[]

    #pattern
    pattern = re.compile(r'''
        (?P<NUMBER>\d+\.\d+|\d+)
      | (?P<PLUS>[+])
      | (?P<MINUS>-)               
      | (?P<OPERATOR>//|[*/%]+)           
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
        if (tokens[char][1] == "MINUS" or tokens[char][1] == "PLUS") and (char == 0 or tokens[char-1][1] != "NUMBER"):           
            tokens[char] = (('-u',"UNARY_MINUS")) if tokens[char][1] == "MINUS" else (('+u', "UNARY_PLUS"))
        elif (tokens[char][0] == "//" or tokens[char][0] == "%") and ('.'  in tokens[char-1][0] or '.'  in tokens[char+1][0]):
            raise Exception("Неверное значение для целочисленного деления")

    output=[]         
    operators=Stack()

    #RPN_formating
    ops={'+':1, '-':1, '*':2, '//':2, '/':2, '%':2, '-u':3, '+u':3}
    for token in tokens:
        value, kind = token[0], token[1]
        if kind == "NUMBER":
            output.append((value, kind))
        else:
            while not operators.is_empty() and ops[operators.last()[0]]>=ops[value]:
                output.append(operators.pop())
            operators.push((value, kind))

    while not operators.is_empty():
        output.append(operators.pop())   
    return output 

# s='--12*3++123//-123'
# print(to_RPN(s))

######Добваить унарный плюс - сделал
######Сделать operators - объектом класса, разобрать с ошибкой operators[-1] в строке 41 (недопустимо [-1] т.к. не введен нужный метод) - сделал
######Сделать class Stack для operators вместо 