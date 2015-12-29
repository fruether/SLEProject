# Generated from cs.g4 by ANTLR 4.5.1
# encoding: utf-8
from antlr4 import *
from io import StringIO


from libs import facts, semantic

semantic.init()
semantic.add_scope("main")

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\34")
        buf.write("\u0089\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\7\2\31\n\2")
        buf.write("\f\2\16\2\34\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\7\3")
        buf.write("&\n\3\f\3\16\3)\13\3\3\3\3\3\3\3\5\3.\n\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3:\n\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4I\n\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\5\4[\n\4\3\5\3\5\7\5_\n\5\f\5\16\5b\13\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\5\6i\n\6\3\7\3\7\3\7\5\7n\n\7\3\7\3\7\3\7\5")
        buf.write("\7s\n\7\5\7u\n\7\3\b\3\b\3\b\5\bz\n\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\5\t\u0082\n\t\3\n\3\n\3\13\3\13\3\13\3\13\2\2")
        buf.write("\f\2\4\6\b\n\f\16\20\22\24\2\2\u0092\2\26\3\2\2\2\49\3")
        buf.write("\2\2\2\6Z\3\2\2\2\b\\\3\2\2\2\ne\3\2\2\2\ft\3\2\2\2\16")
        buf.write("v\3\2\2\2\20\u0081\3\2\2\2\22\u0083\3\2\2\2\24\u0085\3")
        buf.write("\2\2\2\26\32\7\3\2\2\27\31\5\4\3\2\30\27\3\2\2\2\31\34")
        buf.write("\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\35\3\2\2\2\34")
        buf.write("\32\3\2\2\2\35\36\5\6\4\2\36\37\7\4\2\2\37\3\3\2\2\2 ")
        buf.write("!\7\31\2\2!\'\5\22\n\2\"#\5\24\13\2#$\7\5\2\2$&\3\2\2")
        buf.write("\2%\"\3\2\2\2&)\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(*\3\2\2")
        buf.write("\2)\'\3\2\2\2*-\5\24\13\2+,\7\6\2\2,.\5\n\6\2-+\3\2\2")
        buf.write("\2-.\3\2\2\2./\3\2\2\2/\60\7\7\2\2\60\61\b\3\1\2\61\62")
        buf.write("\b\3\1\2\62:\3\2\2\2\63\64\7\b\2\2\64\65\7\33\2\2\65\66")
        buf.write("\b\3\1\2\66\67\5\b\5\2\678\b\3\1\28:\3\2\2\29 \3\2\2\2")
        buf.write("9\63\3\2\2\2:\5\3\2\2\2;[\7\7\2\2<=\7\33\2\2=>\7\6\2\2")
        buf.write(">?\5\n\6\2?@\7\7\2\2@[\3\2\2\2AB\7\t\2\2BC\7\n\2\2CD\5")
        buf.write("\n\6\2DE\7\13\2\2EH\5\6\4\2FG\7\f\2\2GI\5\6\4\2HF\3\2")
        buf.write("\2\2HI\3\2\2\2I[\3\2\2\2JK\7\r\2\2KL\7\n\2\2LM\5\n\6\2")
        buf.write("MN\7\13\2\2NO\5\6\4\2O[\3\2\2\2P[\5\2\2\2QR\7\16\2\2R")
        buf.write("S\7\33\2\2ST\7\7\2\2T[\b\4\1\2UV\7\17\2\2VW\5\n\6\2WX")
        buf.write("\7\7\2\2X[\3\2\2\2Y[\5\b\5\2Z;\3\2\2\2Z<\3\2\2\2ZA\3\2")
        buf.write("\2\2ZJ\3\2\2\2ZP\3\2\2\2ZQ\3\2\2\2ZU\3\2\2\2ZY\3\2\2\2")
        buf.write("[\7\3\2\2\2\\`\7\20\2\2]_\5\6\4\2^]\3\2\2\2_b\3\2\2\2")
        buf.write("`^\3\2\2\2`a\3\2\2\2ac\3\2\2\2b`\3\2\2\2cd\7\21\2\2d\t")
        buf.write("\3\2\2\2eh\5\f\7\2fg\7\22\2\2gi\5\n\6\2hf\3\2\2\2hi\3")
        buf.write("\2\2\2i\13\3\2\2\2jm\5\16\b\2kl\7\23\2\2ln\5\f\7\2mk\3")
        buf.write("\2\2\2mn\3\2\2\2nu\3\2\2\2or\5\16\b\2pq\7\24\2\2qs\5\f")
        buf.write("\7\2rp\3\2\2\2rs\3\2\2\2su\3\2\2\2tj\3\2\2\2to\3\2\2\2")
        buf.write("u\r\3\2\2\2vy\5\20\t\2wx\7\25\2\2xz\5\16\b\2yw\3\2\2\2")
        buf.write("yz\3\2\2\2z\17\3\2\2\2{\u0082\7\32\2\2|\u0082\7\33\2\2")
        buf.write("}~\7\n\2\2~\177\5\n\6\2\177\u0080\7\13\2\2\u0080\u0082")
        buf.write("\3\2\2\2\u0081{\3\2\2\2\u0081|\3\2\2\2\u0081}\3\2\2\2")
        buf.write("\u0082\21\3\2\2\2\u0083\u0084\7\27\2\2\u0084\23\3\2\2")
        buf.write("\2\u0085\u0086\7\33\2\2\u0086\u0087\b\13\1\2\u0087\25")
        buf.write("\3\2\2\2\17\32\'-9HZ`hmrty\u0081")
        return buf.getvalue()


class csParser ( Parser ):

    grammarFileName = "cs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'begin'", "'end'", "','", "'='", "';'", 
                     "'proc'", "'if'", "'('", "')'", "'else'", "'while'", 
                     "'call'", "'write'", "'{'", "'}'", "'>='", "'+'", "'-'", 
                     "'*'", "'bool'", "'int'", "'char'", "'var'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BOOLEAN", "INTEGER", "CHAR", "VAR", "INT", "NAME", 
                      "WS" ]

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

    ruleNames =  [ "scope", "r_decl", "r_stmt", "block", "expr", "aexpr", 
                   "term", "factor", "r_type", "name" ]

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
    VAR=23
    INT=24
    NAME=25
    WS=26

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
            self.state = 20
            self.match(csParser.T__0)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==csParser.T__5 or _la==csParser.VAR:
                self.state = 21
                self.r_decl()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 27
            self.r_stmt()
            self.state = 28
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
            self.l = None # NameContext
            self._NAME = None # Token

        def VAR(self):
            return self.getToken(csParser.VAR, 0)

        def r_type(self):
            return self.getTypedRuleContext(csParser.R_typeContext,0)


        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(csParser.NameContext)
            else:
                return self.getTypedRuleContext(csParser.NameContext,i)


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
            self.state = 55
            token = self._input.LA(1)
            if token in [csParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(csParser.VAR)
                self.state = 31
                localctx.t = self.r_type()
                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 32
                        self.name()
                        self.state = 33
                        self.match(csParser.T__2) 
                    self.state = 39
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 40
                localctx.l = self.name()
                self.state = 43
                _la = self._input.LA(1)
                if _la==csParser.T__3:
                    self.state = 41
                    self.match(csParser.T__3)
                    self.state = 42
                    self.expr()


                self.state = 45
                self.match(csParser.T__4)
                facts.create_fact("typeOF", (None if localctx.t is None else self._input.getText((localctx.t.start,localctx.t.stop))), localctx.l.nameList)
                semantic.release_node()

            elif token in [csParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(csParser.T__5)
                self.state = 50
                localctx._NAME = self.match(csParser.NAME)
                semantic.add_scope((None if localctx._NAME is None else localctx._NAME.text))
                self.state = 52
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
            self.state = 88
            token = self._input.LA(1)
            if token in [csParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.match(csParser.T__4)

            elif token in [csParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.match(csParser.NAME)
                self.state = 59
                self.match(csParser.T__3)
                self.state = 60
                self.expr()
                self.state = 61
                self.match(csParser.T__4)

            elif token in [csParser.T__6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.match(csParser.T__6)
                self.state = 64
                self.match(csParser.T__7)
                self.state = 65
                self.expr()
                self.state = 66
                self.match(csParser.T__8)
                self.state = 67
                self.r_stmt()
                self.state = 70
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 68
                    self.match(csParser.T__9)
                    self.state = 69
                    self.r_stmt()



            elif token in [csParser.T__10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.match(csParser.T__10)
                self.state = 73
                self.match(csParser.T__7)
                self.state = 74
                self.expr()
                self.state = 75
                self.match(csParser.T__8)
                self.state = 76
                self.r_stmt()

            elif token in [csParser.T__0]:
                self.enterOuterAlt(localctx, 5)
                self.state = 78
                self.scope()

            elif token in [csParser.T__11]:
                self.enterOuterAlt(localctx, 6)
                self.state = 79
                self.match(csParser.T__11)
                self.state = 80
                localctx._NAME = self.match(csParser.NAME)
                self.state = 81
                self.match(csParser.T__4)
                facts.create_fact("callTo", semantic.get_current_scope(), (None if localctx._NAME is None else localctx._NAME.text))

            elif token in [csParser.T__12]:
                self.enterOuterAlt(localctx, 7)
                self.state = 83
                self.match(csParser.T__12)
                self.state = 84
                self.expr()
                self.state = 85
                self.match(csParser.T__4)

            elif token in [csParser.T__13]:
                self.enterOuterAlt(localctx, 8)
                self.state = 87
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
            self.state = 90
            self.match(csParser.T__13)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << csParser.T__0) | (1 << csParser.T__4) | (1 << csParser.T__6) | (1 << csParser.T__10) | (1 << csParser.T__11) | (1 << csParser.T__12) | (1 << csParser.T__13) | (1 << csParser.NAME))) != 0):
                self.state = 91
                self.r_stmt()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
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
            self.state = 99
            self.aexpr()
            self.state = 102
            _la = self._input.LA(1)
            if _la==csParser.T__15:
                self.state = 100
                self.match(csParser.T__15)
                self.state = 101
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
            self.state = 114
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.term()
                self.state = 107
                _la = self._input.LA(1)
                if _la==csParser.T__16:
                    self.state = 105
                    self.match(csParser.T__16)
                    self.state = 106
                    self.aexpr()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.term()
                self.state = 112
                _la = self._input.LA(1)
                if _la==csParser.T__17:
                    self.state = 110
                    self.match(csParser.T__17)
                    self.state = 111
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
            self.state = 116
            self.factor()
            self.state = 119
            _la = self._input.LA(1)
            if _la==csParser.T__18:
                self.state = 117
                self.match(csParser.T__18)
                self.state = 118
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
            self.state = 127
            token = self._input.LA(1)
            if token in [csParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.match(csParser.INT)

            elif token in [csParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.match(csParser.NAME)

            elif token in [csParser.T__7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 123
                self.match(csParser.T__7)
                self.state = 124
                self.expr()
                self.state = 125
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
            self.state = 129
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
            self.nameList = None
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
            self.state = 131
            localctx._NAME = self.match(csParser.NAME)

            semantic.add_context("Name", (None if localctx._NAME is None else localctx._NAME.text))
            localctx.nameList = semantic.terminal_list("Name")

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





