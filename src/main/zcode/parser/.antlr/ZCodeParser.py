# Generated from d:/studying/BTL_PPL_HK232/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,54,335,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,5,0,76,8,0,10,0,12,0,79,9,
        0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,88,8,1,1,2,1,2,1,2,1,2,3,2,94,
        8,2,1,3,1,3,1,3,3,3,99,8,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,3,
        5,110,8,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,118,8,6,1,6,1,6,3,6,122,8,
        6,1,7,1,7,1,7,1,7,3,7,128,8,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,136,8,
        8,1,8,1,8,3,8,140,8,8,1,8,1,8,3,8,144,8,8,1,9,1,9,3,9,148,8,9,1,
        10,1,10,1,10,1,10,1,10,3,10,155,8,10,1,11,1,11,1,11,1,11,1,11,3,
        11,162,8,11,1,12,1,12,1,12,1,12,1,12,3,12,169,8,12,1,13,1,13,1,13,
        1,13,1,13,1,13,5,13,177,8,13,10,13,12,13,180,9,13,1,14,1,14,1,14,
        1,14,1,14,1,14,5,14,188,8,14,10,14,12,14,191,9,14,1,15,1,15,1,15,
        1,15,1,15,1,15,5,15,199,8,15,10,15,12,15,202,9,15,1,16,1,16,1,16,
        3,16,207,8,16,1,17,1,17,1,17,3,17,212,8,17,1,18,1,18,3,18,216,8,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,229,
        8,18,1,19,1,19,1,19,3,19,234,8,19,1,19,1,19,1,20,1,20,1,20,1,20,
        1,20,3,20,243,8,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,3,22,
        253,8,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,264,8,
        23,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,26,1,26,3,26,276,8,
        26,1,27,1,27,1,27,1,27,1,27,1,27,3,27,284,8,27,1,27,3,27,287,8,27,
        1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,3,30,305,8,30,1,30,1,30,1,31,1,31,1,31,1,32,1,32,
        1,32,1,33,1,33,3,33,317,8,33,1,33,1,33,1,34,1,34,1,34,1,35,1,35,
        1,35,1,35,1,35,1,35,1,36,4,36,331,8,36,11,36,12,36,332,1,36,0,3,
        26,28,30,37,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,0,6,1,0,3,
        5,2,0,32,37,39,39,1,0,21,22,1,0,24,25,1,0,26,28,1,0,49,50,344,0,
        77,1,0,0,0,2,87,1,0,0,0,4,93,1,0,0,0,6,98,1,0,0,0,8,100,1,0,0,0,
        10,105,1,0,0,0,12,111,1,0,0,0,14,127,1,0,0,0,16,129,1,0,0,0,18,147,
        1,0,0,0,20,154,1,0,0,0,22,161,1,0,0,0,24,168,1,0,0,0,26,170,1,0,
        0,0,28,181,1,0,0,0,30,192,1,0,0,0,32,206,1,0,0,0,34,211,1,0,0,0,
        36,228,1,0,0,0,38,230,1,0,0,0,40,242,1,0,0,0,42,244,1,0,0,0,44,252,
        1,0,0,0,46,263,1,0,0,0,48,265,1,0,0,0,50,268,1,0,0,0,52,275,1,0,
        0,0,54,277,1,0,0,0,56,288,1,0,0,0,58,294,1,0,0,0,60,297,1,0,0,0,
        62,308,1,0,0,0,64,311,1,0,0,0,66,314,1,0,0,0,68,320,1,0,0,0,70,323,
        1,0,0,0,72,330,1,0,0,0,74,76,5,49,0,0,75,74,1,0,0,0,76,79,1,0,0,
        0,77,75,1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,0,79,77,1,0,0,0,80,81,
        3,2,1,0,81,82,5,0,0,1,82,1,1,0,0,0,83,84,3,4,2,0,84,85,3,2,1,0,85,
        88,1,0,0,0,86,88,3,4,2,0,87,83,1,0,0,0,87,86,1,0,0,0,88,3,1,0,0,
        0,89,94,3,16,8,0,90,91,3,6,3,0,91,92,3,72,36,0,92,94,1,0,0,0,93,
        89,1,0,0,0,93,90,1,0,0,0,94,5,1,0,0,0,95,99,3,8,4,0,96,99,3,10,5,
        0,97,99,3,12,6,0,98,95,1,0,0,0,98,96,1,0,0,0,98,97,1,0,0,0,99,7,
        1,0,0,0,100,101,5,7,0,0,101,102,5,45,0,0,102,103,5,23,0,0,103,104,
        3,22,11,0,104,9,1,0,0,0,105,106,5,8,0,0,106,109,5,45,0,0,107,108,
        5,23,0,0,108,110,3,22,11,0,109,107,1,0,0,0,109,110,1,0,0,0,110,11,
        1,0,0,0,111,112,7,0,0,0,112,117,5,45,0,0,113,114,5,40,0,0,114,115,
        3,14,7,0,115,116,5,41,0,0,116,118,1,0,0,0,117,113,1,0,0,0,117,118,
        1,0,0,0,118,121,1,0,0,0,119,120,5,23,0,0,120,122,3,22,11,0,121,119,
        1,0,0,0,121,122,1,0,0,0,122,13,1,0,0,0,123,124,5,46,0,0,124,125,
        5,44,0,0,125,128,3,14,7,0,126,128,5,46,0,0,127,123,1,0,0,0,127,126,
        1,0,0,0,128,15,1,0,0,0,129,130,5,9,0,0,130,131,5,45,0,0,131,132,
        5,42,0,0,132,133,3,18,9,0,133,143,5,43,0,0,134,136,3,72,36,0,135,
        134,1,0,0,0,135,136,1,0,0,0,136,137,1,0,0,0,137,144,3,66,33,0,138,
        140,3,72,36,0,139,138,1,0,0,0,139,140,1,0,0,0,140,141,1,0,0,0,141,
        144,3,70,35,0,142,144,3,72,36,0,143,135,1,0,0,0,143,139,1,0,0,0,
        143,142,1,0,0,0,144,17,1,0,0,0,145,148,3,20,10,0,146,148,1,0,0,0,
        147,145,1,0,0,0,147,146,1,0,0,0,148,19,1,0,0,0,149,150,3,22,11,0,
        150,151,5,44,0,0,151,152,3,20,10,0,152,155,1,0,0,0,153,155,3,22,
        11,0,154,149,1,0,0,0,154,153,1,0,0,0,155,21,1,0,0,0,156,157,3,24,
        12,0,157,158,5,38,0,0,158,159,3,24,12,0,159,162,1,0,0,0,160,162,
        3,24,12,0,161,156,1,0,0,0,161,160,1,0,0,0,162,23,1,0,0,0,163,164,
        3,26,13,0,164,165,7,1,0,0,165,166,3,26,13,0,166,169,1,0,0,0,167,
        169,3,26,13,0,168,163,1,0,0,0,168,167,1,0,0,0,169,25,1,0,0,0,170,
        171,6,13,-1,0,171,172,3,28,14,0,172,178,1,0,0,0,173,174,10,2,0,0,
        174,175,7,2,0,0,175,177,3,28,14,0,176,173,1,0,0,0,177,180,1,0,0,
        0,178,176,1,0,0,0,178,179,1,0,0,0,179,27,1,0,0,0,180,178,1,0,0,0,
        181,182,6,14,-1,0,182,183,3,30,15,0,183,189,1,0,0,0,184,185,10,2,
        0,0,185,186,7,3,0,0,186,188,3,30,15,0,187,184,1,0,0,0,188,191,1,
        0,0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,29,1,0,0,0,191,189,1,0,
        0,0,192,193,6,15,-1,0,193,194,3,32,16,0,194,200,1,0,0,0,195,196,
        10,2,0,0,196,197,7,4,0,0,197,199,3,32,16,0,198,195,1,0,0,0,199,202,
        1,0,0,0,200,198,1,0,0,0,200,201,1,0,0,0,201,31,1,0,0,0,202,200,1,
        0,0,0,203,204,5,20,0,0,204,207,3,32,16,0,205,207,3,34,17,0,206,203,
        1,0,0,0,206,205,1,0,0,0,207,33,1,0,0,0,208,209,7,3,0,0,209,212,3,
        34,17,0,210,212,3,36,18,0,211,208,1,0,0,0,211,210,1,0,0,0,212,35,
        1,0,0,0,213,216,5,45,0,0,214,216,3,38,19,0,215,213,1,0,0,0,215,214,
        1,0,0,0,216,217,1,0,0,0,217,218,5,40,0,0,218,219,3,20,10,0,219,220,
        5,41,0,0,220,229,1,0,0,0,221,229,5,45,0,0,222,229,3,40,20,0,223,
        224,5,42,0,0,224,225,3,22,11,0,225,226,5,43,0,0,226,229,1,0,0,0,
        227,229,3,38,19,0,228,215,1,0,0,0,228,221,1,0,0,0,228,222,1,0,0,
        0,228,223,1,0,0,0,228,227,1,0,0,0,229,37,1,0,0,0,230,231,5,45,0,
        0,231,233,5,42,0,0,232,234,3,20,10,0,233,232,1,0,0,0,233,234,1,0,
        0,0,234,235,1,0,0,0,235,236,5,43,0,0,236,39,1,0,0,0,237,243,5,46,
        0,0,238,243,5,47,0,0,239,243,5,1,0,0,240,243,5,2,0,0,241,243,3,42,
        21,0,242,237,1,0,0,0,242,238,1,0,0,0,242,239,1,0,0,0,242,240,1,0,
        0,0,242,241,1,0,0,0,243,41,1,0,0,0,244,245,5,40,0,0,245,246,3,20,
        10,0,246,247,5,41,0,0,247,43,1,0,0,0,248,249,3,46,23,0,249,250,3,
        44,22,0,250,253,1,0,0,0,251,253,1,0,0,0,252,248,1,0,0,0,252,251,
        1,0,0,0,253,45,1,0,0,0,254,264,3,48,24,0,255,264,3,50,25,0,256,264,
        3,54,27,0,257,264,3,60,30,0,258,264,3,62,31,0,259,264,3,64,32,0,
        260,264,3,66,33,0,261,264,3,68,34,0,262,264,3,70,35,0,263,254,1,
        0,0,0,263,255,1,0,0,0,263,256,1,0,0,0,263,257,1,0,0,0,263,258,1,
        0,0,0,263,259,1,0,0,0,263,260,1,0,0,0,263,261,1,0,0,0,263,262,1,
        0,0,0,264,47,1,0,0,0,265,266,3,6,3,0,266,267,3,72,36,0,267,49,1,
        0,0,0,268,269,3,52,26,0,269,270,5,23,0,0,270,271,3,22,11,0,271,272,
        3,72,36,0,272,51,1,0,0,0,273,276,5,45,0,0,274,276,3,42,21,0,275,
        273,1,0,0,0,275,274,1,0,0,0,276,53,1,0,0,0,277,278,5,15,0,0,278,
        279,5,42,0,0,279,280,3,22,11,0,280,281,5,43,0,0,281,283,3,46,23,
        0,282,284,3,56,28,0,283,282,1,0,0,0,283,284,1,0,0,0,284,286,1,0,
        0,0,285,287,3,58,29,0,286,285,1,0,0,0,286,287,1,0,0,0,287,55,1,0,
        0,0,288,289,5,17,0,0,289,290,5,42,0,0,290,291,3,22,11,0,291,292,
        5,43,0,0,292,293,3,46,23,0,293,57,1,0,0,0,294,295,5,16,0,0,295,296,
        3,46,23,0,296,59,1,0,0,0,297,298,5,10,0,0,298,299,5,45,0,0,299,300,
        5,11,0,0,300,301,3,22,11,0,301,302,5,12,0,0,302,304,3,22,11,0,303,
        305,3,72,36,0,304,303,1,0,0,0,304,305,1,0,0,0,305,306,1,0,0,0,306,
        307,3,46,23,0,307,61,1,0,0,0,308,309,5,13,0,0,309,310,3,72,36,0,
        310,63,1,0,0,0,311,312,5,14,0,0,312,313,3,72,36,0,313,65,1,0,0,0,
        314,316,5,6,0,0,315,317,3,20,10,0,316,315,1,0,0,0,316,317,1,0,0,
        0,317,318,1,0,0,0,318,319,3,72,36,0,319,67,1,0,0,0,320,321,3,38,
        19,0,321,322,3,72,36,0,322,69,1,0,0,0,323,324,5,18,0,0,324,325,3,
        72,36,0,325,326,3,44,22,0,326,327,5,19,0,0,327,328,3,72,36,0,328,
        71,1,0,0,0,329,331,7,5,0,0,330,329,1,0,0,0,331,332,1,0,0,0,332,330,
        1,0,0,0,332,333,1,0,0,0,333,73,1,0,0,0,32,77,87,93,98,109,117,121,
        127,135,139,143,147,154,161,168,178,189,200,206,211,215,228,233,
        242,252,263,275,283,286,304,316,332
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'<-'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'!'", "'&&'", "'||'", "'='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'...'", "'=='", "'['", "']'", 
                     "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "NOT", "AND", "OR", "ASSIGNINIT", "ADD", "SUB", 
                      "MUL", "DIV", "MODUL", "NOT_OP", "AND_OP", "OR_OP", 
                      "ASSIGN", "NOT_EQUAL", "LESS_THAN", "LESS_OR_EQUAL", 
                      "GREATER_THAN", "GREATER_OR_EQUAL", "CONCAT", "EQUAL", 
                      "LBRACKET", "RBRACKET", "LPAREN", "RPAREN", "COMMA", 
                      "ID", "NUMBER_LIT", "STRING_LIT", "BOOLEAN_LIT", "NEWLINE", 
                      "COMMENTS", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_list_declared = 1
    RULE_declared = 2
    RULE_variables = 3
    RULE_implicit_var = 4
    RULE_implicit_dynamic = 5
    RULE_keyword_var = 6
    RULE_list_NUMBER_LIT = 7
    RULE_function = 8
    RULE_parameters_list = 9
    RULE_list_expr = 10
    RULE_expression = 11
    RULE_expression1 = 12
    RULE_expression2 = 13
    RULE_expression3 = 14
    RULE_expression4 = 15
    RULE_expression5 = 16
    RULE_expression6 = 17
    RULE_expression7 = 18
    RULE_funcall = 19
    RULE_literal = 20
    RULE_array_literal = 21
    RULE_statement_list = 22
    RULE_statement = 23
    RULE_declaration_statement = 24
    RULE_assignment_statement = 25
    RULE_lhs = 26
    RULE_if_statement = 27
    RULE_elif_statement = 28
    RULE_else_statement = 29
    RULE_for_statement = 30
    RULE_break_statement = 31
    RULE_continue_statement = 32
    RULE_return_statement = 33
    RULE_call_statement = 34
    RULE_block_statement = 35
    RULE_ignore = 36

    ruleNames =  [ "program", "list_declared", "declared", "variables", 
                   "implicit_var", "implicit_dynamic", "keyword_var", "list_NUMBER_LIT", 
                   "function", "parameters_list", "list_expr", "expression", 
                   "expression1", "expression2", "expression3", "expression4", 
                   "expression5", "expression6", "expression7", "funcall", 
                   "literal", "array_literal", "statement_list", "statement", 
                   "declaration_statement", "assignment_statement", "lhs", 
                   "if_statement", "elif_statement", "else_statement", "for_statement", 
                   "break_statement", "continue_statement", "return_statement", 
                   "call_statement", "block_statement", "ignore" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    NUMBER=3
    BOOL=4
    STRING=5
    RETURN=6
    VAR=7
    DYNAMIC=8
    FUNC=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    NOT=20
    AND=21
    OR=22
    ASSIGNINIT=23
    ADD=24
    SUB=25
    MUL=26
    DIV=27
    MODUL=28
    NOT_OP=29
    AND_OP=30
    OR_OP=31
    ASSIGN=32
    NOT_EQUAL=33
    LESS_THAN=34
    LESS_OR_EQUAL=35
    GREATER_THAN=36
    GREATER_OR_EQUAL=37
    CONCAT=38
    EQUAL=39
    LBRACKET=40
    RBRACKET=41
    LPAREN=42
    RPAREN=43
    COMMA=44
    ID=45
    NUMBER_LIT=46
    STRING_LIT=47
    BOOLEAN_LIT=48
    NEWLINE=49
    COMMENTS=50
    WS=51
    ERROR_CHAR=52
    UNCLOSE_STRING=53
    ILLEGAL_ESCAPE=54

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_declared(self):
            return self.getTypedRuleContext(ZCodeParser.List_declaredContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==49:
                self.state = 74
                self.match(ZCodeParser.NEWLINE)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self.list_declared()
            self.state = 81
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared(self):
            return self.getTypedRuleContext(ZCodeParser.DeclaredContext,0)


        def list_declared(self):
            return self.getTypedRuleContext(ZCodeParser.List_declaredContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_declared




    def list_declared(self):

        localctx = ZCodeParser.List_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_list_declared)
        try:
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.declared()
                self.state = 84
                self.list_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionContext,0)


        def variables(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declared




    def declared(self):

        localctx = ZCodeParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declared)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.function()
                pass
            elif token in [3, 4, 5, 7, 8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.variables()
                self.state = 91
                self.ignore()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def implicit_var(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_varContext,0)


        def implicit_dynamic(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_dynamicContext,0)


        def keyword_var(self):
            return self.getTypedRuleContext(ZCodeParser.Keyword_varContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variables




    def variables(self):

        localctx = ZCodeParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variables)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.implicit_var()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.implicit_dynamic()
                pass
            elif token in [3, 4, 5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.keyword_var()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGNINIT(self):
            return self.getToken(ZCodeParser.ASSIGNINIT, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_var




    def implicit_var(self):

        localctx = ZCodeParser.Implicit_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_implicit_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(ZCodeParser.VAR)
            self.state = 101
            self.match(ZCodeParser.ID)
            self.state = 102
            self.match(ZCodeParser.ASSIGNINIT)
            self.state = 103
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_dynamicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGNINIT(self):
            return self.getToken(ZCodeParser.ASSIGNINIT, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_dynamic




    def implicit_dynamic(self):

        localctx = ZCodeParser.Implicit_dynamicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_implicit_dynamic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(ZCodeParser.DYNAMIC)
            self.state = 106
            self.match(ZCodeParser.ID)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 107
                self.match(ZCodeParser.ASSIGNINIT)
                self.state = 108
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keyword_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def list_NUMBER_LIT(self):
            return self.getTypedRuleContext(ZCodeParser.List_NUMBER_LITContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def ASSIGNINIT(self):
            return self.getToken(ZCodeParser.ASSIGNINIT, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_keyword_var




    def keyword_var(self):

        localctx = ZCodeParser.Keyword_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_keyword_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 112
            self.match(ZCodeParser.ID)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 113
                self.match(ZCodeParser.LBRACKET)
                self.state = 114
                self.list_NUMBER_LIT()
                self.state = 115
                self.match(ZCodeParser.RBRACKET)


            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 119
                self.match(ZCodeParser.ASSIGNINIT)
                self.state = 120
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_NUMBER_LITContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_NUMBER_LIT(self):
            return self.getTypedRuleContext(ZCodeParser.List_NUMBER_LITContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_NUMBER_LIT




    def list_NUMBER_LIT(self):

        localctx = ZCodeParser.List_NUMBER_LITContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_list_NUMBER_LIT)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.match(ZCodeParser.NUMBER_LIT)
                self.state = 124
                self.match(ZCodeParser.COMMA)
                self.state = 125
                self.list_NUMBER_LIT()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.match(ZCodeParser.NUMBER_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def parameters_list(self):
            return self.getTypedRuleContext(ZCodeParser.Parameters_listContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function




    def function(self):

        localctx = ZCodeParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(ZCodeParser.FUNC)
            self.state = 130
            self.match(ZCodeParser.ID)
            self.state = 131
            self.match(ZCodeParser.LPAREN)
            self.state = 132
            self.parameters_list()
            self.state = 133
            self.match(ZCodeParser.RPAREN)
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49 or _la==50:
                    self.state = 134
                    self.ignore()


                self.state = 137
                self.return_statement()
                pass

            elif la_ == 2:
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49 or _la==50:
                    self.state = 138
                    self.ignore()


                self.state = 141
                self.block_statement()
                pass

            elif la_ == 3:
                self.state = 142
                self.ignore()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameters_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_expr(self):
            return self.getTypedRuleContext(ZCodeParser.List_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameters_list




    def parameters_list(self):

        localctx = ZCodeParser.Parameters_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parameters_list)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 20, 24, 25, 40, 42, 45, 46, 47]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.list_expr()
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_expr(self):
            return self.getTypedRuleContext(ZCodeParser.List_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_expr




    def list_expr(self):

        localctx = ZCodeParser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_expr)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.expression()
                self.state = 150
                self.match(ZCodeParser.COMMA)
                self.state = 151
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression1Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expression)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.expression1()
                self.state = 157
                self.match(ZCodeParser.CONCAT)
                self.state = 158
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.expression1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression2Context,i)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(ZCodeParser.NOT_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(ZCodeParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(ZCodeParser.GREATER_THAN, 0)

        def LESS_OR_EQUAL(self):
            return self.getToken(ZCodeParser.LESS_OR_EQUAL, 0)

        def GREATER_OR_EQUAL(self):
            return self.getToken(ZCodeParser.GREATER_OR_EQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression1




    def expression1(self):

        localctx = ZCodeParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.expression2(0)
                self.state = 164
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 820338753536) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 165
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.expression2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(ZCodeParser.Expression2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression2



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 178
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 173
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 174
                    _la = self._input.LA(1)
                    if not(_la==21 or _la==22):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 175
                    self.expression3(0) 
                self.state = 180
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression3



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 184
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 185
                    _la = self._input.LA(1)
                    if not(_la==24 or _la==25):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 186
                    self.expression4(0) 
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MODUL(self):
            return self.getToken(ZCodeParser.MODUL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression4



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 200
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 195
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 196
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 197
                    self.expression5() 
                self.state = 202
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression5




    def expression5(self):

        localctx = ZCodeParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expression5)
        try:
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.match(ZCodeParser.NOT)
                self.state = 204
                self.expression5()
                pass
            elif token in [1, 2, 24, 25, 40, 42, 45, 46, 47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.expression6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def expression7(self):
            return self.getTypedRuleContext(ZCodeParser.Expression7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression6




    def expression6(self):

        localctx = ZCodeParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expression6)
        self._la = 0 # Token type
        try:
            self.state = 211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24, 25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                _la = self._input.LA(1)
                if not(_la==24 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 209
                self.expression6()
                pass
            elif token in [1, 2, 40, 42, 45, 46, 47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.expression7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def list_expr(self):
            return self.getTypedRuleContext(ZCodeParser.List_exprContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def funcall(self):
            return self.getTypedRuleContext(ZCodeParser.FuncallContext,0)


        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression7




    def expression7(self):

        localctx = ZCodeParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expression7)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 213
                    self.match(ZCodeParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 214
                    self.funcall()
                    pass


                self.state = 217
                self.match(ZCodeParser.LBRACKET)
                self.state = 218
                self.list_expr()
                self.state = 219
                self.match(ZCodeParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 222
                self.literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 223
                self.match(ZCodeParser.LPAREN)
                self.state = 224
                self.expression()
                self.state = 225
                self.match(ZCodeParser.RPAREN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 227
                self.funcall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def list_expr(self):
            return self.getTypedRuleContext(ZCodeParser.List_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcall




    def funcall(self):

        localctx = ZCodeParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(ZCodeParser.ID)
            self.state = 231
            self.match(ZCodeParser.LPAREN)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 251788214140934) != 0):
                self.state = 232
                self.list_expr()


            self.state = 235
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def array_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literal




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_literal)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(ZCodeParser.NUMBER_LIT)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.match(ZCodeParser.STRING_LIT)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 239
                self.match(ZCodeParser.TRUE)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 240
                self.match(ZCodeParser.FALSE)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 5)
                self.state = 241
                self.array_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def list_expr(self):
            return self.getTypedRuleContext(ZCodeParser.List_exprContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_literal




    def array_literal(self):

        localctx = ZCodeParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(ZCodeParser.LBRACKET)
            self.state = 245
            self.list_expr()
            self.state = 246
            self.match(ZCodeParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_list




    def statement_list(self):

        localctx = ZCodeParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_statement_list)
        try:
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 6, 7, 8, 10, 13, 14, 15, 18, 40, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.statement()
                self.state = 249
                self.statement_list()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Declaration_statementContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(ZCodeParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Call_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_statement)
        try:
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.declaration_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 256
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 257
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 258
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 259
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 260
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 261
                self.call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 262
                self.block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration_statement




    def declaration_statement(self):

        localctx = ZCodeParser.Declaration_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_declaration_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.variables()
            self.state = 266
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGNINIT(self):
            return self.getToken(ZCodeParser.ASSIGNINIT, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.lhs()
            self.state = 269
            self.match(ZCodeParser.ASSIGNINIT)
            self.state = 270
            self.expression()
            self.state = 271
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def array_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_lhs)
        try:
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.match(ZCodeParser.ID)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.array_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def elif_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_statementContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Else_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(ZCodeParser.IF)
            self.state = 278
            self.match(ZCodeParser.LPAREN)
            self.state = 279
            self.expression()
            self.state = 280
            self.match(ZCodeParser.RPAREN)
            self.state = 281
            self.statement()
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 282
                self.elif_statement()


            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 285
                self.else_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_statement




    def elif_statement(self):

        localctx = ZCodeParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(ZCodeParser.ELIF)
            self.state = 289
            self.match(ZCodeParser.LPAREN)
            self.state = 290
            self.expression()
            self.state = 291
            self.match(ZCodeParser.RPAREN)
            self.state = 292
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_statement




    def else_statement(self):

        localctx = ZCodeParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(ZCodeParser.ELSE)
            self.state = 295
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(ZCodeParser.FOR)
            self.state = 298
            self.match(ZCodeParser.ID)
            self.state = 299
            self.match(ZCodeParser.UNTIL)
            self.state = 300
            self.expression()
            self.state = 301
            self.match(ZCodeParser.BY)
            self.state = 302
            self.expression()
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49 or _la==50:
                self.state = 303
                self.ignore()


            self.state = 306
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(ZCodeParser.BREAK)
            self.state = 309
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(ZCodeParser.CONTINUE)
            self.state = 312
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def list_expr(self):
            return self.getTypedRuleContext(ZCodeParser.List_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(ZCodeParser.RETURN)
            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 251788214140934) != 0):
                self.state = 315
                self.list_expr()


            self.state = 318
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(ZCodeParser.FuncallContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_call_statement




    def call_statement(self):

        localctx = ZCodeParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.funcall()
            self.state = 321
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_statement




    def block_statement(self):

        localctx = ZCodeParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(ZCodeParser.BEGIN)
            self.state = 324
            self.ignore()
            self.state = 325
            self.statement_list()
            self.state = 326
            self.match(ZCodeParser.END)
            self.state = 327
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENTS(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.COMMENTS)
            else:
                return self.getToken(ZCodeParser.COMMENTS, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ignore




    def ignore(self):

        localctx = ZCodeParser.IgnoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_ignore)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 329
                _la = self._input.LA(1)
                if not(_la==49 or _la==50):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 332 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==49 or _la==50):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expression2_sempred
        self._predicates[14] = self.expression3_sempred
        self._predicates[15] = self.expression4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




