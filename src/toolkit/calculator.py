from tokenizer import rpn

if __name__=="__main__":
    s='123+3//345+5-3.4'
    print(rpn(s))