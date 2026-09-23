from tokenizer import tokenize

def space_cleaning(chars):
    for char in chars:
        if char == ' ':
            chars=chars.replace(char, '')
    return chars
#double_minus\plus
def minusminus_plusplus(chars):
    while '--' in chars:
        chars=chars.replace('--','+')
    while '++' in chars:
        chars=chars.replace('++','+')
    return chars

#double_operator_error
def post_validation_operators(chars):
    for token in range(len(chars)-1):
        return (chars[token][1]!="NUMBER" and chars[token+1]=="OPERATOR")
    # return tokens
def initial_validation_operators(chars):
    
    for token in range(len(chars)-2):
        return (chars[token]!="NUMBER" and chars[token+1]!="NUMBER" and chars[token+2]!="NUMBER")

# s="1*+2"
# print(double_operator(s))
##программа моежт некорректно работать с пробелами и двойным минусом/плюсом - составить алгоритм по корректной поэтапной зачистке/проверке выражения


