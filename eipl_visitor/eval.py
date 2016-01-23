__author__ = 'freddy'

from antlr4 import *
from csLexer import csLexer
from csParser import csParser
import sys
from libs import facts
from FactExtractorVisitor import FactExtractionVisitor

def main(argv):

    input = FileStream(argv[1])
    lexer = csLexer(input)
    stream = CommonTokenStream(lexer)
    parser = csParser(stream)
    tree = parser.scope()
    extractor = FactExtractionVisitor()
    extractor.visit(tree)
    facts.show()
if __name__ == '__main__':
    main(sys.argv)