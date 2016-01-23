# Generated from cs.g4 by ANTLR 4.5.1
# encoding: utf-8
from antlr4 import *
from io import StringIO


from libs import facts, semantic, variables

semantic.init()
semantic.add_scope("main")
variables.nameList = []
variables.staticOpt = None

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\35")
        buf.write("\u0092\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\7\2")
        buf.write("\33\n\2\f\2\16\2\36\13\2\3\2\3\2\3\2\3\3\5\3$\n\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\7\3+\n\3\f\3\16\3.\13\3\3\3\3\3\3\3\5")
        buf.write("\3\63\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\5\3@\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4O\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4a\n\4\3\5\3\5\7\5e\n\5")
        buf.write("\f\5\16\5h\13\5\3\5\3\5\3\6\3\6\3\6\5\6o\n\6\3\7\3\7\3")
        buf.write("\7\5\7t\n\7\3\7\3\7\3\7\5\7y\n\7\5\7{\n\7\3\b\3\b\3\b")
        buf.write("\5\b\u0080\n\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0088\n\t\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\2\2\r\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\2\2\u009b\2\30\3\2\2\2\4?\3\2\2\2\6")
        buf.write("`\3\2\2\2\bb\3\2\2\2\nk\3\2\2\2\fz\3\2\2\2\16|\3\2\2\2")
        buf.write("\20\u0087\3\2\2\2\22\u0089\3\2\2\2\24\u008b\3\2\2\2\26")
        buf.write("\u008e\3\2\2\2\30\34\7\3\2\2\31\33\5\4\3\2\32\31\3\2\2")
        buf.write("\2\33\36\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35\37\3\2")
        buf.write("\2\2\36\34\3\2\2\2\37 \5\6\4\2 !\7\4\2\2!\3\3\2\2\2\"")
        buf.write("$\5\26\f\2#\"\3\2\2\2#$\3\2\2\2$%\3\2\2\2%&\7\32\2\2&")
        buf.write(",\5\22\n\2\'(\5\24\13\2()\7\5\2\2)+\3\2\2\2*\'\3\2\2\2")
        buf.write("+.\3\2\2\2,*\3\2\2\2,-\3\2\2\2-/\3\2\2\2.,\3\2\2\2/\62")
        buf.write("\5\24\13\2\60\61\7\6\2\2\61\63\5\n\6\2\62\60\3\2\2\2\62")
        buf.write("\63\3\2\2\2\63\64\3\2\2\2\64\65\7\7\2\2\65\66\b\3\1\2")
        buf.write("\66\67\b\3\1\2\678\b\3\1\28@\3\2\2\29:\7\b\2\2:;\7\34")
        buf.write("\2\2;<\b\3\1\2<=\5\b\5\2=>\b\3\1\2>@\3\2\2\2?#\3\2\2\2")
        buf.write("?9\3\2\2\2@\5\3\2\2\2Aa\7\7\2\2BC\7\34\2\2CD\7\6\2\2D")
        buf.write("E\5\n\6\2EF\7\7\2\2Fa\3\2\2\2GH\7\t\2\2HI\7\n\2\2IJ\5")
        buf.write("\n\6\2JK\7\13\2\2KN\5\6\4\2LM\7\f\2\2MO\5\6\4\2NL\3\2")
        buf.write("\2\2NO\3\2\2\2Oa\3\2\2\2PQ\7\r\2\2QR\7\n\2\2RS\5\n\6\2")
        buf.write("ST\7\13\2\2TU\5\6\4\2Ua\3\2\2\2Va\5\2\2\2WX\7\16\2\2X")
        buf.write("Y\7\34\2\2YZ\7\7\2\2Za\b\4\1\2[\\\7\17\2\2\\]\5\n\6\2")
        buf.write("]^\7\7\2\2^a\3\2\2\2_a\5\b\5\2`A\3\2\2\2`B\3\2\2\2`G\3")
        buf.write("\2\2\2`P\3\2\2\2`V\3\2\2\2`W\3\2\2\2`[\3\2\2\2`_\3\2\2")
        buf.write("\2a\7\3\2\2\2bf\7\20\2\2ce\5\6\4\2dc\3\2\2\2eh\3\2\2\2")
        buf.write("fd\3\2\2\2fg\3\2\2\2gi\3\2\2\2hf\3\2\2\2ij\7\21\2\2j\t")
        buf.write("\3\2\2\2kn\5\f\7\2lm\7\22\2\2mo\5\n\6\2nl\3\2\2\2no\3")
        buf.write("\2\2\2o\13\3\2\2\2ps\5\16\b\2qr\7\23\2\2rt\5\f\7\2sq\3")
        buf.write("\2\2\2st\3\2\2\2t{\3\2\2\2ux\5\16\b\2vw\7\24\2\2wy\5\f")
        buf.write("\7\2xv\3\2\2\2xy\3\2\2\2y{\3\2\2\2zp\3\2\2\2zu\3\2\2\2")
        buf.write("{\r\3\2\2\2|\177\5\20\t\2}~\7\25\2\2~\u0080\5\16\b\2\177")
        buf.write("}\3\2\2\2\177\u0080\3\2\2\2\u0080\17\3\2\2\2\u0081\u0088")
        buf.write("\7\33\2\2\u0082\u0088\7\34\2\2\u0083\u0084\7\n\2\2\u0084")
        buf.write("\u0085\5\n\6\2\u0085\u0086\7\13\2\2\u0086\u0088\3\2\2")
        buf.write("\2\u0087\u0081\3\2\2\2\u0087\u0082\3\2\2\2\u0087\u0083")
        buf.write("\3\2\2\2\u0088\21\3\2\2\2\u0089\u008a\7\27\2\2\u008a\23")
        buf.write("\3\2\2\2\u008b\u008c\7\34\2\2\u008c\u008d\b\13\1\2\u008d")
        buf.write("\25\3\2\2\2\u008e\u008f\7\31\2\2\u008f\u0090\b\f\1\2\u0090")
        buf.write("\27\3\2\2\2\20\34#,\62?N`fnsxz\177\u0087")
        return buf.getvalue()


class csParser ( Parser ):

    grammarFileName = "cs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'begin'", "'end'", "','", "'='", "';'", 
                     "'proc'", "'if'", "'('", "')'", "'else'", "'while'", 
                     "'call'", "'write'", "'{'", "'}'", "'>='", "'+'", "'-'", 
                     "'*'", "'bool'", "'int'", "'char'", "'static'", "'var'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BOOLEAN", "INTEGER", "CHAR", "STATIC", "VAR", "INT", 
                      "NAME", "WS" ]

    RULE_scope = 0
    RULE_r_decl = 1
    RULE_r_stmt = 2
    RULE_block = 3
    RULE_expr = 4
    RULE_aexpr = 5
    RULE_term = 6
    RULE_factor = 7
    RULE_r_type = 8
    RULE_name = 9
    RULE_static = 10

    ruleNames =  [ "scope", "r_decl", "r_stmt", "block", "expr", "aexpr", 
                   "term", "factor", "r_type", "name", "static" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    BOOLEAN=20
    INTEGER=21
    CHAR=22
    STATIC=23
    VAR=24
    INT=25
    NAME=26
    WS=27

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ScopeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def r_stmt(self):
            return self.getTypedRuleContext(csParser.R_stmtContext,0)


        def r_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(csParser.R_declContext)
            else:
                return self.getTypedRuleContext(csParser.R_declContext,i)


        def getRuleIndex(self):
            return csParser.RULE_scope

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScope" ):
                listener.enterScope(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScope" ):
                listener.exitScope(self)




    def scope(self):

        localctx = csParser.ScopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_scope)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(csParser.T__0)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << csParser.T__5) | (1 << csParser.STATIC) | (1 << csParser.VAR))) != 0):
                self.state = 23
                self.r_decl()
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.r_stmt()
            self.state = 30
            self.match(csParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class R_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.t = None # R_typeContext
            self._NAME = None # Token

        def VAR(self):
            return self.getToken(csParser.VAR, 0)

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(csParser.NameContext)
            else:
                return self.getTypedRuleContext(csParser.NameContext,i)


        def r_type(self):
            return self.getTypedRuleContext(csParser.R_typeContext,0)


        def static(self):
            return self.getTypedRuleContext(csParser.StaticContext,0)


        def expr(self):
            return self.getTypedRuleContext(csParser.ExprContext,0)


        def NAME(self):
            return self.getToken(csParser.NAME, 0)

        def block(self):
            return self.getTypedRuleContext(csParser.BlockContext,0)


        def getRuleIndex(self):
            return csParser.RULE_r_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR_decl" ):
                listener.enterR_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR_decl" ):
                listener.exitR_decl(self)




    def r_decl(self):

        localctx = csParser.R_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_r_decl)
        self._la = 0 # Token type
        try:
            self.state = 61
            token = self._input.LA(1)
            if token in [csParser.STATIC, csParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                _la = self._input.LA(1)
                if _la==csParser.STATIC:
                    self.state = 32
                    self.static()


                self.state = 35
                self.match(csParser.VAR)
                self.state = 36
                localctx.t = self.r_type()
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 37
                        self.name()
                        self.state = 38
                        self.match(csParser.T__2) 
                    self.state = 44
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 45
                self.name()
                self.state = 48
                _la = self._input.LA(1)
                if _la==csParser.T__3:
                    self.state = 46
                    self.match(csParser.T__3)
                    self.state = 47
                    self.expr()


                self.state = 50
                self.match(csParser.T__4)
                facts.create_fact("typeOF", (None if localctx.t is None else self._input.getText((localctx.t.start,localctx.t.stop))), variables.nameList)
                {facts.if_not_empty(variables.staticOpt, [("Static", variables.nameList)])}
                semantic.release_node()

            elif token in [csParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(csParser.T__5)
                self.state = 56
                localctx._NAME = self.match(csParser.NAME)
                semantic.add_scope((None if localctx._NAME is None else localctx._NAME.text))
                self.state = 58
                self.block()
                semantic.remove_scope()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class R_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NAME = None # Token

        def NAME(self):
            return self.getToken(csParser.NAME, 0)

        def expr(self):
            return self.getTypedRuleContext(csParser.ExprContext,0)


        def r_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(csParser.R_stmtContext)
            else:
                return self.getTypedRuleContext(csParser.R_stmtContext,i)


        def scope(self):
            return self.getTypedRuleContext(csParser.ScopeContext,0)


        def block(self):
            return self.getTypedRuleContext(csParser.BlockContext,0)


        def getRuleIndex(self):
            return csParser.RULE_r_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR_stmt" ):
                listener.enterR_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR_stmt" ):
                listener.exitR_stmt(self)




    def r_stmt(self):

        localctx = csParser.R_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_r_stmt)
        try:
            self.state = 94
            token = self._input.LA(1)
            if token in [csParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(csParser.T__4)

            elif token in [csParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(csParser.NAME)
                self.state = 65
                self.match(csParser.T__3)
                self.state = 66
                self.expr()
                self.state = 67
                self.match(csParser.T__4)

            elif token in [csParser.T__6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self.match(csParser.T__6)
                self.state = 70
                self.match(csParser.T__7)
                self.state = 71
                self.expr()
                self.state = 72
                self.match(csParser.T__8)
                self.state = 73
                self.r_stmt()
                self.state = 76
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 74
                    self.match(csParser.T__9)
                    self.state = 75
                    self.r_stmt()



            elif token in [csParser.T__10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 78
                self.match(csParser.T__10)
                self.state = 79
                self.match(csParser.T__7)
                self.state = 80
                self.expr()
                self.state = 81
                self.match(csParser.T__8)
                self.state = 82
                self.r_stmt()

            elif token in [csParser.T__0]:
                self.enterOuterAlt(localctx, 5)
                self.state = 84
                self.scope()

            elif token in [csParser.T__11]:
                self.enterOuterAlt(localctx, 6)
                self.state = 85
                self.match(csParser.T__11)
                self.state = 86
                localctx._NAME = self.match(csParser.NAME)
                self.state = 87
                self.match(csParser.T__4)
                facts.create_fact("callTo", semantic.get_current_scope(), (None if localctx._NAME is None else localctx._NAME.text))

            elif token in [csParser.T__12]:
                self.enterOuterAlt(localctx, 7)
                self.state = 89
                self.match(csParser.T__12)
                self.state = 90
                self.expr()
                self.state = 91
                self.match(csParser.T__4)

            elif token in [csParser.T__13]:
                self.enterOuterAlt(localctx, 8)
                self.state = 93
                self.block()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def r_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(csParser.R_stmtContext)
            else:
                return self.getTypedRuleContext(csParser.R_stmtContext,i)


        def getRuleIndex(self):
            return csParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = csParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(csParser.T__13)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << csParser.T__0) | (1 << csParser.T__4) | (1 << csParser.T__6) | (1 << csParser.T__10) | (1 << csParser.T__11) | (1 << csParser.T__12) | (1 << csParser.T__13) | (1 << csParser.NAME))) != 0):
                self.state = 97
                self.r_stmt()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
            self.match(csParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aexpr(self):
            return self.getTypedRuleContext(csParser.AexprContext,0)


        def expr(self):
            return self.getTypedRuleContext(csParser.ExprContext,0)


        def getRuleIndex(self):
            return csParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = csParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.aexpr()
            self.state = 108
            _la = self._input.LA(1)
            if _la==csParser.T__15:
                self.state = 106
                self.match(csParser.T__15)
                self.state = 107
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AexprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(csParser.TermContext,0)


        def aexpr(self):
            return self.getTypedRuleContext(csParser.AexprContext,0)


        def getRuleIndex(self):
            return csParser.RULE_aexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAexpr" ):
                listener.enterAexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAexpr" ):
                listener.exitAexpr(self)




    def aexpr(self):

        localctx = csParser.AexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_aexpr)
        self._la = 0 # Token type
        try:
            self.state = 120
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.term()
                self.state = 113
                _la = self._input.LA(1)
                if _la==csParser.T__16:
                    self.state = 111
                    self.match(csParser.T__16)
                    self.state = 112
                    self.aexpr()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.term()
                self.state = 118
                _la = self._input.LA(1)
                if _la==csParser.T__17:
                    self.state = 116
                    self.match(csParser.T__17)
                    self.state = 117
                    self.aexpr()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(csParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(csParser.TermContext,0)


        def getRuleIndex(self):
            return csParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = csParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.factor()
            self.state = 125
            _la = self._input.LA(1)
            if _la==csParser.T__18:
                self.state = 123
                self.match(csParser.T__18)
                self.state = 124
                self.term()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(csParser.INT, 0)

        def NAME(self):
            return self.getToken(csParser.NAME, 0)

        def expr(self):
            return self.getTypedRuleContext(csParser.ExprContext,0)


        def getRuleIndex(self):
            return csParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = csParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_factor)
        try:
            self.state = 133
            token = self._input.LA(1)
            if token in [csParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(csParser.INT)

            elif token in [csParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.match(csParser.NAME)

            elif token in [csParser.T__7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.match(csParser.T__7)
                self.state = 130
                self.expr()
                self.state = 131
                self.match(csParser.T__8)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class R_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(csParser.INTEGER, 0)

        def getRuleIndex(self):
            return csParser.RULE_r_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR_type" ):
                listener.enterR_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR_type" ):
                listener.exitR_type(self)




    def r_type(self):

        localctx = csParser.R_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_r_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(csParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.nameElement = None
            self._NAME = None # Token

        def NAME(self):
            return self.getToken(csParser.NAME, 0)

        def getRuleIndex(self):
            return csParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = csParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            localctx._NAME = self.match(csParser.NAME)
            nameElement = semantic.exec_block("name","List", (None if localctx._NAME is None else localctx._NAME.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StaticContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.staticElement = None
            self._STATIC = None # Token

        def STATIC(self):
            return self.getToken(csParser.STATIC, 0)

        def getRuleIndex(self):
            return csParser.RULE_static

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatic" ):
                listener.enterStatic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatic" ):
                listener.exitStatic(self)




    def static(self):

        localctx = csParser.StaticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_static)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            localctx._STATIC = self.match(csParser.STATIC)
            staticElement = semantic.exec_block("static","Opt", (None if localctx._STATIC is None else localctx._STATIC.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




