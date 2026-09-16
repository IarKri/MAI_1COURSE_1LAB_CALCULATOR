import re

def tokenize(text):
    rules=[
        ("OPERATOR", r"\+"),
        ("OPERATOR", r"-"),
        ("OPERATOR", r"\*"),
        ("OPERATOR", r"/"),
        ("NUMBER", r"\d+\.?\d*"),
    ]

    tokens=[]

