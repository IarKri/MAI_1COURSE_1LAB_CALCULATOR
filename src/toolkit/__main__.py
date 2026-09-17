
from tokenizer import tokenize

if __name__==__main__:
    s='-1/0+2.34//-567*203.67+-+-' 
    print(tokenize.tokenize(s))