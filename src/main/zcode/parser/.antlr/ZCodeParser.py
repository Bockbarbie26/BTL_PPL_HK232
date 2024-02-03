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
        4,1,55,363,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,1,0,5,0,80,
        8,0,10,0,12,0,83,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,92,8,1,1,2,
        1,2,1,2,1,2,3,2,98,8,2,1,3,1,3,1,3,3,3,103,8,3,1,4,1,4,1,4,1,4,1,
        4,1,5,1,5,1,5,1,5,3,5,114,8,5,1,6,1,6,1,6,1,6,3,6,120,8,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,130,8,6,1,7,1,7,1,7,1,7,3,7,136,8,
        7,1,8,1,8,1,8,1,8,3,8,142,8,8,1,8,1,8,3,8,146,8,8,1,8,1,8,3,8,150,
        8,8,1,8,1,8,3,8,154,8,8,1,9,1,9,3,9,158,8,9,1,10,1,10,1,10,1,10,
        1,10,3,10,165,8,10,1,11,1,11,1,11,1,11,1,11,3,11,172,8,11,1,12,1,
        12,1,12,1,12,1,12,1,12,5,12,180,8,12,10,12,12,12,183,9,12,1,13,1,
        13,1,13,1,13,1,13,1,13,5,13,191,8,13,10,13,12,13,194,9,13,1,14,1,
        14,1,14,1,14,1,14,1,14,5,14,202,8,14,10,14,12,14,205,9,14,1,15,1,
        15,1,15,1,15,1,15,1,15,5,15,213,8,15,10,15,12,15,216,9,15,1,16,1,
        16,1,16,3,16,221,8,16,1,17,1,17,1,17,3,17,226,8,17,1,18,1,18,1,18,
        1,18,1,18,5,18,233,8,18,10,18,12,18,236,9,18,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,3,19,245,8,19,1,20,1,20,1,20,1,20,1,20,1,21,1,21,
        1,21,1,21,1,21,3,21,257,8,21,1,22,1,22,3,22,261,8,22,1,22,1,22,1,
        23,1,23,1,23,1,23,1,23,3,23,270,8,23,1,24,1,24,1,24,1,24,3,24,276,
        8,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,287,8,25,
        1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,28,1,28,3,28,299,8,28,
        1,29,1,29,1,29,1,29,1,29,1,29,5,29,307,8,29,10,29,12,29,310,9,29,
        1,29,3,29,313,8,29,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,3,32,331,8,32,1,32,1,32,1,33,
        3,33,336,8,33,1,33,1,33,1,34,3,34,341,8,34,1,34,1,34,1,35,1,35,3,
        35,347,8,35,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,38,4,
        38,359,8,38,11,38,12,38,360,1,38,0,5,24,26,28,30,36,39,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,
        54,56,58,60,62,64,66,68,70,72,74,76,0,6,1,0,4,6,2,0,33,38,40,40,
        1,0,22,23,1,0,25,26,1,0,27,29,1,0,50,51,373,0,81,1,0,0,0,2,91,1,
        0,0,0,4,97,1,0,0,0,6,102,1,0,0,0,8,104,1,0,0,0,10,109,1,0,0,0,12,
        129,1,0,0,0,14,135,1,0,0,0,16,137,1,0,0,0,18,157,1,0,0,0,20,164,
        1,0,0,0,22,171,1,0,0,0,24,173,1,0,0,0,26,184,1,0,0,0,28,195,1,0,
        0,0,30,206,1,0,0,0,32,220,1,0,0,0,34,225,1,0,0,0,36,227,1,0,0,0,
        38,244,1,0,0,0,40,246,1,0,0,0,42,256,1,0,0,0,44,258,1,0,0,0,46,269,
        1,0,0,0,48,275,1,0,0,0,50,286,1,0,0,0,52,288,1,0,0,0,54,291,1,0,
        0,0,56,298,1,0,0,0,58,300,1,0,0,0,60,314,1,0,0,0,62,320,1,0,0,0,
        64,323,1,0,0,0,66,335,1,0,0,0,68,340,1,0,0,0,70,344,1,0,0,0,72,348,
        1,0,0,0,74,350,1,0,0,0,76,358,1,0,0,0,78,80,5,50,0,0,79,78,1,0,0,
        0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,81,
        1,0,0,0,84,85,3,2,1,0,85,86,5,0,0,1,86,1,1,0,0,0,87,88,3,4,2,0,88,
        89,3,2,1,0,89,92,1,0,0,0,90,92,3,4,2,0,91,87,1,0,0,0,91,90,1,0,0,
        0,92,3,1,0,0,0,93,98,3,16,8,0,94,95,3,6,3,0,95,96,3,76,38,0,96,98,
        1,0,0,0,97,93,1,0,0,0,97,94,1,0,0,0,98,5,1,0,0,0,99,103,3,8,4,0,
        100,103,3,10,5,0,101,103,3,12,6,0,102,99,1,0,0,0,102,100,1,0,0,0,
        102,101,1,0,0,0,103,7,1,0,0,0,104,105,5,8,0,0,105,106,5,46,0,0,106,
        107,5,24,0,0,107,108,3,22,11,0,108,9,1,0,0,0,109,110,5,9,0,0,110,
        113,5,46,0,0,111,112,5,24,0,0,112,114,3,22,11,0,113,111,1,0,0,0,
        113,114,1,0,0,0,114,11,1,0,0,0,115,116,7,0,0,0,116,119,5,46,0,0,
        117,118,5,24,0,0,118,120,3,22,11,0,119,117,1,0,0,0,119,120,1,0,0,
        0,120,130,1,0,0,0,121,122,5,1,0,0,122,123,5,46,0,0,123,124,5,41,
        0,0,124,125,3,14,7,0,125,126,5,42,0,0,126,127,5,24,0,0,127,128,3,
        22,11,0,128,130,1,0,0,0,129,115,1,0,0,0,129,121,1,0,0,0,130,13,1,
        0,0,0,131,132,5,47,0,0,132,133,5,45,0,0,133,136,3,14,7,0,134,136,
        5,47,0,0,135,131,1,0,0,0,135,134,1,0,0,0,136,15,1,0,0,0,137,138,
        5,10,0,0,138,139,5,46,0,0,139,141,5,43,0,0,140,142,3,18,9,0,141,
        140,1,0,0,0,141,142,1,0,0,0,142,143,1,0,0,0,143,153,5,44,0,0,144,
        146,3,76,38,0,145,144,1,0,0,0,145,146,1,0,0,0,146,147,1,0,0,0,147,
        154,3,70,35,0,148,150,3,76,38,0,149,148,1,0,0,0,149,150,1,0,0,0,
        150,151,1,0,0,0,151,154,3,74,37,0,152,154,3,76,38,0,153,145,1,0,
        0,0,153,149,1,0,0,0,153,152,1,0,0,0,154,17,1,0,0,0,155,158,3,20,
        10,0,156,158,1,0,0,0,157,155,1,0,0,0,157,156,1,0,0,0,158,19,1,0,
        0,0,159,160,3,22,11,0,160,161,5,45,0,0,161,162,3,20,10,0,162,165,
        1,0,0,0,163,165,3,22,11,0,164,159,1,0,0,0,164,163,1,0,0,0,165,21,
        1,0,0,0,166,167,3,24,12,0,167,168,5,39,0,0,168,169,3,24,12,0,169,
        172,1,0,0,0,170,172,3,24,12,0,171,166,1,0,0,0,171,170,1,0,0,0,172,
        23,1,0,0,0,173,174,6,12,-1,0,174,175,3,26,13,0,175,181,1,0,0,0,176,
        177,10,2,0,0,177,178,7,1,0,0,178,180,3,24,12,3,179,176,1,0,0,0,180,
        183,1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,25,1,0,0,0,183,181,
        1,0,0,0,184,185,6,13,-1,0,185,186,3,28,14,0,186,192,1,0,0,0,187,
        188,10,2,0,0,188,189,7,2,0,0,189,191,3,28,14,0,190,187,1,0,0,0,191,
        194,1,0,0,0,192,190,1,0,0,0,192,193,1,0,0,0,193,27,1,0,0,0,194,192,
        1,0,0,0,195,196,6,14,-1,0,196,197,3,30,15,0,197,203,1,0,0,0,198,
        199,10,2,0,0,199,200,7,3,0,0,200,202,3,30,15,0,201,198,1,0,0,0,202,
        205,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,29,1,0,0,0,205,203,
        1,0,0,0,206,207,6,15,-1,0,207,208,3,32,16,0,208,214,1,0,0,0,209,
        210,10,2,0,0,210,211,7,4,0,0,211,213,3,32,16,0,212,209,1,0,0,0,213,
        216,1,0,0,0,214,212,1,0,0,0,214,215,1,0,0,0,215,31,1,0,0,0,216,214,
        1,0,0,0,217,218,5,21,0,0,218,221,3,32,16,0,219,221,3,34,17,0,220,
        217,1,0,0,0,220,219,1,0,0,0,221,33,1,0,0,0,222,223,7,3,0,0,223,226,
        3,34,17,0,224,226,3,36,18,0,225,222,1,0,0,0,225,224,1,0,0,0,226,
        35,1,0,0,0,227,228,6,18,-1,0,228,229,3,38,19,0,229,234,1,0,0,0,230,
        231,10,2,0,0,231,233,3,40,20,0,232,230,1,0,0,0,233,236,1,0,0,0,234,
        232,1,0,0,0,234,235,1,0,0,0,235,37,1,0,0,0,236,234,1,0,0,0,237,245,
        5,46,0,0,238,245,3,42,21,0,239,240,5,43,0,0,240,241,3,22,11,0,241,
        242,5,44,0,0,242,245,1,0,0,0,243,245,3,16,8,0,244,237,1,0,0,0,244,
        238,1,0,0,0,244,239,1,0,0,0,244,243,1,0,0,0,245,39,1,0,0,0,246,247,
        3,22,11,0,247,248,5,41,0,0,248,249,3,22,11,0,249,250,5,42,0,0,250,
        41,1,0,0,0,251,257,5,47,0,0,252,257,5,48,0,0,253,257,5,2,0,0,254,
        257,5,3,0,0,255,257,3,44,22,0,256,251,1,0,0,0,256,252,1,0,0,0,256,
        253,1,0,0,0,256,254,1,0,0,0,256,255,1,0,0,0,257,43,1,0,0,0,258,260,
        5,43,0,0,259,261,3,46,23,0,260,259,1,0,0,0,260,261,1,0,0,0,261,262,
        1,0,0,0,262,263,5,44,0,0,263,45,1,0,0,0,264,265,3,22,11,0,265,266,
        5,45,0,0,266,267,3,46,23,0,267,270,1,0,0,0,268,270,3,22,11,0,269,
        264,1,0,0,0,269,268,1,0,0,0,270,47,1,0,0,0,271,272,3,50,25,0,272,
        273,3,48,24,0,273,276,1,0,0,0,274,276,1,0,0,0,275,271,1,0,0,0,275,
        274,1,0,0,0,276,49,1,0,0,0,277,287,3,52,26,0,278,287,3,54,27,0,279,
        287,3,58,29,0,280,287,3,64,32,0,281,287,3,66,33,0,282,287,3,68,34,
        0,283,287,3,70,35,0,284,287,3,72,36,0,285,287,3,74,37,0,286,277,
        1,0,0,0,286,278,1,0,0,0,286,279,1,0,0,0,286,280,1,0,0,0,286,281,
        1,0,0,0,286,282,1,0,0,0,286,283,1,0,0,0,286,284,1,0,0,0,286,285,
        1,0,0,0,287,51,1,0,0,0,288,289,3,6,3,0,289,290,3,76,38,0,290,53,
        1,0,0,0,291,292,3,56,28,0,292,293,5,24,0,0,293,294,3,22,11,0,294,
        295,3,76,38,0,295,55,1,0,0,0,296,299,5,46,0,0,297,299,3,44,22,0,
        298,296,1,0,0,0,298,297,1,0,0,0,299,57,1,0,0,0,300,301,5,16,0,0,
        301,302,5,43,0,0,302,303,3,22,11,0,303,304,5,44,0,0,304,308,3,50,
        25,0,305,307,3,60,30,0,306,305,1,0,0,0,307,310,1,0,0,0,308,306,1,
        0,0,0,308,309,1,0,0,0,309,312,1,0,0,0,310,308,1,0,0,0,311,313,3,
        62,31,0,312,311,1,0,0,0,312,313,1,0,0,0,313,59,1,0,0,0,314,315,5,
        18,0,0,315,316,5,43,0,0,316,317,3,22,11,0,317,318,5,44,0,0,318,319,
        3,50,25,0,319,61,1,0,0,0,320,321,5,17,0,0,321,322,3,50,25,0,322,
        63,1,0,0,0,323,324,5,11,0,0,324,325,5,46,0,0,325,326,5,12,0,0,326,
        327,3,22,11,0,327,328,5,13,0,0,328,330,3,22,11,0,329,331,3,76,38,
        0,330,329,1,0,0,0,330,331,1,0,0,0,331,332,1,0,0,0,332,333,3,50,25,
        0,333,65,1,0,0,0,334,336,3,76,38,0,335,334,1,0,0,0,335,336,1,0,0,
        0,336,337,1,0,0,0,337,338,5,14,0,0,338,67,1,0,0,0,339,341,3,76,38,
        0,340,339,1,0,0,0,340,341,1,0,0,0,341,342,1,0,0,0,342,343,5,15,0,
        0,343,69,1,0,0,0,344,346,5,7,0,0,345,347,3,22,11,0,346,345,1,0,0,
        0,346,347,1,0,0,0,347,71,1,0,0,0,348,349,3,16,8,0,349,73,1,0,0,0,
        350,351,5,19,0,0,351,352,3,76,38,0,352,353,3,48,24,0,353,354,3,76,
        38,0,354,355,5,20,0,0,355,356,3,76,38,0,356,75,1,0,0,0,357,359,7,
        5,0,0,358,357,1,0,0,0,359,360,1,0,0,0,360,358,1,0,0,0,360,361,1,
        0,0,0,361,77,1,0,0,0,36,81,91,97,102,113,119,129,135,141,145,149,
        153,157,164,171,181,192,203,214,220,225,234,244,256,260,269,275,
        286,298,308,312,330,335,340,346,360
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'array'", "'true'", "'false'", "'number'", 
                     "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
                     "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'<-'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'!'", "'&&'", "'||'", "'='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'...'", "'=='", "'['", "']'", 
                     "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "TRUE", "FALSE", "NUMBER", 
                      "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", 
                      "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
                      "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ASSIGNINIT", 
                      "ADD", "SUB", "MUL", "DIV", "MODUL", "NOT_OP", "AND_OP", 
                      "OR_OP", "ASSIGN", "NOT_EQUAL", "LESS_THAN", "LESS_OR_EQUAL", 
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
    RULE_funct = 8
    RULE_prameters_list = 9
    RULE_list_expr = 10
    RULE_expression = 11
    RULE_expression1 = 12
    RULE_expression2 = 13
    RULE_expression3 = 14
    RULE_expression4 = 15
    RULE_expression5 = 16
    RULE_expression6 = 17
    RULE_expression7 = 18
    RULE_expression8 = 19
    RULE_index_operator = 20
    RULE_literal = 21
    RULE_array_literal = 22
    RULE_list_literal = 23
    RULE_statement_list = 24
    RULE_statement = 25
    RULE_declaration_statement = 26
    RULE_assignment_statement = 27
    RULE_lhs = 28
    RULE_if_statement = 29
    RULE_elif_statement = 30
    RULE_else_statement = 31
    RULE_for_statement = 32
    RULE_break_statement = 33
    RULE_continue_statement = 34
    RULE_return_statement = 35
    RULE_call_statement = 36
    RULE_block_statement = 37
    RULE_ignore = 38

    ruleNames =  [ "program", "list_declared", "declared", "variables", 
                   "implicit_var", "implicit_dynamic", "keyword_var", "list_NUMBER_LIT", 
                   "funct", "prameters_list", "list_expr", "expression", 
                   "expression1", "expression2", "expression3", "expression4", 
                   "expression5", "expression6", "expression7", "expression8", 
                   "index_operator", "literal", "array_literal", "list_literal", 
                   "statement_list", "statement", "declaration_statement", 
                   "assignment_statement", "lhs", "if_statement", "elif_statement", 
                   "else_statement", "for_statement", "break_statement", 
                   "continue_statement", "return_statement", "call_statement", 
                   "block_statement", "ignore" ]

    EOF = Token.EOF
    T__0=1
    TRUE=2
    FALSE=3
    NUMBER=4
    BOOL=5
    STRING=6
    RETURN=7
    VAR=8
    DYNAMIC=9
    FUNC=10
    FOR=11
    UNTIL=12
    BY=13
    BREAK=14
    CONTINUE=15
    IF=16
    ELSE=17
    ELIF=18
    BEGIN=19
    END=20
    NOT=21
    AND=22
    OR=23
    ASSIGNINIT=24
    ADD=25
    SUB=26
    MUL=27
    DIV=28
    MODUL=29
    NOT_OP=30
    AND_OP=31
    OR_OP=32
    ASSIGN=33
    NOT_EQUAL=34
    LESS_THAN=35
    LESS_OR_EQUAL=36
    GREATER_THAN=37
    GREATER_OR_EQUAL=38
    CONCAT=39
    EQUAL=40
    LBRACKET=41
    RBRACKET=42
    LPAREN=43
    RPAREN=44
    COMMA=45
    ID=46
    NUMBER_LIT=47
    STRING_LIT=48
    BOOLEAN_LIT=49
    NEWLINE=50
    COMMENTS=51
    WS=52
    ERROR_CHAR=53
    UNCLOSE_STRING=54
    ILLEGAL_ESCAPE=55

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
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 78
                self.match(ZCodeParser.NEWLINE)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.list_declared()
            self.state = 85
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
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.declared()
                self.state = 88
                self.list_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
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

        def funct(self):
            return self.getTypedRuleContext(ZCodeParser.FunctContext,0)


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
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.funct()
                pass
            elif token in [1, 4, 5, 6, 8, 9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.variables()
                self.state = 95
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
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.implicit_var()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.implicit_dynamic()
                pass
            elif token in [1, 4, 5, 6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
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
            self.state = 104
            self.match(ZCodeParser.VAR)
            self.state = 105
            self.match(ZCodeParser.ID)
            self.state = 106
            self.match(ZCodeParser.ASSIGNINIT)
            self.state = 107
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
            self.state = 109
            self.match(ZCodeParser.DYNAMIC)
            self.state = 110
            self.match(ZCodeParser.ID)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 111
                self.match(ZCodeParser.ASSIGNINIT)
                self.state = 112
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

        def ASSIGNINIT(self):
            return self.getToken(ZCodeParser.ASSIGNINIT, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def list_NUMBER_LIT(self):
            return self.getTypedRuleContext(ZCodeParser.List_NUMBER_LITContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_keyword_var




    def keyword_var(self):

        localctx = ZCodeParser.Keyword_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_keyword_var)
        self._la = 0 # Token type
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 116
                self.match(ZCodeParser.ID)
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==24:
                    self.state = 117
                    self.match(ZCodeParser.ASSIGNINIT)
                    self.state = 118
                    self.expression()


                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.match(ZCodeParser.T__0)
                self.state = 122
                self.match(ZCodeParser.ID)
                self.state = 123
                self.match(ZCodeParser.LBRACKET)
                self.state = 124
                self.list_NUMBER_LIT()
                self.state = 125
                self.match(ZCodeParser.RBRACKET)
                self.state = 126
                self.match(ZCodeParser.ASSIGNINIT)
                self.state = 127
                self.expression()
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
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(ZCodeParser.NUMBER_LIT)
                self.state = 132
                self.match(ZCodeParser.COMMA)
                self.state = 133
                self.list_NUMBER_LIT()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(ZCodeParser.NUMBER_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctContext(ParserRuleContext):
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

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def prameters_list(self):
            return self.getTypedRuleContext(ZCodeParser.Prameters_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funct




    def funct(self):

        localctx = ZCodeParser.FunctContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_funct)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(ZCodeParser.FUNC)
            self.state = 138
            self.match(ZCodeParser.ID)
            self.state = 139
            self.match(ZCodeParser.LPAREN)
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 140
                self.prameters_list()


            self.state = 143
            self.match(ZCodeParser.RPAREN)
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==50 or _la==51:
                    self.state = 144
                    self.ignore()


                self.state = 147
                self.return_statement()
                pass

            elif la_ == 2:
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==50 or _la==51:
                    self.state = 148
                    self.ignore()


                self.state = 151
                self.block_statement()
                pass

            elif la_ == 3:
                self.state = 152
                self.ignore()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prameters_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_expr(self):
            return self.getTypedRuleContext(ZCodeParser.List_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_prameters_list




    def prameters_list(self):

        localctx = ZCodeParser.Prameters_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_prameters_list)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 10, 21, 25, 26, 43, 46, 47, 48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.list_expr()
                pass
            elif token in [44]:
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
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.expression()
                self.state = 160
                self.match(ZCodeParser.COMMA)
                self.state = 161
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
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
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.expression1(0)
                self.state = 167
                self.match(ZCodeParser.CONCAT)
                self.state = 168
                self.expression1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.expression1(0)
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

        def expression2(self):
            return self.getTypedRuleContext(ZCodeParser.Expression2Context,0)


        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression1Context,i)


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



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 181
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 176
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 177
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1640677507072) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 178
                    self.expression1(3) 
                self.state = 183
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
            self.state = 185
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 192
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 187
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 188
                    _la = self._input.LA(1)
                    if not(_la==22 or _la==23):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 189
                    self.expression3(0) 
                self.state = 194
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
            self.state = 196
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 203
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 198
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 199
                    _la = self._input.LA(1)
                    if not(_la==25 or _la==26):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 200
                    self.expression4(0) 
                self.state = 205
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
            self.state = 207
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 214
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 209
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 210
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 211
                    self.expression5() 
                self.state = 216
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(ZCodeParser.NOT)
                self.state = 218
                self.expression5()
                pass
            elif token in [2, 3, 10, 25, 26, 43, 46, 47, 48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
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
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25, 26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                _la = self._input.LA(1)
                if not(_la==25 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 223
                self.expression6()
                pass
            elif token in [2, 3, 10, 43, 46, 47, 48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.expression7(0)
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

        def expression8(self):
            return self.getTypedRuleContext(ZCodeParser.Expression8Context,0)


        def expression7(self):
            return self.getTypedRuleContext(ZCodeParser.Expression7Context,0)


        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression7



    def expression7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expression7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.expression8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 234
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression7)
                    self.state = 230
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 231
                    self.index_operator() 
                self.state = 236
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def funct(self):
            return self.getTypedRuleContext(ZCodeParser.FunctContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression8




    def expression8(self):

        localctx = ZCodeParser.Expression8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expression8)
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 239
                self.match(ZCodeParser.LPAREN)
                self.state = 240
                self.expression()
                self.state = 241
                self.match(ZCodeParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 243
                self.funct()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operator




    def index_operator(self):

        localctx = ZCodeParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_index_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.expression()
            self.state = 247
            self.match(ZCodeParser.LBRACKET)
            self.state = 248
            self.expression()
            self.state = 249
            self.match(ZCodeParser.RBRACKET)
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
        self.enterRule(localctx, 42, self.RULE_literal)
        try:
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [47]:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.match(ZCodeParser.NUMBER_LIT)
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.match(ZCodeParser.STRING_LIT)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 253
                self.match(ZCodeParser.TRUE)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 254
                self.match(ZCodeParser.FALSE)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 5)
                self.state = 255
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

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def list_literal(self):
            return self.getTypedRuleContext(ZCodeParser.List_literalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_literal




    def array_literal(self):

        localctx = ZCodeParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(ZCodeParser.LPAREN)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 501377405027340) != 0):
                self.state = 259
                self.list_literal()


            self.state = 262
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_literal(self):
            return self.getTypedRuleContext(ZCodeParser.List_literalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_literal




    def list_literal(self):

        localctx = ZCodeParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_list_literal)
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.expression()
                self.state = 265
                self.match(ZCodeParser.COMMA)
                self.state = 266
                self.list_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.expression()
                pass


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
        self.enterRule(localctx, 48, self.RULE_statement_list)
        try:
            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.statement()
                self.state = 272
                self.statement_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


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
        self.enterRule(localctx, 50, self.RULE_statement)
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.declaration_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 279
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 280
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 281
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 282
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 283
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 284
                self.call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 285
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
        self.enterRule(localctx, 52, self.RULE_declaration_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.variables()
            self.state = 289
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
        self.enterRule(localctx, 54, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.lhs()
            self.state = 292
            self.match(ZCodeParser.ASSIGNINIT)
            self.state = 293
            self.expression()
            self.state = 294
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
        self.enterRule(localctx, 56, self.RULE_lhs)
        try:
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.match(ZCodeParser.ID)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
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


        def elif_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Elif_statementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Elif_statementContext,i)


        def else_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Else_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(ZCodeParser.IF)
            self.state = 301
            self.match(ZCodeParser.LPAREN)
            self.state = 302
            self.expression()
            self.state = 303
            self.match(ZCodeParser.RPAREN)
            self.state = 304
            self.statement()
            self.state = 308
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 305
                    self.elif_statement() 
                self.state = 310
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 311
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
        self.enterRule(localctx, 60, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(ZCodeParser.ELIF)
            self.state = 315
            self.match(ZCodeParser.LPAREN)
            self.state = 316
            self.expression()
            self.state = 317
            self.match(ZCodeParser.RPAREN)
            self.state = 318
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
        self.enterRule(localctx, 62, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(ZCodeParser.ELSE)
            self.state = 321
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
        self.enterRule(localctx, 64, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(ZCodeParser.FOR)
            self.state = 324
            self.match(ZCodeParser.ID)
            self.state = 325
            self.match(ZCodeParser.UNTIL)
            self.state = 326
            self.expression()
            self.state = 327
            self.match(ZCodeParser.BY)
            self.state = 328
            self.expression()
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 329
                self.ignore()


            self.state = 332
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
        self.enterRule(localctx, 66, self.RULE_break_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50 or _la==51:
                self.state = 334
                self.ignore()


            self.state = 337
            self.match(ZCodeParser.BREAK)
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
        self.enterRule(localctx, 68, self.RULE_continue_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50 or _la==51:
                self.state = 339
                self.ignore()


            self.state = 342
            self.match(ZCodeParser.CONTINUE)
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

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(ZCodeParser.RETURN)
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 345
                self.expression()


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

        def funct(self):
            return self.getTypedRuleContext(ZCodeParser.FunctContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_call_statement




    def call_statement(self):

        localctx = ZCodeParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.funct()
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
        self.enterRule(localctx, 74, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(ZCodeParser.BEGIN)
            self.state = 351
            self.ignore()
            self.state = 352
            self.statement_list()
            self.state = 353
            self.ignore()
            self.state = 354
            self.match(ZCodeParser.END)
            self.state = 355
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
        self.enterRule(localctx, 76, self.RULE_ignore)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 357
                    _la = self._input.LA(1)
                    if not(_la==50 or _la==51):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 360 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
        self._predicates[12] = self.expression1_sempred
        self._predicates[13] = self.expression2_sempred
        self._predicates[14] = self.expression3_sempred
        self._predicates[15] = self.expression4_sempred
        self._predicates[18] = self.expression7_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression7_sempred(self, localctx:Expression7Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




