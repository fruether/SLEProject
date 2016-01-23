# Generated from cs.g4 by ANTLR 4.5.1
from antlr4 import *
from io import StringIO


from libs import facts, semantic, variables

semantic.init()
semantic.add_scope("main")
variables.nameList = []
variables.staticOpt = None


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\35")
        buf.write("\u00a7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\20\3")
        buf.write("\20\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\32\6\32\u0093\n\32\r\32\16\32\u0094\3\33")
        buf.write("\6\33\u0098\n\33\r\33\16\33\u0099\3\34\3\34\5\34\u009e")
        buf.write("\n\34\3\34\3\34\6\34\u00a2\n\34\r\34\16\34\u00a3\3\34")
        buf.write("\3\34\2\2\35\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\35\3\2\4\3\2\62;\3\2")
        buf.write("c|\u00ac\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\39\3\2\2\2\5?\3\2\2\2\7C\3\2\2\2\t")
        buf.write("E\3\2\2\2\13G\3\2\2\2\rI\3\2\2\2\17N\3\2\2\2\21Q\3\2\2")
        buf.write("\2\23S\3\2\2\2\25U\3\2\2\2\27Z\3\2\2\2\31`\3\2\2\2\33")
        buf.write("e\3\2\2\2\35k\3\2\2\2\37m\3\2\2\2!o\3\2\2\2#r\3\2\2\2")
        buf.write("%t\3\2\2\2\'v\3\2\2\2)x\3\2\2\2+}\3\2\2\2-\u0081\3\2\2")
        buf.write("\2/\u0086\3\2\2\2\61\u008d\3\2\2\2\63\u0092\3\2\2\2\65")
        buf.write("\u0097\3\2\2\2\67\u00a1\3\2\2\29:\7d\2\2:;\7g\2\2;<\7")
        buf.write("i\2\2<=\7k\2\2=>\7p\2\2>\4\3\2\2\2?@\7g\2\2@A\7p\2\2A")
        buf.write("B\7f\2\2B\6\3\2\2\2CD\7.\2\2D\b\3\2\2\2EF\7?\2\2F\n\3")
        buf.write("\2\2\2GH\7=\2\2H\f\3\2\2\2IJ\7r\2\2JK\7t\2\2KL\7q\2\2")
        buf.write("LM\7e\2\2M\16\3\2\2\2NO\7k\2\2OP\7h\2\2P\20\3\2\2\2QR")
        buf.write("\7*\2\2R\22\3\2\2\2ST\7+\2\2T\24\3\2\2\2UV\7g\2\2VW\7")
        buf.write("n\2\2WX\7u\2\2XY\7g\2\2Y\26\3\2\2\2Z[\7y\2\2[\\\7j\2\2")
        buf.write("\\]\7k\2\2]^\7n\2\2^_\7g\2\2_\30\3\2\2\2`a\7e\2\2ab\7")
        buf.write("c\2\2bc\7n\2\2cd\7n\2\2d\32\3\2\2\2ef\7y\2\2fg\7t\2\2")
        buf.write("gh\7k\2\2hi\7v\2\2ij\7g\2\2j\34\3\2\2\2kl\7}\2\2l\36\3")
        buf.write("\2\2\2mn\7\177\2\2n \3\2\2\2op\7@\2\2pq\7?\2\2q\"\3\2")
        buf.write("\2\2rs\7-\2\2s$\3\2\2\2tu\7/\2\2u&\3\2\2\2vw\7,\2\2w(")
        buf.write("\3\2\2\2xy\7d\2\2yz\7q\2\2z{\7q\2\2{|\7n\2\2|*\3\2\2\2")
        buf.write("}~\7k\2\2~\177\7p\2\2\177\u0080\7v\2\2\u0080,\3\2\2\2")
        buf.write("\u0081\u0082\7e\2\2\u0082\u0083\7j\2\2\u0083\u0084\7c")
        buf.write("\2\2\u0084\u0085\7t\2\2\u0085.\3\2\2\2\u0086\u0087\7u")
        buf.write("\2\2\u0087\u0088\7v\2\2\u0088\u0089\7c\2\2\u0089\u008a")
        buf.write("\7v\2\2\u008a\u008b\7k\2\2\u008b\u008c\7e\2\2\u008c\60")
        buf.write("\3\2\2\2\u008d\u008e\7x\2\2\u008e\u008f\7c\2\2\u008f\u0090")
        buf.write("\7t\2\2\u0090\62\3\2\2\2\u0091\u0093\t\2\2\2\u0092\u0091")
        buf.write("\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0092\3\2\2\2\u0094")
        buf.write("\u0095\3\2\2\2\u0095\64\3\2\2\2\u0096\u0098\t\3\2\2\u0097")
        buf.write("\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u0097\3\2\2\2")
        buf.write("\u0099\u009a\3\2\2\2\u009a\66\3\2\2\2\u009b\u00a2\7\"")
        buf.write("\2\2\u009c\u009e\7\17\2\2\u009d\u009c\3\2\2\2\u009d\u009e")
        buf.write("\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a2\7\f\2\2\u00a0")
        buf.write("\u00a2\7\13\2\2\u00a1\u009b\3\2\2\2\u00a1\u009d\3\2\2")
        buf.write("\2\u00a1\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a1")
        buf.write("\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5")
        buf.write("\u00a6\b\34\2\2\u00a68\3\2\2\2\b\2\u0094\u0099\u009d\u00a1")
        buf.write("\u00a3\3\3\34\2")
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
    STATIC = 23
    VAR = 24
    INT = 25
    NAME = 26
    WS = 27

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'begin'", "'end'", "','", "'='", "';'", "'proc'", "'if'", "'('", 
            "')'", "'else'", "'while'", "'call'", "'write'", "'{'", "'}'", 
            "'>='", "'+'", "'-'", "'*'", "'bool'", "'int'", "'char'", "'static'", 
            "'var'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLEAN", "INTEGER", "CHAR", "STATIC", "VAR", "INT", "NAME", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "BOOLEAN", 
                  "INTEGER", "CHAR", "STATIC", "VAR", "INT", "NAME", "WS" ]

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
    		actions[26] = self.WS_action 
    		self._actions = actions
    	action = self._actions.get(ruleIndex, None)
    	if action is not None:
    		action(localctx, actionIndex)
    	else:
    		raise Exception("No registered action for:" + str(ruleIndex))

    def WS_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.skip();
     


