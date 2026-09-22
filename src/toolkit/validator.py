from toolkit.tokenizer import tokenize

def space_cleaning(chars):
    while ' ' in chars:
        chars=chars.replace(' ', '')
    return chars

#double_minus\plus
def minusminus_plusplus(chars):
    while ' ' in chars:
        chars=chars.replace(' ', '')
    while '--' in chars:
        chars=chars.replace('--','+')
    while '++' in chars:
        chars=chars.replace('++','+')
    return chars

#double_operator_error
def double_operator_check(chars):
    tokens=[tokens for tokens in chars.split()]
    for token in range(len(tokens)-1):
        if (tokens[token][1]!="NUMBER" and tokens[token+1]=="OPERATOR"):
            return SyntaxError("Невозможная математическая операция")
    # return tokens


# s="1*+2"
# print(double_operator(s))
##программа моежт некорректно работать с пробелами и двойным минусом/плюсом - составить алгоритм по корректной поэтапной зачистке/проверке выражения