__author__ = 'freddy'

from csListener import csListener
from libs import semantic
from libs import facts
class FactExtractionListener(csListener):

    def __init__(self):
        semantic.add_scope("main")

    def enterR_decl(self, ctx):
        if ctx.block() is not None:
            routine_name = ctx.NAME()[0].getText()
            semantic.add_scope(routine_name)
        else:
            variables = semantic.unwrapLexims(ctx.NAME())
            facts.if_not_empty(ctx.STATIC(), [("static",variables)])
            facts.create_fact("typeOf", ctx.r_type().getText() , variables)

    def exitR_decl(self, ctx):
        if ctx.block() is not None:
            semantic.remove_scope()

    def enterR_stmt(self, ctx):
        text = ctx.getText()
        if text[0:4] == "call":
            name = ctx.NAME().getText()
            facts.create_fact("callTo", semantic.get_current_scope(),  name)

    def enterBlock(self, ctx):
        statements = semantic.unwrapLexims(ctx.r_stmt())
        if (len(statements) >= 2):
            facts.create_fact("succ", facts.next(statements,[]))