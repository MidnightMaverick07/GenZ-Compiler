from tokenizer import tokenize
from parser import parse
from interpreter import execute

with open("example.genz") as f:
    code = f.read()

tokens = tokenize(code)
ast = parse(tokens)
execute(ast)