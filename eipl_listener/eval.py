__author__ = 'freddy'

from antlr4 import *
from csLexer import csLexer
from csParser import csParser
import sys
from FactExtractionListener import FactExtractionListener
from libs import facts
def main(argv):

    input = FileStream(argv[1])
    lexer = csLexer(input)
    stream = CommonTokenStream(lexer)
    parser = csParser(stream)
    tree = parser.scope()
    printer = FactExtractionListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    facts.show()

if __name__ == '__main__':
    main(sys.argv)