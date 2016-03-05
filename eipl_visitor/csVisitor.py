# Generated from cs.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .csParser import csParser
else:
    from csParser import csParser

# This class defines a complete generic visitor for a parse tree produced by csParser.

class csVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by csParser#scope.
    def visitScope(self, ctx:csParser.ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by csParser#r_decl.
    def visitR_decl(self, ctx:csParser.R_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by csParser#r_stmt.
    def visitR_stmt(self, ctx:csParser.R_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by csParser#block.
    def visitBlock(self, ctx:csParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by csParser#expr.
    def visitExpr(self, ctx:csParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by csParser#aexpr.
    def visitAexpr(self, ctx:csParser.AexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by csParser#term.
    def visitTerm(self, ctx:csParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by csParser#factor.
    def visitFactor(self, ctx:csParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by csParser#r_type.
    def visitR_type(self, ctx:csParser.R_typeContext):
        return self.visitChildren(ctx)



del csParser