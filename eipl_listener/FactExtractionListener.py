__author__ = 'freddy'

from csListener import csListener
from libs import semantic
from libs import facts
class FactExtractionListener(csListener):
     # Enter a parse tree produced by csParser#scope.
    def enterR_decl(self, ctx):
        if ctx.block() is not None:

            routine_name = ctx.name().NAME().getText()
            semantic.add_scope(routine_name)

    def exitR_delc(self, ctx):
        if ctx.block() is not None:
            semantic.remove_scope()

    def enterR_stmt(self, ctx):
        text = ctx.getText()
        if text[0:4] == "call":
            name = str(ctx.NAME())
            facts.create_fact("callTo", semantic.get_current_scope(),  name)