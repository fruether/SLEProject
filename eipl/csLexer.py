# Generated from cs.g4 by ANTLR 4.5.1
from antlr4 import *
from io import StringIO


from libs import facts, semantic

semantic.init()
semantic.add_scope("main")
nameList = []


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\34")
        buf.write("\u009e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\31\6\31\u008a\n\31\r\31\16\31\u008b")
        buf.write("\3\32\6\32\u008f\n\32\r\32\16\32\u0090\3\33\3\33\5\33")
        buf.write("\u0095\n\33\3\33\3\33\6\33\u0099\n\33\r\33\16\33\u009a")
        buf.write("\3\33\3\33\2\2\34\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\3\2\4\3\2\62;\3\2c")
        buf.write("|\u00a3\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\3\67\3\2\2\2\5=\3\2\2\2\7A\3\2\2\2\tC\3\2\2\2\13")
        buf.write("E\3\2\2\2\rG\3\2\2\2\17L\3\2\2\2\21O\3\2\2\2\23Q\3\2\2")
        buf.write("\2\25S\3\2\2\2\27X\3\2\2\2\31^\3\2\2\2\33c\3\2\2\2\35")
        buf.write("i\3\2\2\2\37k\3\2\2\2!m\3\2\2\2#p\3\2\2\2%r\3\2\2\2\'")
        buf.write("t\3\2\2\2)v\3\2\2\2+{\3\2\2\2-\177\3\2\2\2/\u0084\3\2")
        buf.write("\2\2\61\u0089\3\2\2\2\63\u008e\3\2\2\2\65\u0098\3\2\2")
        buf.write("\2\678\7d\2\289\7g\2\29:\7i\2\2:;\7k\2\2;<\7p\2\2<\4\3")
        buf.write("\2\2\2=>\7g\2\2>?\7p\2\2?@\7f\2\2@\6\3\2\2\2AB\7.\2\2")
        buf.write("B\b\3\2\2\2CD\7?\2\2D\n\3\2\2\2EF\7=\2\2F\f\3\2\2\2GH")
        buf.write("\7r\2\2HI\7t\2\2IJ\7q\2\2JK\7e\2\2K\16\3\2\2\2LM\7k\2")
        buf.write("\2MN\7h\2\2N\20\3\2\2\2OP\7*\2\2P\22\3\2\2\2QR\7+\2\2")
        buf.write("R\24\3\2\2\2ST\7g\2\2TU\7n\2\2UV\7u\2\2VW\7g\2\2W\26\3")
        buf.write("\2\2\2XY\7y\2\2YZ\7j\2\2Z[\7k\2\2[\\\7n\2\2\\]\7g\2\2")
        buf.write("]\30\3\2\2\2^_\7e\2\2_`\7c\2\2`a\7n\2\2ab\7n\2\2b\32\3")
        buf.write("\2\2\2cd\7y\2\2de\7t\2\2ef\7k\2\2fg\7v\2\2gh\7g\2\2h\34")
        buf.write("\3\2\2\2ij\7}\2\2j\36\3\2\2\2kl\7\177\2\2l \3\2\2\2mn")
        buf.write("\7@\2\2no\7?\2\2o\"\3\2\2\2pq\7-\2\2q$\3\2\2\2rs\7/\2")
        buf.write("\2s&\3\2\2\2tu\7,\2\2u(\3\2\2\2vw\7d\2\2wx\7q\2\2xy\7")
        buf.write("q\2\2yz\7n\2\2z*\3\2\2\2{|\7k\2\2|}\7p\2\2}~\7v\2\2~,")
        buf.write("\3\2\2\2\177\u0080\7e\2\2\u0080\u0081\7j\2\2\u0081\u0082")
        buf.write("\7c\2\2\u0082\u0083\7t\2\2\u0083.\3\2\2\2\u0084\u0085")
        buf.write("\7x\2\2\u0085\u0086\7c\2\2\u0086\u0087\7t\2\2\u0087\60")
        buf.write("\3\2\2\2\u0088\u008a\t\2\2\2\u0089\u0088\3\2\2\2\u008a")
        buf.write("\u008b\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2")
        buf.write("\u008c\62\3\2\2\2\u008d\u008f\t\3\2\2\u008e\u008d\3\2")
        buf.write("\2\2\u008f\u0090\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091")
        buf.write("\3\2\2\2\u0091\64\3\2\2\2\u0092\u0099\7\"\2\2\u0093\u0095")
        buf.write("\7\17\2\2\u0094\u0093\3\2\2\2\u0094\u0095\3\2\2\2\u0095")
        buf.write("\u0096\3\2\2\2\u0096\u0099\7\f\2\2\u0097\u0099\7\13\2")
        buf.write("\2\u0098\u0092\3\2\2\2\u0098\u0094\3\2\2\2\u0098\u0097")
        buf.write("\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u0098\3\2\2\2\u009a")
        buf.write("\u009b\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d\b\33\2")
        buf.write("\2\u009d\66\3\2\2\2\b\2\u008b\u0090\u0094\u0098\u009a")
        buf.write("\3\3\33\2")
        return buf.getvalue()


class csLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    BOOLEAN = 20
    INTEGER = 21
    CHAR = 22
    VAR = 23
    INT = 24
    NAME = 25
    WS = 26

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'begin'", "'end'", "','", "'='", "';'", "'proc'", "'if'", "'('", 
            "')'", "'else'", "'while'", "'call'", "'write'", "'{'", "'}'", 
            "'>='", "'+'", "'-'", "'*'", "'bool'", "'int'", "'char'", "'var'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLEAN", "INTEGER", "CHAR", "VAR", "INT", "NAME", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "BOOLEAN", 
                  "INTEGER", "CHAR", "VAR", "INT", "NAME", "WS" ]

    grammarFileName = "cs.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
    	if self._actions is None:
    		actions = dict()
    		actions[25] = self.WS_action 
    		self._actions = actions
    	action = self._actions.get(ruleIndex, None)
    	if action is not None:
    		action(localctx, actionIndex)
    	else:
    		raise Exception("No registered action for:" + str(ruleIndex))

    def WS_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.skip();
     


