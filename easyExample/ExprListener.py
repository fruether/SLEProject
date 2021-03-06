# Generated from Expr.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprParser#decl.
    def enterDecl(self, ctx:ExprParser.DeclContext):
        pass

    # Exit a parse tree produced by ExprParser#decl.
    def exitDecl(self, ctx:ExprParser.DeclContext):
        pass


    # Enter a parse tree produced by ExprParser#identifier.
    def enterIdentifier(self, ctx:ExprParser.IdentifierContext):
        pass

    # Exit a parse tree produced by ExprParser#identifier.
    def exitIdentifier(self, ctx:ExprParser.IdentifierContext):
        pass


