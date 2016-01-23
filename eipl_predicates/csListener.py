# Generated from cs.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .csParser import csParser
else:
    from csParser import csParser

from libs import facts, semantic, variables

semantic.init()
semantic.add_scope("main")
variables.nameList = []
variables.staticOpt = None


# This class defines a complete listener for a parse tree produced by csParser.
class csListener(ParseTreeListener):

    # Enter a parse tree produced by csParser#scope.
    def enterScope(self, ctx:csParser.ScopeContext):
        pass

    # Exit a parse tree produced by csParser#scope.
    def exitScope(self, ctx:csParser.ScopeContext):
        pass


    # Enter a parse tree produced by csParser#r_decl.
    def enterR_decl(self, ctx:csParser.R_declContext):
        pass

    # Exit a parse tree produced by csParser#r_decl.
    def exitR_decl(self, ctx:csParser.R_declContext):
        pass


    # Enter a parse tree produced by csParser#r_stmt.
    def enterR_stmt(self, ctx:csParser.R_stmtContext):
        pass

    # Exit a parse tree produced by csParser#r_stmt.
    def exitR_stmt(self, ctx:csParser.R_stmtContext):
        pass


    # Enter a parse tree produced by csParser#block.
    def enterBlock(self, ctx:csParser.BlockContext):
        pass

    # Exit a parse tree produced by csParser#block.
    def exitBlock(self, ctx:csParser.BlockContext):
        pass


    # Enter a parse tree produced by csParser#expr.
    def enterExpr(self, ctx:csParser.ExprContext):
        pass

    # Exit a parse tree produced by csParser#expr.
    def exitExpr(self, ctx:csParser.ExprContext):
        pass


    # Enter a parse tree produced by csParser#aexpr.
    def enterAexpr(self, ctx:csParser.AexprContext):
        pass

    # Exit a parse tree produced by csParser#aexpr.
    def exitAexpr(self, ctx:csParser.AexprContext):
        pass


    # Enter a parse tree produced by csParser#term.
    def enterTerm(self, ctx:csParser.TermContext):
        pass

    # Exit a parse tree produced by csParser#term.
    def exitTerm(self, ctx:csParser.TermContext):
        pass


    # Enter a parse tree produced by csParser#factor.
    def enterFactor(self, ctx:csParser.FactorContext):
        pass

    # Exit a parse tree produced by csParser#factor.
    def exitFactor(self, ctx:csParser.FactorContext):
        pass


    # Enter a parse tree produced by csParser#r_type.
    def enterR_type(self, ctx:csParser.R_typeContext):
        pass

    # Exit a parse tree produced by csParser#r_type.
    def exitR_type(self, ctx:csParser.R_typeContext):
        pass


    # Enter a parse tree produced by csParser#name.
    def enterName(self, ctx:csParser.NameContext):
        pass

    # Exit a parse tree produced by csParser#name.
    def exitName(self, ctx:csParser.NameContext):
        pass


    # Enter a parse tree produced by csParser#static.
    def enterStatic(self, ctx:csParser.StaticContext):
        pass

    # Exit a parse tree produced by csParser#static.
    def exitStatic(self, ctx:csParser.StaticContext):
        pass


