# Generated from d:/studying/HK232/PPL/BTL_PhanTien/btl1_updated/BTL1 UPDATE 25-1/initial/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,55,400,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,1,0,1,0,1,0,1,0,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,
        11,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,
        16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,
        18,1,18,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,
        21,1,22,1,22,1,22,1,23,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,
        27,1,27,1,28,1,28,1,29,1,29,1,30,1,30,1,30,1,31,1,31,1,31,1,32,1,
        32,1,33,1,33,1,33,1,34,1,34,1,35,1,35,1,35,1,36,1,36,1,37,1,37,1,
        37,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,40,1,40,1,41,1,41,1,42,1,
        42,1,43,1,43,1,44,1,44,1,45,1,45,5,45,293,8,45,10,45,12,45,296,9,
        45,1,46,1,46,1,46,5,46,301,8,46,10,46,12,46,304,9,46,3,46,306,8,
        46,1,46,3,46,309,8,46,1,47,4,47,312,8,47,11,47,12,47,313,1,48,1,
        48,3,48,318,8,48,1,48,4,48,321,8,48,11,48,12,48,322,1,49,1,49,1,
        49,1,49,1,49,1,49,1,49,1,49,3,49,333,8,49,1,50,1,50,3,50,337,8,50,
        1,51,1,51,1,52,1,52,1,52,1,52,5,52,345,8,52,10,52,12,52,348,9,52,
        1,52,1,52,1,53,4,53,353,8,53,11,53,12,53,354,1,53,1,53,1,54,1,54,
        1,54,1,55,1,55,1,55,1,55,1,55,1,55,5,55,368,8,55,10,55,12,55,371,
        9,55,1,55,1,55,1,55,1,55,3,55,377,8,55,1,55,1,55,1,56,1,56,1,56,
        1,56,1,56,1,56,5,56,387,8,56,10,56,12,56,390,9,56,1,56,1,56,1,56,
        1,56,1,56,3,56,397,8,56,1,56,1,56,0,0,57,1,1,3,2,5,3,7,4,9,5,11,
        6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,
        35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,
        57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,
        79,40,81,41,83,42,85,43,87,44,89,45,91,46,93,47,95,0,97,0,99,48,
        101,49,103,50,105,51,107,52,109,53,111,54,113,55,1,0,12,3,0,65,90,
        95,95,97,122,4,0,48,57,65,90,95,95,97,122,1,0,48,57,2,0,69,69,101,
        101,2,0,43,43,45,45,5,0,10,10,12,13,34,34,39,39,92,92,7,0,39,39,
        92,92,98,98,102,102,110,110,114,114,116,116,1,0,10,10,2,0,10,10,
        12,13,3,0,8,9,12,13,32,32,2,0,12,13,39,39,1,0,34,34,419,0,1,1,0,
        0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,
        0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,
        0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,
        0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,
        0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,
        0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,
        0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,
        0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,
        0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,
        0,93,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,0,
        0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,1,115,
        1,0,0,0,3,121,1,0,0,0,5,126,1,0,0,0,7,132,1,0,0,0,9,139,1,0,0,0,
        11,144,1,0,0,0,13,151,1,0,0,0,15,158,1,0,0,0,17,162,1,0,0,0,19,170,
        1,0,0,0,21,175,1,0,0,0,23,179,1,0,0,0,25,185,1,0,0,0,27,188,1,0,
        0,0,29,194,1,0,0,0,31,203,1,0,0,0,33,206,1,0,0,0,35,211,1,0,0,0,
        37,216,1,0,0,0,39,222,1,0,0,0,41,226,1,0,0,0,43,230,1,0,0,0,45,234,
        1,0,0,0,47,237,1,0,0,0,49,240,1,0,0,0,51,242,1,0,0,0,53,244,1,0,
        0,0,55,246,1,0,0,0,57,248,1,0,0,0,59,250,1,0,0,0,61,252,1,0,0,0,
        63,255,1,0,0,0,65,258,1,0,0,0,67,260,1,0,0,0,69,263,1,0,0,0,71,265,
        1,0,0,0,73,268,1,0,0,0,75,270,1,0,0,0,77,273,1,0,0,0,79,277,1,0,
        0,0,81,280,1,0,0,0,83,282,1,0,0,0,85,284,1,0,0,0,87,286,1,0,0,0,
        89,288,1,0,0,0,91,290,1,0,0,0,93,297,1,0,0,0,95,311,1,0,0,0,97,315,
        1,0,0,0,99,332,1,0,0,0,101,336,1,0,0,0,103,338,1,0,0,0,105,340,1,
        0,0,0,107,352,1,0,0,0,109,358,1,0,0,0,111,361,1,0,0,0,113,380,1,
        0,0,0,115,116,5,97,0,0,116,117,5,114,0,0,117,118,5,114,0,0,118,119,
        5,97,0,0,119,120,5,121,0,0,120,2,1,0,0,0,121,122,5,116,0,0,122,123,
        5,114,0,0,123,124,5,117,0,0,124,125,5,101,0,0,125,4,1,0,0,0,126,
        127,5,102,0,0,127,128,5,97,0,0,128,129,5,108,0,0,129,130,5,115,0,
        0,130,131,5,101,0,0,131,6,1,0,0,0,132,133,5,110,0,0,133,134,5,117,
        0,0,134,135,5,109,0,0,135,136,5,98,0,0,136,137,5,101,0,0,137,138,
        5,114,0,0,138,8,1,0,0,0,139,140,5,98,0,0,140,141,5,111,0,0,141,142,
        5,111,0,0,142,143,5,108,0,0,143,10,1,0,0,0,144,145,5,115,0,0,145,
        146,5,116,0,0,146,147,5,114,0,0,147,148,5,105,0,0,148,149,5,110,
        0,0,149,150,5,103,0,0,150,12,1,0,0,0,151,152,5,114,0,0,152,153,5,
        101,0,0,153,154,5,116,0,0,154,155,5,117,0,0,155,156,5,114,0,0,156,
        157,5,110,0,0,157,14,1,0,0,0,158,159,5,118,0,0,159,160,5,97,0,0,
        160,161,5,114,0,0,161,16,1,0,0,0,162,163,5,100,0,0,163,164,5,121,
        0,0,164,165,5,110,0,0,165,166,5,97,0,0,166,167,5,109,0,0,167,168,
        5,105,0,0,168,169,5,99,0,0,169,18,1,0,0,0,170,171,5,102,0,0,171,
        172,5,117,0,0,172,173,5,110,0,0,173,174,5,99,0,0,174,20,1,0,0,0,
        175,176,5,102,0,0,176,177,5,111,0,0,177,178,5,114,0,0,178,22,1,0,
        0,0,179,180,5,117,0,0,180,181,5,110,0,0,181,182,5,116,0,0,182,183,
        5,105,0,0,183,184,5,108,0,0,184,24,1,0,0,0,185,186,5,98,0,0,186,
        187,5,121,0,0,187,26,1,0,0,0,188,189,5,98,0,0,189,190,5,114,0,0,
        190,191,5,101,0,0,191,192,5,97,0,0,192,193,5,107,0,0,193,28,1,0,
        0,0,194,195,5,99,0,0,195,196,5,111,0,0,196,197,5,110,0,0,197,198,
        5,116,0,0,198,199,5,105,0,0,199,200,5,110,0,0,200,201,5,117,0,0,
        201,202,5,101,0,0,202,30,1,0,0,0,203,204,5,105,0,0,204,205,5,102,
        0,0,205,32,1,0,0,0,206,207,5,101,0,0,207,208,5,108,0,0,208,209,5,
        115,0,0,209,210,5,101,0,0,210,34,1,0,0,0,211,212,5,101,0,0,212,213,
        5,108,0,0,213,214,5,105,0,0,214,215,5,102,0,0,215,36,1,0,0,0,216,
        217,5,98,0,0,217,218,5,101,0,0,218,219,5,103,0,0,219,220,5,105,0,
        0,220,221,5,110,0,0,221,38,1,0,0,0,222,223,5,101,0,0,223,224,5,110,
        0,0,224,225,5,100,0,0,225,40,1,0,0,0,226,227,5,110,0,0,227,228,5,
        111,0,0,228,229,5,116,0,0,229,42,1,0,0,0,230,231,5,97,0,0,231,232,
        5,110,0,0,232,233,5,100,0,0,233,44,1,0,0,0,234,235,5,111,0,0,235,
        236,5,114,0,0,236,46,1,0,0,0,237,238,5,60,0,0,238,239,5,45,0,0,239,
        48,1,0,0,0,240,241,5,43,0,0,241,50,1,0,0,0,242,243,5,45,0,0,243,
        52,1,0,0,0,244,245,5,42,0,0,245,54,1,0,0,0,246,247,5,47,0,0,247,
        56,1,0,0,0,248,249,5,37,0,0,249,58,1,0,0,0,250,251,5,33,0,0,251,
        60,1,0,0,0,252,253,5,38,0,0,253,254,5,38,0,0,254,62,1,0,0,0,255,
        256,5,124,0,0,256,257,5,124,0,0,257,64,1,0,0,0,258,259,5,61,0,0,
        259,66,1,0,0,0,260,261,5,33,0,0,261,262,5,61,0,0,262,68,1,0,0,0,
        263,264,5,60,0,0,264,70,1,0,0,0,265,266,5,60,0,0,266,267,5,61,0,
        0,267,72,1,0,0,0,268,269,5,62,0,0,269,74,1,0,0,0,270,271,5,62,0,
        0,271,272,5,61,0,0,272,76,1,0,0,0,273,274,5,46,0,0,274,275,5,46,
        0,0,275,276,5,46,0,0,276,78,1,0,0,0,277,278,5,61,0,0,278,279,5,61,
        0,0,279,80,1,0,0,0,280,281,5,91,0,0,281,82,1,0,0,0,282,283,5,93,
        0,0,283,84,1,0,0,0,284,285,5,40,0,0,285,86,1,0,0,0,286,287,5,41,
        0,0,287,88,1,0,0,0,288,289,5,44,0,0,289,90,1,0,0,0,290,294,7,0,0,
        0,291,293,7,1,0,0,292,291,1,0,0,0,293,296,1,0,0,0,294,292,1,0,0,
        0,294,295,1,0,0,0,295,92,1,0,0,0,296,294,1,0,0,0,297,305,3,95,47,
        0,298,302,5,46,0,0,299,301,3,95,47,0,300,299,1,0,0,0,301,304,1,0,
        0,0,302,300,1,0,0,0,302,303,1,0,0,0,303,306,1,0,0,0,304,302,1,0,
        0,0,305,298,1,0,0,0,305,306,1,0,0,0,306,308,1,0,0,0,307,309,3,97,
        48,0,308,307,1,0,0,0,308,309,1,0,0,0,309,94,1,0,0,0,310,312,7,2,
        0,0,311,310,1,0,0,0,312,313,1,0,0,0,313,311,1,0,0,0,313,314,1,0,
        0,0,314,96,1,0,0,0,315,317,7,3,0,0,316,318,7,4,0,0,317,316,1,0,0,
        0,317,318,1,0,0,0,318,320,1,0,0,0,319,321,7,2,0,0,320,319,1,0,0,
        0,321,322,1,0,0,0,322,320,1,0,0,0,322,323,1,0,0,0,323,98,1,0,0,0,
        324,325,5,34,0,0,325,333,8,5,0,0,326,327,5,92,0,0,327,333,7,6,0,
        0,328,329,5,39,0,0,329,330,5,34,0,0,330,331,1,0,0,0,331,333,6,49,
        0,0,332,324,1,0,0,0,332,326,1,0,0,0,332,328,1,0,0,0,333,100,1,0,
        0,0,334,337,3,3,1,0,335,337,3,5,2,0,336,334,1,0,0,0,336,335,1,0,
        0,0,337,102,1,0,0,0,338,339,7,7,0,0,339,104,1,0,0,0,340,341,5,35,
        0,0,341,342,5,35,0,0,342,346,1,0,0,0,343,345,8,8,0,0,344,343,1,0,
        0,0,345,348,1,0,0,0,346,344,1,0,0,0,346,347,1,0,0,0,347,349,1,0,
        0,0,348,346,1,0,0,0,349,350,6,52,1,0,350,106,1,0,0,0,351,353,7,9,
        0,0,352,351,1,0,0,0,353,354,1,0,0,0,354,352,1,0,0,0,354,355,1,0,
        0,0,355,356,1,0,0,0,356,357,6,53,1,0,357,108,1,0,0,0,358,359,9,0,
        0,0,359,360,6,54,2,0,360,110,1,0,0,0,361,369,5,34,0,0,362,368,8,
        5,0,0,363,364,5,92,0,0,364,368,7,6,0,0,365,366,5,39,0,0,366,368,
        5,34,0,0,367,362,1,0,0,0,367,363,1,0,0,0,367,365,1,0,0,0,368,371,
        1,0,0,0,369,367,1,0,0,0,369,370,1,0,0,0,370,376,1,0,0,0,371,369,
        1,0,0,0,372,377,5,0,0,1,373,374,5,13,0,0,374,377,5,10,0,0,375,377,
        5,10,0,0,376,372,1,0,0,0,376,373,1,0,0,0,376,375,1,0,0,0,377,378,
        1,0,0,0,378,379,6,55,3,0,379,112,1,0,0,0,380,388,5,34,0,0,381,387,
        8,5,0,0,382,383,5,92,0,0,383,387,7,6,0,0,384,385,5,39,0,0,385,387,
        5,34,0,0,386,381,1,0,0,0,386,382,1,0,0,0,386,384,1,0,0,0,387,390,
        1,0,0,0,388,386,1,0,0,0,388,389,1,0,0,0,389,396,1,0,0,0,390,388,
        1,0,0,0,391,397,7,10,0,0,392,393,5,92,0,0,393,397,8,6,0,0,394,395,
        5,39,0,0,395,397,8,11,0,0,396,391,1,0,0,0,396,392,1,0,0,0,396,394,
        1,0,0,0,397,398,1,0,0,0,398,399,6,56,4,0,399,114,1,0,0,0,18,0,294,
        302,305,308,313,317,322,332,336,346,354,367,369,376,386,388,396,
        5,1,49,0,6,0,0,1,54,1,1,55,2,1,56,3
    ]

class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    TRUE = 2
    FALSE = 3
    NUMBER = 4
    BOOL = 5
    STRING = 6
    RETURN = 7
    VAR = 8
    DYNAMIC = 9
    FUNC = 10
    FOR = 11
    UNTIL = 12
    BY = 13
    BREAK = 14
    CONTINUE = 15
    IF = 16
    ELSE = 17
    ELIF = 18
    BEGIN = 19
    END = 20
    NOT = 21
    AND = 22
    OR = 23
    ASSIGNINIT = 24
    ADD = 25
    SUB = 26
    MUL = 27
    DIV = 28
    MODUL = 29
    NOT_OP = 30
    AND_OP = 31
    OR_OP = 32
    ASSIGN = 33
    NOT_EQUAL = 34
    LESS_THAN = 35
    LESS_OR_EQUAL = 36
    GREATER_THAN = 37
    GREATER_OR_EQUAL = 38
    CONCAT = 39
    EQUAL = 40
    LBRACKET = 41
    RBRACKET = 42
    LPAREN = 43
    RPAREN = 44
    COMMA = 45
    ID = 46
    NUMBER_LIT = 47
    STRING_LIT = 48
    BOOLEAN_LIT = 49
    NEWLINE = 50
    COMMENTS = 51
    WS = 52
    ERROR_CHAR = 53
    UNCLOSE_STRING = 54
    ILLEGAL_ESCAPE = 55

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'array'", "'true'", "'false'", "'number'", "'bool'", "'string'", 
            "'return'", "'var'", "'dynamic'", "'func'", "'for'", "'until'", 
            "'by'", "'break'", "'continue'", "'if'", "'else'", "'elif'", 
            "'begin'", "'end'", "'not'", "'and'", "'or'", "'<-'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", "'['", "']'", 
            "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ASSIGNINIT", 
            "ADD", "SUB", "MUL", "DIV", "MODUL", "NOT_OP", "AND_OP", "OR_OP", 
            "ASSIGN", "NOT_EQUAL", "LESS_THAN", "LESS_OR_EQUAL", "GREATER_THAN", 
            "GREATER_OR_EQUAL", "CONCAT", "EQUAL", "LBRACKET", "RBRACKET", 
            "LPAREN", "RPAREN", "COMMA", "ID", "NUMBER_LIT", "STRING_LIT", 
            "BOOLEAN_LIT", "NEWLINE", "COMMENTS", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "ASSIGNINIT", "ADD", "SUB", "MUL", "DIV", 
                  "MODUL", "NOT_OP", "AND_OP", "OR_OP", "ASSIGN", "NOT_EQUAL", 
                  "LESS_THAN", "LESS_OR_EQUAL", "GREATER_THAN", "GREATER_OR_EQUAL", 
                  "CONCAT", "EQUAL", "LBRACKET", "RBRACKET", "LPAREN", "RPAREN", 
                  "COMMA", "ID", "NUMBER_LIT", "INT", "EXP", "STRING_LIT", 
                  "BOOLEAN_LIT", "NEWLINE", "COMMENTS", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[49] = self.STRING_LIT_action 
            actions[54] = self.ERROR_CHAR_action 
            actions[55] = self.UNCLOSE_STRING_action 
            actions[56] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1];
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
            			raise UncloseString(self.text[1:-2])
            		elif(self.text[-1] == '\n'):
            			raise UncloseString(self.text[1:-1])
            		else:
            			raise UncloseString(slef.text[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text[1:]);
     

