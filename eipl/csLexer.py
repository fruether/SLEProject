# Generated from cs.g4 by ANTLR 4.5.1
from antlr4 import *
from io import StringIO


from libs import facts, semantic

semantic.init()
semantic.add_scope("main")


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\33")
        buf.write("\u009a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\22")
        buf.write("\3\22\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30")
        buf.write("\6\30\u0086\n\30\r\30\16\30\u0087\3\31\6\31\u008b\n\31")
        buf.write("\r\31\16\31\u008c\3\32\3\32\5\32\u0091\n\32\3\32\3\32")
        buf.write("\6\32\u0095\n\32\r\32\16\32\u0096\3\32\3\32\2\2\33\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\3\2\4\3\2\62;\3\2c|\u009f\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\3\65\3\2\2\2\5;\3\2\2\2\7?\3\2\2\2")
        buf.write("\tA\3\2\2\2\13C\3\2\2\2\rH\3\2\2\2\17K\3\2\2\2\21M\3\2")
        buf.write("\2\2\23O\3\2\2\2\25T\3\2\2\2\27Z\3\2\2\2\31_\3\2\2\2\33")
        buf.write("e\3\2\2\2\35g\3\2\2\2\37i\3\2\2\2!l\3\2\2\2#n\3\2\2\2")
        buf.write("%p\3\2\2\2\'r\3\2\2\2)w\3\2\2\2+{\3\2\2\2-\u0080\3\2\2")
        buf.write("\2/\u0085\3\2\2\2\61\u008a\3\2\2\2\63\u0094\3\2\2\2\65")
        buf.write("\66\7d\2\2\66\67\7g\2\2\678\7i\2\289\7k\2\29:\7p\2\2:")
        buf.write("\4\3\2\2\2;<\7g\2\2<=\7p\2\2=>\7f\2\2>\6\3\2\2\2?@\7?")
        buf.write("\2\2@\b\3\2\2\2AB\7=\2\2B\n\3\2\2\2CD\7r\2\2DE\7t\2\2")
        buf.write("EF\7q\2\2FG\7e\2\2G\f\3\2\2\2HI\7k\2\2IJ\7h\2\2J\16\3")
        buf.write("\2\2\2KL\7*\2\2L\20\3\2\2\2MN\7+\2\2N\22\3\2\2\2OP\7g")
        buf.write("\2\2PQ\7n\2\2QR\7u\2\2RS\7g\2\2S\24\3\2\2\2TU\7y\2\2U")
        buf.write("V\7j\2\2VW\7k\2\2WX\7n\2\2XY\7g\2\2Y\26\3\2\2\2Z[\7e\2")
        buf.write("\2[\\\7c\2\2\\]\7n\2\2]^\7n\2\2^\30\3\2\2\2_`\7y\2\2`")
        buf.write("a\7t\2\2ab\7k\2\2bc\7v\2\2cd\7g\2\2d\32\3\2\2\2ef\7}\2")
        buf.write("\2f\34\3\2\2\2gh\7\177\2\2h\36\3\2\2\2ij\7@\2\2jk\7?\2")
        buf.write("\2k \3\2\2\2lm\7-\2\2m\"\3\2\2\2no\7/\2\2o$\3\2\2\2pq")
        buf.write("\7,\2\2q&\3\2\2\2rs\7d\2\2st\7q\2\2tu\7q\2\2uv\7n\2\2")
        buf.write("v(\3\2\2\2wx\7k\2\2xy\7p\2\2yz\7v\2\2z*\3\2\2\2{|\7e\2")
        buf.write("\2|}\7j\2\2}~\7c\2\2~\177\7t\2\2\177,\3\2\2\2\u0080\u0081")
        buf.write("\7x\2\2\u0081\u0082\7c\2\2\u0082\u0083\7t\2\2\u0083.\3")
        buf.write("\2\2\2\u0084\u0086\t\2\2\2\u0085\u0084\3\2\2\2\u0086\u0087")
        buf.write("\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088")
        buf.write("\60\3\2\2\2\u0089\u008b\t\3\2\2\u008a\u0089\3\2\2\2\u008b")
        buf.write("\u008c\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2")
        buf.write("\u008d\62\3\2\2\2\u008e\u0095\7\"\2\2\u008f\u0091\7\17")
        buf.write("\2\2\u0090\u008f\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0092")
        buf.write("\3\2\2\2\u0092\u0095\7\f\2\2\u0093\u0095\7\13\2\2\u0094")
        buf.write("\u008e\3\2\2\2\u0094\u0090\3\2\2\2\u0094\u0093\3\2\2\2")
        buf.write("\u0095\u0096\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3")
        buf.write("\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099\b\32\2\2\u0099")
        buf.write("\64\3\2\2\2\b\2\u0087\u008c\u0090\u0094\u0096\3\3\32\2")
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
    BOOLEAN = 19
    INTEGER = 20
    CHAR = 21
    VAR = 22
    INT = 23
    NAME = 24
    WS = 25

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'begin'", "'end'", "'='", "';'", "'proc'", "'if'", "'('", "')'", 
            "'else'", "'while'", "'call'", "'write'", "'{'", "'}'", "'>='", 
            "'+'", "'-'", "'*'", "'bool'", "'int'", "'char'", "'var'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLEAN", "INTEGER", "CHAR", "VAR", "INT", "NAME", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "BOOLEAN", "INTEGER", 
                  "CHAR", "VAR", "INT", "NAME", "WS" ]

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
    		actions[24] = self.WS_action 
    		self._actions = actions
    	action = self._actions.get(ruleIndex, None)
    	if action is not None:
    		action(localctx, actionIndex)
    	else:
    		raise Exception("No registered action for:" + str(ruleIndex))

    def WS_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.skip();
     


