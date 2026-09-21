from tokenizer import tokenize

#double_minus\plus
def minusminus_plusplus(chars):
    while '--' in chars:
        chars=chars.replace('--','+')
    while '++' in chars:
        chars=chars.replace('++','+')
    return chars

#double_operator_error
def double_operator(chars):
    tokens=tokenize(chars)
    for token in range(len(tokens)):
        if (tokens[token][1]!="NUMBER" and tokens[token+1]=="OPERATOR") or (tokens[token][1]=="OPERATOR" and tokens[token+1]!="NUMBER"):
            return SyntaxError("Невозможная математическая операция")



s="1+*2"
print(double_operator(s))