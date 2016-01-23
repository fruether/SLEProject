__author__ = 'freddy'

from csListener import csListener
from libs import semantic
from libs import facts
class FactExtractionListener(csListener):

    def enterR_decl(self, ctx):
        if ctx.block() is not None:
            routine_name = ctx.NAME()[0].getText()
            semantic.add_scope(routine_name)
        else:
            variables =  semantic.unwrapLexims(ctx.NAME())
            facts.if_not_empty(ctx.STATIC(), [("static",variables)])
            facts.create_fact("typeOf", ctx.r_type().getText() , variables)

    def exitR_delc(self, ctx):
        if ctx.block() is not None:
            semantic.remove_scope()

    def enterR_stmt(self, ctx):
        text = ctx.getText()
        if text[0:4] == "call":
            name = str(ctx.NAME())
            facts.create_fact("callTo", semantic.get_current_scope(),  name)
