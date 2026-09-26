import re
from src.toolkit.classes import Stack

#tokenizing
def tokenize(chars):
    tokens=[]

    #pattern
    pattern = re.compile(r'''
        (?P<NUMBER>\d+\.\d+|\d+)
      | (?P<PLUS>[+])
      | (?P<MINUS>-)   
      | (?P<OPERATOR>//|[*/%])
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
            if '.' in value:
                raise ValueError("Float type is incorrect")
            raise ValueError("Incorrect character")
        tokens.append((value, kind))
    return tokens

#transforming_to_RPN
def shunting_yard(tokens):
    tokens=tokenize(tokens)
    for char in range(len(tokens)):
        if (tokens[char][1] == "MINUS" or tokens[char][1] == "PLUS") and \
            (char == 0 or tokens[char-1][1] != "NUMBER"):
            tokens[char] = (('-u',"UNARY_MINUS")) if tokens[char][1] == "MINUS" \
                else (('+u', "UNARY_PLUS"))

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

# s='5+.3'
# print(tokenize(s))


