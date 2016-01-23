__author__ = 'freddy'

from csVisitor import csVisitor
from libs import semantic, facts
from antlr4.tree.Tree import TerminalNodeImpl
class FactExtractionVisitor(csVisitor):

    def __init__(self):
        semantic.add_scope("main")

    def visitR_decl(self, ctx):
        if ctx.block() is not None:
            funcName = ctx.NAME()[0].getText()
            semantic.add_scope(funcName)

            self.walkContext(ctx)
            semantic.remove_scope()
        else:
            variables = semantic.unwraplexims(ctx.NAME())
            facts.if_not_empty(ctx.STATIC(), [("static", variables)])
            facts.create_fact("typeOf", ctx.r_type().getText() , variables)

    def visitR_stmt(self, ctx):
        expression = ctx.getText()
        if expression.startswith("call"):
            funcCall = ctx.NAME().getText()
            facts.create_fact("CallTo", semantic.get_current_scope(), funcCall)
        self.walkContext(ctx)

    def walkContext(self, context):
        for x in context.getChildren():
            if not isinstance(x, TerminalNodeImpl):
                super(FactExtractionVisitor, self).visit(x)