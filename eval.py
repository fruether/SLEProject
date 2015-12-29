__author__ = 'freddy'

from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
import sys

def main(argv):
    input = FileStream(argv[1])
    lexer = ExprLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()

if __name__ == '__main__':
    main(sys.argv)