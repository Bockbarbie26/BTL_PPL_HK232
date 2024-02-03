# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\38")
        buf.write("\u015e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\3\2\7\2P\n\2\f\2\16\2S\13\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\5\3\\\n\3\3\4\3\4\3\4\3\4\5\4b\n\4\3\5\3")
        buf.write("\5\3\5\5\5g\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\5")
        buf.write("\7r\n\7\3\b\3\b\3\b\3\b\3\b\3\b\5\bz\n\b\3\b\3\b\5\b~")
        buf.write("\n\b\3\t\3\t\3\t\3\t\5\t\u0084\n\t\3\n\3\n\3\n\3\n\5\n")
        buf.write("\u008a\n\n\3\n\3\n\5\n\u008e\n\n\3\n\3\n\5\n\u0092\n\n")
        buf.write("\3\n\3\n\5\n\u0096\n\n\3\13\3\13\5\13\u009a\n\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\5\f\u00a1\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u00a8")
        buf.write("\n\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u00b0\n\16\f\16")
        buf.write("\16\16\u00b3\13\16\3\17\3\17\3\17\3\17\3\17\3\17\7\17")
        buf.write("\u00bb\n\17\f\17\16\17\u00be\13\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\7\20\u00c6\n\20\f\20\16\20\u00c9\13\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\7\21\u00d1\n\21\f\21\16\21\u00d4")
        buf.write("\13\21\3\22\3\22\3\22\5\22\u00d9\n\22\3\23\3\23\3\23\5")
        buf.write("\23\u00de\n\23\3\24\3\24\5\24\u00e2\n\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\5\24\u00e9\n\24\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\5\25\u00f2\n\25\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\5\27\u00fe\n\27\3\30\3\30\3\30\3")
        buf.write("\30\3\31\3\31\3\31\3\31\5\31\u0108\n\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0113\n\32\3\33\3")
        buf.write("\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\5\35\u011f")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u0127\n\36\f")
        buf.write("\36\16\36\u012a\13\36\3\36\5\36\u012d\n\36\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\5!\u013f")
        buf.write("\n!\3!\3!\3\"\5\"\u0144\n\"\3\"\3\"\3#\5#\u0149\n#\3#")
        buf.write("\3#\3$\3$\5$\u014f\n$\3%\3%\3&\3&\3&\3&\3&\3&\3\'\6\'")
        buf.write("\u015a\n\'\r\'\16\'\u015b\3\'\2\6\32\34\36 (\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJL\2\b\3\2\5\7\4\2\"\'))\3\2\27\30\3\2\32\33\3\2")
        buf.write("\34\36\3\2\63\64\2\u0168\2Q\3\2\2\2\4[\3\2\2\2\6a\3\2")
        buf.write("\2\2\bf\3\2\2\2\nh\3\2\2\2\fm\3\2\2\2\16s\3\2\2\2\20\u0083")
        buf.write("\3\2\2\2\22\u0085\3\2\2\2\24\u0099\3\2\2\2\26\u00a0\3")
        buf.write("\2\2\2\30\u00a7\3\2\2\2\32\u00a9\3\2\2\2\34\u00b4\3\2")
        buf.write("\2\2\36\u00bf\3\2\2\2 \u00ca\3\2\2\2\"\u00d8\3\2\2\2$")
        buf.write("\u00dd\3\2\2\2&\u00e8\3\2\2\2(\u00f1\3\2\2\2*\u00f3\3")
        buf.write("\2\2\2,\u00fd\3\2\2\2.\u00ff\3\2\2\2\60\u0107\3\2\2\2")
        buf.write("\62\u0112\3\2\2\2\64\u0114\3\2\2\2\66\u0117\3\2\2\28\u011e")
        buf.write("\3\2\2\2:\u0120\3\2\2\2<\u012e\3\2\2\2>\u0134\3\2\2\2")
        buf.write("@\u0137\3\2\2\2B\u0143\3\2\2\2D\u0148\3\2\2\2F\u014c\3")
        buf.write("\2\2\2H\u0150\3\2\2\2J\u0152\3\2\2\2L\u0159\3\2\2\2NP")
        buf.write("\7\63\2\2ON\3\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3\2\2\2RT\3")
        buf.write("\2\2\2SQ\3\2\2\2TU\5\4\3\2UV\7\2\2\3V\3\3\2\2\2WX\5\6")
        buf.write("\4\2XY\5\4\3\2Y\\\3\2\2\2Z\\\5\6\4\2[W\3\2\2\2[Z\3\2\2")
        buf.write("\2\\\5\3\2\2\2]b\5\22\n\2^_\5\b\5\2_`\5L\'\2`b\3\2\2\2")
        buf.write("a]\3\2\2\2a^\3\2\2\2b\7\3\2\2\2cg\5\n\6\2dg\5\f\7\2eg")
        buf.write("\5\16\b\2fc\3\2\2\2fd\3\2\2\2fe\3\2\2\2g\t\3\2\2\2hi\7")
        buf.write("\t\2\2ij\7/\2\2jk\7\31\2\2kl\5\30\r\2l\13\3\2\2\2mn\7")
        buf.write("\n\2\2nq\7/\2\2op\7\31\2\2pr\5\30\r\2qo\3\2\2\2qr\3\2")
        buf.write("\2\2r\r\3\2\2\2st\t\2\2\2ty\7/\2\2uv\7*\2\2vw\5\20\t\2")
        buf.write("wx\7+\2\2xz\3\2\2\2yu\3\2\2\2yz\3\2\2\2z}\3\2\2\2{|\7")
        buf.write("\31\2\2|~\5\30\r\2}{\3\2\2\2}~\3\2\2\2~\17\3\2\2\2\177")
        buf.write("\u0080\7\60\2\2\u0080\u0081\7.\2\2\u0081\u0084\5\20\t")
        buf.write("\2\u0082\u0084\7\60\2\2\u0083\177\3\2\2\2\u0083\u0082")
        buf.write("\3\2\2\2\u0084\21\3\2\2\2\u0085\u0086\7\13\2\2\u0086\u0087")
        buf.write("\7/\2\2\u0087\u0089\7,\2\2\u0088\u008a\5\24\13\2\u0089")
        buf.write("\u0088\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008b\3\2\2\2")
        buf.write("\u008b\u0095\7-\2\2\u008c\u008e\5L\'\2\u008d\u008c\3\2")
        buf.write("\2\2\u008d\u008e\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0096")
        buf.write("\5F$\2\u0090\u0092\5L\'\2\u0091\u0090\3\2\2\2\u0091\u0092")
        buf.write("\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0096\5J&\2\u0094\u0096")
        buf.write("\5L\'\2\u0095\u008d\3\2\2\2\u0095\u0091\3\2\2\2\u0095")
        buf.write("\u0094\3\2\2\2\u0096\23\3\2\2\2\u0097\u009a\5\26\f\2\u0098")
        buf.write("\u009a\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u0098\3\2\2\2")
        buf.write("\u009a\25\3\2\2\2\u009b\u009c\5\30\r\2\u009c\u009d\7.")
        buf.write("\2\2\u009d\u009e\5\26\f\2\u009e\u00a1\3\2\2\2\u009f\u00a1")
        buf.write("\5\30\r\2\u00a0\u009b\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1")
        buf.write("\27\3\2\2\2\u00a2\u00a3\5\32\16\2\u00a3\u00a4\7(\2\2\u00a4")
        buf.write("\u00a5\5\32\16\2\u00a5\u00a8\3\2\2\2\u00a6\u00a8\5\32")
        buf.write("\16\2\u00a7\u00a2\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\31")
        buf.write("\3\2\2\2\u00a9\u00aa\b\16\1\2\u00aa\u00ab\5\34\17\2\u00ab")
        buf.write("\u00b1\3\2\2\2\u00ac\u00ad\f\4\2\2\u00ad\u00ae\t\3\2\2")
        buf.write("\u00ae\u00b0\5\32\16\5\u00af\u00ac\3\2\2\2\u00b0\u00b3")
        buf.write("\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2")
        buf.write("\33\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b5\b\17\1\2\u00b5")
        buf.write("\u00b6\5\36\20\2\u00b6\u00bc\3\2\2\2\u00b7\u00b8\f\4\2")
        buf.write("\2\u00b8\u00b9\t\4\2\2\u00b9\u00bb\5\36\20\2\u00ba\u00b7")
        buf.write("\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc")
        buf.write("\u00bd\3\2\2\2\u00bd\35\3\2\2\2\u00be\u00bc\3\2\2\2\u00bf")
        buf.write("\u00c0\b\20\1\2\u00c0\u00c1\5 \21\2\u00c1\u00c7\3\2\2")
        buf.write("\2\u00c2\u00c3\f\4\2\2\u00c3\u00c4\t\5\2\2\u00c4\u00c6")
        buf.write("\5 \21\2\u00c5\u00c2\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7")
        buf.write("\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\37\3\2\2\2\u00c9")
        buf.write("\u00c7\3\2\2\2\u00ca\u00cb\b\21\1\2\u00cb\u00cc\5\"\22")
        buf.write("\2\u00cc\u00d2\3\2\2\2\u00cd\u00ce\f\4\2\2\u00ce\u00cf")
        buf.write("\t\6\2\2\u00cf\u00d1\5\"\22\2\u00d0\u00cd\3\2\2\2\u00d1")
        buf.write("\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2")
        buf.write("\u00d3!\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5\u00d6\7\26\2")
        buf.write("\2\u00d6\u00d9\5\"\22\2\u00d7\u00d9\5$\23\2\u00d8\u00d5")
        buf.write("\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9#\3\2\2\2\u00da\u00db")
        buf.write("\t\5\2\2\u00db\u00de\5$\23\2\u00dc\u00de\5&\24\2\u00dd")
        buf.write("\u00da\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de%\3\2\2\2\u00df")
        buf.write("\u00e2\7/\2\2\u00e0\u00e2\5*\26\2\u00e1\u00df\3\2\2\2")
        buf.write("\u00e1\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\7")
        buf.write("*\2\2\u00e4\u00e5\5\26\f\2\u00e5\u00e6\7+\2\2\u00e6\u00e9")
        buf.write("\3\2\2\2\u00e7\u00e9\5(\25\2\u00e8\u00e1\3\2\2\2\u00e8")
        buf.write("\u00e7\3\2\2\2\u00e9\'\3\2\2\2\u00ea\u00f2\7/\2\2\u00eb")
        buf.write("\u00f2\5,\27\2\u00ec\u00ed\7,\2\2\u00ed\u00ee\5\30\r\2")
        buf.write("\u00ee\u00ef\7-\2\2\u00ef\u00f2\3\2\2\2\u00f0\u00f2\5")
        buf.write("*\26\2\u00f1\u00ea\3\2\2\2\u00f1\u00eb\3\2\2\2\u00f1\u00ec")
        buf.write("\3\2\2\2\u00f1\u00f0\3\2\2\2\u00f2)\3\2\2\2\u00f3\u00f4")
        buf.write("\7/\2\2\u00f4\u00f5\7,\2\2\u00f5\u00f6\5\26\f\2\u00f6")
        buf.write("\u00f7\7-\2\2\u00f7+\3\2\2\2\u00f8\u00fe\7\60\2\2\u00f9")
        buf.write("\u00fe\7\61\2\2\u00fa\u00fe\7\3\2\2\u00fb\u00fe\7\4\2")
        buf.write("\2\u00fc\u00fe\5.\30\2\u00fd\u00f8\3\2\2\2\u00fd\u00f9")
        buf.write("\3\2\2\2\u00fd\u00fa\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd")
        buf.write("\u00fc\3\2\2\2\u00fe-\3\2\2\2\u00ff\u0100\7*\2\2\u0100")
        buf.write("\u0101\5\26\f\2\u0101\u0102\7+\2\2\u0102/\3\2\2\2\u0103")
        buf.write("\u0104\5\62\32\2\u0104\u0105\5\60\31\2\u0105\u0108\3\2")
        buf.write("\2\2\u0106\u0108\3\2\2\2\u0107\u0103\3\2\2\2\u0107\u0106")
        buf.write("\3\2\2\2\u0108\61\3\2\2\2\u0109\u0113\5\64\33\2\u010a")
        buf.write("\u0113\5\66\34\2\u010b\u0113\5:\36\2\u010c\u0113\5@!\2")
        buf.write("\u010d\u0113\5B\"\2\u010e\u0113\5D#\2\u010f\u0113\5F$")
        buf.write("\2\u0110\u0113\5H%\2\u0111\u0113\5J&\2\u0112\u0109\3\2")
        buf.write("\2\2\u0112\u010a\3\2\2\2\u0112\u010b\3\2\2\2\u0112\u010c")
        buf.write("\3\2\2\2\u0112\u010d\3\2\2\2\u0112\u010e\3\2\2\2\u0112")
        buf.write("\u010f\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0111\3\2\2\2")
        buf.write("\u0113\63\3\2\2\2\u0114\u0115\5\b\5\2\u0115\u0116\5L\'")
        buf.write("\2\u0116\65\3\2\2\2\u0117\u0118\58\35\2\u0118\u0119\7")
        buf.write("\31\2\2\u0119\u011a\5\30\r\2\u011a\u011b\5L\'\2\u011b")
        buf.write("\67\3\2\2\2\u011c\u011f\7/\2\2\u011d\u011f\5.\30\2\u011e")
        buf.write("\u011c\3\2\2\2\u011e\u011d\3\2\2\2\u011f9\3\2\2\2\u0120")
        buf.write("\u0121\7\21\2\2\u0121\u0122\7,\2\2\u0122\u0123\5\30\r")
        buf.write("\2\u0123\u0124\7-\2\2\u0124\u0128\5\62\32\2\u0125\u0127")
        buf.write("\5<\37\2\u0126\u0125\3\2\2\2\u0127\u012a\3\2\2\2\u0128")
        buf.write("\u0126\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012c\3\2\2\2")
        buf.write("\u012a\u0128\3\2\2\2\u012b\u012d\5> \2\u012c\u012b\3\2")
        buf.write("\2\2\u012c\u012d\3\2\2\2\u012d;\3\2\2\2\u012e\u012f\7")
        buf.write("\23\2\2\u012f\u0130\7,\2\2\u0130\u0131\5\30\r\2\u0131")
        buf.write("\u0132\7-\2\2\u0132\u0133\5\62\32\2\u0133=\3\2\2\2\u0134")
        buf.write("\u0135\7\22\2\2\u0135\u0136\5\62\32\2\u0136?\3\2\2\2\u0137")
        buf.write("\u0138\7\f\2\2\u0138\u0139\7/\2\2\u0139\u013a\7\r\2\2")
        buf.write("\u013a\u013b\5\30\r\2\u013b\u013c\7\16\2\2\u013c\u013e")
        buf.write("\5\30\r\2\u013d\u013f\5L\'\2\u013e\u013d\3\2\2\2\u013e")
        buf.write("\u013f\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0141\5\62\32")
        buf.write("\2\u0141A\3\2\2\2\u0142\u0144\5L\'\2\u0143\u0142\3\2\2")
        buf.write("\2\u0143\u0144\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0146")
        buf.write("\7\17\2\2\u0146C\3\2\2\2\u0147\u0149\5L\'\2\u0148\u0147")
        buf.write("\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014a\3\2\2\2\u014a")
        buf.write("\u014b\7\20\2\2\u014bE\3\2\2\2\u014c\u014e\7\b\2\2\u014d")
        buf.write("\u014f\5\30\r\2\u014e\u014d\3\2\2\2\u014e\u014f\3\2\2")
        buf.write("\2\u014fG\3\2\2\2\u0150\u0151\5*\26\2\u0151I\3\2\2\2\u0152")
        buf.write("\u0153\7\24\2\2\u0153\u0154\5L\'\2\u0154\u0155\5\60\31")
        buf.write("\2\u0155\u0156\7\25\2\2\u0156\u0157\5L\'\2\u0157K\3\2")
        buf.write("\2\2\u0158\u015a\t\7\2\2\u0159\u0158\3\2\2\2\u015a\u015b")
        buf.write("\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c")
        buf.write("M\3\2\2\2%Q[afqy}\u0083\u0089\u008d\u0091\u0095\u0099")
        buf.write("\u00a0\u00a7\u00b1\u00bc\u00c7\u00d2\u00d8\u00dd\u00e1")
        buf.write("\u00e8\u00f1\u00fd\u0107\u0112\u011e\u0128\u012c\u013e")
        buf.write("\u0143\u0148\u014e\u015b")
        return buf.getvalue()


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
    RULE_funcall = 20
    RULE_literal = 21
    RULE_array_literal = 22
    RULE_statement_list = 23
    RULE_statement = 24
    RULE_declaration_statement = 25
    RULE_assignment_statement = 26
    RULE_lhs = 27
    RULE_if_statement = 28
    RULE_elif_statement = 29
    RULE_else_statement = 30
    RULE_for_statement = 31
    RULE_break_statement = 32
    RULE_continue_statement = 33
    RULE_return_statement = 34
    RULE_call_statement = 35
    RULE_block_statement = 36
    RULE_ignore = 37

    ruleNames =  [ "program", "list_declared", "declared", "variables", 
                   "implicit_var", "implicit_dynamic", "keyword_var", "list_NUMBER_LIT", 
                   "function", "prameters_list", "list_expr", "expression", 
                   "expression1", "expression2", "expression3", "expression4", 
                   "expression5", "expression6", "expression7", "expression8", 
                   "funcall", "literal", "array_literal", "statement_list", 
                   "statement", "declaration_statement", "assignment_statement", 
                   "lhs", "if_statement", "elif_statement", "else_statement", 
                   "for_statement", "break_statement", "continue_statement", 
                   "return_statement", "call_statement", "block_statement", 
                   "ignore" ]

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
        self.checkVersion("4.9.2")
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 76
                self.match(ZCodeParser.NEWLINE)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
            self.list_declared()
            self.state = 83
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_declared" ):
                return visitor.visitList_declared(self)
            else:
                return visitor.visitChildren(self)




    def list_declared(self):

        localctx = ZCodeParser.List_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_list_declared)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.declared()
                self.state = 86
                self.list_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared" ):
                return visitor.visitDeclared(self)
            else:
                return visitor.visitChildren(self)




    def declared(self):

        localctx = ZCodeParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declared)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.function()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.variables()
                self.state = 93
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)




    def variables(self):

        localctx = ZCodeParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variables)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.implicit_var()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.implicit_dynamic()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 99
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_var" ):
                return visitor.visitImplicit_var(self)
            else:
                return visitor.visitChildren(self)




    def implicit_var(self):

        localctx = ZCodeParser.Implicit_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_implicit_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(ZCodeParser.VAR)
            self.state = 103
            self.match(ZCodeParser.ID)
            self.state = 104
            self.match(ZCodeParser.ASSIGNINIT)
            self.state = 105
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_dynamic" ):
                return visitor.visitImplicit_dynamic(self)
            else:
                return visitor.visitChildren(self)




    def implicit_dynamic(self):

        localctx = ZCodeParser.Implicit_dynamicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_implicit_dynamic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(ZCodeParser.DYNAMIC)
            self.state = 108
            self.match(ZCodeParser.ID)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGNINIT:
                self.state = 109
                self.match(ZCodeParser.ASSIGNINIT)
                self.state = 110
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword_var" ):
                return visitor.visitKeyword_var(self)
            else:
                return visitor.visitChildren(self)




    def keyword_var(self):

        localctx = ZCodeParser.Keyword_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_keyword_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 114
            self.match(ZCodeParser.ID)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LBRACKET:
                self.state = 115
                self.match(ZCodeParser.LBRACKET)
                self.state = 116
                self.list_NUMBER_LIT()
                self.state = 117
                self.match(ZCodeParser.RBRACKET)


            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGNINIT:
                self.state = 121
                self.match(ZCodeParser.ASSIGNINIT)
                self.state = 122
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_NUMBER_LIT" ):
                return visitor.visitList_NUMBER_LIT(self)
            else:
                return visitor.visitChildren(self)




    def list_NUMBER_LIT(self):

        localctx = ZCodeParser.List_NUMBER_LITContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_list_NUMBER_LIT)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.match(ZCodeParser.NUMBER_LIT)
                self.state = 126
                self.match(ZCodeParser.COMMA)
                self.state = 127
                self.list_NUMBER_LIT()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
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
            return ZCodeParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ZCodeParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(ZCodeParser.FUNC)
            self.state = 132
            self.match(ZCodeParser.ID)
            self.state = 133
            self.match(ZCodeParser.LPAREN)
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 134
                self.prameters_list()


            self.state = 137
            self.match(ZCodeParser.RPAREN)
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE or _la==ZCodeParser.COMMENTS:
                    self.state = 138
                    self.ignore()


                self.state = 141
                self.return_statement()
                pass

            elif la_ == 2:
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE or _la==ZCodeParser.COMMENTS:
                    self.state = 142
                    self.ignore()


                self.state = 145
                self.block_statement()
                pass

            elif la_ == 3:
                self.state = 146
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrameters_list" ):
                return visitor.visitPrameters_list(self)
            else:
                return visitor.visitChildren(self)




    def prameters_list(self):

        localctx = ZCodeParser.Prameters_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_prameters_list)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.ADD, ZCodeParser.SUB, ZCodeParser.LBRACKET, ZCodeParser.LPAREN, ZCodeParser.ID, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.list_expr()
                pass
            elif token in [ZCodeParser.RPAREN]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr" ):
                return visitor.visitList_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_expr(self):

        localctx = ZCodeParser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_expr)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.expression()
                self.state = 154
                self.match(ZCodeParser.COMMA)
                self.state = 155
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expression)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.expression1(0)
                self.state = 161
                self.match(ZCodeParser.CONCAT)
                self.state = 162
                self.expression1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)



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
            self.state = 168
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 175
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 170
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 171
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.ASSIGN) | (1 << ZCodeParser.NOT_EQUAL) | (1 << ZCodeParser.LESS_THAN) | (1 << ZCodeParser.LESS_OR_EQUAL) | (1 << ZCodeParser.GREATER_THAN) | (1 << ZCodeParser.GREATER_OR_EQUAL) | (1 << ZCodeParser.EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 172
                    self.expression1(3) 
                self.state = 177
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



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
            self.state = 179
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 181
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 182
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 183
                    self.expression3(0) 
                self.state = 188
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



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
            self.state = 190
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 197
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 192
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 193
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 194
                    self.expression4(0) 
                self.state = 199
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



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
            self.state = 201
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 208
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 203
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 204
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MODUL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 205
                    self.expression5() 
                self.state = 210
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = ZCodeParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expression5)
        try:
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(ZCodeParser.NOT)
                self.state = 212
                self.expression5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.ADD, ZCodeParser.SUB, ZCodeParser.LBRACKET, ZCodeParser.LPAREN, ZCodeParser.ID, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)




    def expression6(self):

        localctx = ZCodeParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expression6)
        self._la = 0 # Token type
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ADD, ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 217
                self.expression6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LBRACKET, ZCodeParser.LPAREN, ZCodeParser.ID, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
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


        def expression8(self):
            return self.getTypedRuleContext(ZCodeParser.Expression8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = ZCodeParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expression7)
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 221
                    self.match(ZCodeParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 222
                    self.funcall()
                    pass


                self.state = 225
                self.match(ZCodeParser.LBRACKET)
                self.state = 226
                self.list_expr()
                self.state = 227
                self.match(ZCodeParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.expression8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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

        def funcall(self):
            return self.getTypedRuleContext(ZCodeParser.FuncallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression8" ):
                return visitor.visitExpression8(self)
            else:
                return visitor.visitChildren(self)




    def expression8(self):

        localctx = ZCodeParser.Expression8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expression8)
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.match(ZCodeParser.LPAREN)
                self.state = 235
                self.expression()
                self.state = 236
                self.match(ZCodeParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 238
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

        def list_expr(self):
            return self.getTypedRuleContext(ZCodeParser.List_exprContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = ZCodeParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_funcall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(ZCodeParser.ID)
            self.state = 242
            self.match(ZCodeParser.LPAREN)
            self.state = 243
            self.list_expr()
            self.state = 244
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_literal)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(ZCodeParser.NUMBER_LIT)
                pass
            elif token in [ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.match(ZCodeParser.STRING_LIT)
                pass
            elif token in [ZCodeParser.TRUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.match(ZCodeParser.TRUE)
                pass
            elif token in [ZCodeParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 249
                self.match(ZCodeParser.FALSE)
                pass
            elif token in [ZCodeParser.LBRACKET]:
                self.enterOuterAlt(localctx, 5)
                self.state = 250
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = ZCodeParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(ZCodeParser.LBRACKET)
            self.state = 254
            self.list_expr()
            self.state = 255
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = ZCodeParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_statement_list)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.LBRACKET, ZCodeParser.ID, ZCodeParser.NEWLINE, ZCodeParser.COMMENTS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.statement()
                self.state = 258
                self.statement_list()
                pass
            elif token in [ZCodeParser.END]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_statement)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.declaration_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 265
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 266
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 267
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 268
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 269
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 270
                self.call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 271
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_statement" ):
                return visitor.visitDeclaration_statement(self)
            else:
                return visitor.visitChildren(self)




    def declaration_statement(self):

        localctx = ZCodeParser.Declaration_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_declaration_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.variables()
            self.state = 275
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.lhs()
            self.state = 278
            self.match(ZCodeParser.ASSIGNINIT)
            self.state = 279
            self.expression()
            self.state = 280
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_lhs)
        try:
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.match(ZCodeParser.ID)
                pass
            elif token in [ZCodeParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(ZCodeParser.IF)
            self.state = 287
            self.match(ZCodeParser.LPAREN)
            self.state = 288
            self.expression()
            self.state = 289
            self.match(ZCodeParser.RPAREN)
            self.state = 290
            self.statement()
            self.state = 294
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 291
                    self.elif_statement() 
                self.state = 296
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 297
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_statement" ):
                return visitor.visitElif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elif_statement(self):

        localctx = ZCodeParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(ZCodeParser.ELIF)
            self.state = 301
            self.match(ZCodeParser.LPAREN)
            self.state = 302
            self.expression()
            self.state = 303
            self.match(ZCodeParser.RPAREN)
            self.state = 304
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = ZCodeParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(ZCodeParser.ELSE)
            self.state = 307
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(ZCodeParser.FOR)
            self.state = 310
            self.match(ZCodeParser.ID)
            self.state = 311
            self.match(ZCodeParser.UNTIL)
            self.state = 312
            self.expression()
            self.state = 313
            self.match(ZCodeParser.BY)
            self.state = 314
            self.expression()
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 315
                self.ignore()


            self.state = 318
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_break_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE or _la==ZCodeParser.COMMENTS:
                self.state = 320
                self.ignore()


            self.state = 323
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_continue_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE or _la==ZCodeParser.COMMENTS:
                self.state = 325
                self.ignore()


            self.state = 328
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(ZCodeParser.RETURN)
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 331
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

        def funcall(self):
            return self.getTypedRuleContext(ZCodeParser.FuncallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = ZCodeParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.funcall()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = ZCodeParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(ZCodeParser.BEGIN)
            self.state = 337
            self.ignore()
            self.state = 338
            self.statement_list()
            self.state = 339
            self.match(ZCodeParser.END)
            self.state = 340
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore" ):
                return visitor.visitIgnore(self)
            else:
                return visitor.visitChildren(self)




    def ignore(self):

        localctx = ZCodeParser.IgnoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_ignore)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 342
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.NEWLINE or _la==ZCodeParser.COMMENTS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 345 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
         




