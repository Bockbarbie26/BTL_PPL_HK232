# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\29")
        buf.write("\u0192\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3")
        buf.write(")\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\7/\u0127\n")
        buf.write("/\f/\16/\u012a\13/\3\60\3\60\3\60\7\60\u012f\n\60\f\60")
        buf.write("\16\60\u0132\13\60\5\60\u0134\n\60\3\60\5\60\u0137\n\60")
        buf.write("\3\61\6\61\u013a\n\61\r\61\16\61\u013b\3\62\3\62\5\62")
        buf.write("\u0140\n\62\3\62\6\62\u0143\n\62\r\62\16\62\u0144\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u014f\n\63\3")
        buf.write("\64\3\64\5\64\u0153\n\64\3\65\3\65\3\66\3\66\3\66\3\66")
        buf.write("\7\66\u015b\n\66\f\66\16\66\u015e\13\66\3\66\3\66\3\67")
        buf.write("\6\67\u0163\n\67\r\67\16\67\u0164\3\67\3\67\38\38\38\3")
        buf.write("9\39\39\39\39\39\79\u0172\n9\f9\169\u0175\139\39\39\3")
        buf.write("9\39\59\u017b\n9\39\39\3:\3:\3:\3:\3:\3:\7:\u0185\n:\f")
        buf.write(":\16:\u0188\13:\3:\3:\3:\3:\3:\5:\u018f\n:\3:\3:\2\2;")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\60_\61a\2c\2e\62g\63i\64k\65m\66o\67q8")
        buf.write("s9\3\2\16\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4")
        buf.write("\2--//\7\2\f\f\16\17$$))^^\t\2))^^ddhhppttvv\3\2\f\f\4")
        buf.write("\2\f\f\16\17\5\2\n\13\16\17\"\"\4\2\16\17))\3\2$$\2\u01a5")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3")
        buf.write("\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\3u")
        buf.write("\3\2\2\2\5{\3\2\2\2\7\u0080\3\2\2\2\t\u0086\3\2\2\2\13")
        buf.write("\u008d\3\2\2\2\r\u0092\3\2\2\2\17\u0099\3\2\2\2\21\u00a0")
        buf.write("\3\2\2\2\23\u00a4\3\2\2\2\25\u00ac\3\2\2\2\27\u00b1\3")
        buf.write("\2\2\2\31\u00b5\3\2\2\2\33\u00bb\3\2\2\2\35\u00be\3\2")
        buf.write("\2\2\37\u00c4\3\2\2\2!\u00cd\3\2\2\2#\u00d0\3\2\2\2%\u00d5")
        buf.write("\3\2\2\2\'\u00da\3\2\2\2)\u00e0\3\2\2\2+\u00e4\3\2\2\2")
        buf.write("-\u00e8\3\2\2\2/\u00ec\3\2\2\2\61\u00ef\3\2\2\2\63\u00f2")
        buf.write("\3\2\2\2\65\u00f4\3\2\2\2\67\u00f6\3\2\2\29\u00f8\3\2")
        buf.write("\2\2;\u00fa\3\2\2\2=\u00fc\3\2\2\2?\u00fe\3\2\2\2A\u0101")
        buf.write("\3\2\2\2C\u0104\3\2\2\2E\u0106\3\2\2\2G\u0109\3\2\2\2")
        buf.write("I\u010b\3\2\2\2K\u010e\3\2\2\2M\u0110\3\2\2\2O\u0113\3")
        buf.write("\2\2\2Q\u0117\3\2\2\2S\u011a\3\2\2\2U\u011c\3\2\2\2W\u011e")
        buf.write("\3\2\2\2Y\u0120\3\2\2\2[\u0122\3\2\2\2]\u0124\3\2\2\2")
        buf.write("_\u012b\3\2\2\2a\u0139\3\2\2\2c\u013d\3\2\2\2e\u014e\3")
        buf.write("\2\2\2g\u0152\3\2\2\2i\u0154\3\2\2\2k\u0156\3\2\2\2m\u0162")
        buf.write("\3\2\2\2o\u0168\3\2\2\2q\u016b\3\2\2\2s\u017e\3\2\2\2")
        buf.write("uv\7c\2\2vw\7t\2\2wx\7t\2\2xy\7c\2\2yz\7{\2\2z\4\3\2\2")
        buf.write("\2{|\7v\2\2|}\7t\2\2}~\7w\2\2~\177\7g\2\2\177\6\3\2\2")
        buf.write("\2\u0080\u0081\7h\2\2\u0081\u0082\7c\2\2\u0082\u0083\7")
        buf.write("n\2\2\u0083\u0084\7u\2\2\u0084\u0085\7g\2\2\u0085\b\3")
        buf.write("\2\2\2\u0086\u0087\7p\2\2\u0087\u0088\7w\2\2\u0088\u0089")
        buf.write("\7o\2\2\u0089\u008a\7d\2\2\u008a\u008b\7g\2\2\u008b\u008c")
        buf.write("\7t\2\2\u008c\n\3\2\2\2\u008d\u008e\7d\2\2\u008e\u008f")
        buf.write("\7q\2\2\u008f\u0090\7q\2\2\u0090\u0091\7n\2\2\u0091\f")
        buf.write("\3\2\2\2\u0092\u0093\7u\2\2\u0093\u0094\7v\2\2\u0094\u0095")
        buf.write("\7t\2\2\u0095\u0096\7k\2\2\u0096\u0097\7p\2\2\u0097\u0098")
        buf.write("\7i\2\2\u0098\16\3\2\2\2\u0099\u009a\7t\2\2\u009a\u009b")
        buf.write("\7g\2\2\u009b\u009c\7v\2\2\u009c\u009d\7w\2\2\u009d\u009e")
        buf.write("\7t\2\2\u009e\u009f\7p\2\2\u009f\20\3\2\2\2\u00a0\u00a1")
        buf.write("\7x\2\2\u00a1\u00a2\7c\2\2\u00a2\u00a3\7t\2\2\u00a3\22")
        buf.write("\3\2\2\2\u00a4\u00a5\7f\2\2\u00a5\u00a6\7{\2\2\u00a6\u00a7")
        buf.write("\7p\2\2\u00a7\u00a8\7c\2\2\u00a8\u00a9\7o\2\2\u00a9\u00aa")
        buf.write("\7k\2\2\u00aa\u00ab\7e\2\2\u00ab\24\3\2\2\2\u00ac\u00ad")
        buf.write("\7h\2\2\u00ad\u00ae\7w\2\2\u00ae\u00af\7p\2\2\u00af\u00b0")
        buf.write("\7e\2\2\u00b0\26\3\2\2\2\u00b1\u00b2\7h\2\2\u00b2\u00b3")
        buf.write("\7q\2\2\u00b3\u00b4\7t\2\2\u00b4\30\3\2\2\2\u00b5\u00b6")
        buf.write("\7w\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8\7v\2\2\u00b8\u00b9")
        buf.write("\7k\2\2\u00b9\u00ba\7n\2\2\u00ba\32\3\2\2\2\u00bb\u00bc")
        buf.write("\7d\2\2\u00bc\u00bd\7{\2\2\u00bd\34\3\2\2\2\u00be\u00bf")
        buf.write("\7d\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2")
        buf.write("\7c\2\2\u00c2\u00c3\7m\2\2\u00c3\36\3\2\2\2\u00c4\u00c5")
        buf.write("\7e\2\2\u00c5\u00c6\7q\2\2\u00c6\u00c7\7p\2\2\u00c7\u00c8")
        buf.write("\7v\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb")
        buf.write("\7w\2\2\u00cb\u00cc\7g\2\2\u00cc \3\2\2\2\u00cd\u00ce")
        buf.write("\7k\2\2\u00ce\u00cf\7h\2\2\u00cf\"\3\2\2\2\u00d0\u00d1")
        buf.write("\7g\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3\7u\2\2\u00d3\u00d4")
        buf.write("\7g\2\2\u00d4$\3\2\2\2\u00d5\u00d6\7g\2\2\u00d6\u00d7")
        buf.write("\7n\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9\7h\2\2\u00d9&\3")
        buf.write("\2\2\2\u00da\u00db\7d\2\2\u00db\u00dc\7g\2\2\u00dc\u00dd")
        buf.write("\7i\2\2\u00dd\u00de\7k\2\2\u00de\u00df\7p\2\2\u00df(\3")
        buf.write("\2\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3")
        buf.write("\7f\2\2\u00e3*\3\2\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6")
        buf.write("\7q\2\2\u00e6\u00e7\7v\2\2\u00e7,\3\2\2\2\u00e8\u00e9")
        buf.write("\7c\2\2\u00e9\u00ea\7p\2\2\u00ea\u00eb\7f\2\2\u00eb.\3")
        buf.write("\2\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee\7t\2\2\u00ee\60")
        buf.write("\3\2\2\2\u00ef\u00f0\7>\2\2\u00f0\u00f1\7/\2\2\u00f1\62")
        buf.write("\3\2\2\2\u00f2\u00f3\7-\2\2\u00f3\64\3\2\2\2\u00f4\u00f5")
        buf.write("\7/\2\2\u00f5\66\3\2\2\2\u00f6\u00f7\7,\2\2\u00f78\3\2")
        buf.write("\2\2\u00f8\u00f9\7\61\2\2\u00f9:\3\2\2\2\u00fa\u00fb\7")
        buf.write("\'\2\2\u00fb<\3\2\2\2\u00fc\u00fd\7#\2\2\u00fd>\3\2\2")
        buf.write("\2\u00fe\u00ff\7(\2\2\u00ff\u0100\7(\2\2\u0100@\3\2\2")
        buf.write("\2\u0101\u0102\7~\2\2\u0102\u0103\7~\2\2\u0103B\3\2\2")
        buf.write("\2\u0104\u0105\7?\2\2\u0105D\3\2\2\2\u0106\u0107\7#\2")
        buf.write("\2\u0107\u0108\7?\2\2\u0108F\3\2\2\2\u0109\u010a\7>\2")
        buf.write("\2\u010aH\3\2\2\2\u010b\u010c\7>\2\2\u010c\u010d\7?\2")
        buf.write("\2\u010dJ\3\2\2\2\u010e\u010f\7@\2\2\u010fL\3\2\2\2\u0110")
        buf.write("\u0111\7@\2\2\u0111\u0112\7?\2\2\u0112N\3\2\2\2\u0113")
        buf.write("\u0114\7\60\2\2\u0114\u0115\7\60\2\2\u0115\u0116\7\60")
        buf.write("\2\2\u0116P\3\2\2\2\u0117\u0118\7?\2\2\u0118\u0119\7?")
        buf.write("\2\2\u0119R\3\2\2\2\u011a\u011b\7]\2\2\u011bT\3\2\2\2")
        buf.write("\u011c\u011d\7_\2\2\u011dV\3\2\2\2\u011e\u011f\7*\2\2")
        buf.write("\u011fX\3\2\2\2\u0120\u0121\7+\2\2\u0121Z\3\2\2\2\u0122")
        buf.write("\u0123\7.\2\2\u0123\\\3\2\2\2\u0124\u0128\t\2\2\2\u0125")
        buf.write("\u0127\t\3\2\2\u0126\u0125\3\2\2\2\u0127\u012a\3\2\2\2")
        buf.write("\u0128\u0126\3\2\2\2\u0128\u0129\3\2\2\2\u0129^\3\2\2")
        buf.write("\2\u012a\u0128\3\2\2\2\u012b\u0133\5a\61\2\u012c\u0130")
        buf.write("\7\60\2\2\u012d\u012f\5a\61\2\u012e\u012d\3\2\2\2\u012f")
        buf.write("\u0132\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u0131\3\2\2\2")
        buf.write("\u0131\u0134\3\2\2\2\u0132\u0130\3\2\2\2\u0133\u012c\3")
        buf.write("\2\2\2\u0133\u0134\3\2\2\2\u0134\u0136\3\2\2\2\u0135\u0137")
        buf.write("\5c\62\2\u0136\u0135\3\2\2\2\u0136\u0137\3\2\2\2\u0137")
        buf.write("`\3\2\2\2\u0138\u013a\t\4\2\2\u0139\u0138\3\2\2\2\u013a")
        buf.write("\u013b\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2")
        buf.write("\u013cb\3\2\2\2\u013d\u013f\t\5\2\2\u013e\u0140\t\6\2")
        buf.write("\2\u013f\u013e\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0142")
        buf.write("\3\2\2\2\u0141\u0143\t\4\2\2\u0142\u0141\3\2\2\2\u0143")
        buf.write("\u0144\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145\3\2\2\2")
        buf.write("\u0145d\3\2\2\2\u0146\u0147\7$\2\2\u0147\u014f\n\7\2\2")
        buf.write("\u0148\u0149\7^\2\2\u0149\u014f\t\b\2\2\u014a\u014b\7")
        buf.write(")\2\2\u014b\u014c\7$\2\2\u014c\u014d\3\2\2\2\u014d\u014f")
        buf.write("\b\63\2\2\u014e\u0146\3\2\2\2\u014e\u0148\3\2\2\2\u014e")
        buf.write("\u014a\3\2\2\2\u014ff\3\2\2\2\u0150\u0153\5\5\3\2\u0151")
        buf.write("\u0153\5\7\4\2\u0152\u0150\3\2\2\2\u0152\u0151\3\2\2\2")
        buf.write("\u0153h\3\2\2\2\u0154\u0155\t\t\2\2\u0155j\3\2\2\2\u0156")
        buf.write("\u0157\7%\2\2\u0157\u0158\7%\2\2\u0158\u015c\3\2\2\2\u0159")
        buf.write("\u015b\n\n\2\2\u015a\u0159\3\2\2\2\u015b\u015e\3\2\2\2")
        buf.write("\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015f\3")
        buf.write("\2\2\2\u015e\u015c\3\2\2\2\u015f\u0160\b\66\3\2\u0160")
        buf.write("l\3\2\2\2\u0161\u0163\t\13\2\2\u0162\u0161\3\2\2\2\u0163")
        buf.write("\u0164\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2")
        buf.write("\u0165\u0166\3\2\2\2\u0166\u0167\b\67\3\2\u0167n\3\2\2")
        buf.write("\2\u0168\u0169\13\2\2\2\u0169\u016a\b8\4\2\u016ap\3\2")
        buf.write("\2\2\u016b\u0173\7$\2\2\u016c\u0172\n\7\2\2\u016d\u016e")
        buf.write("\7^\2\2\u016e\u0172\t\b\2\2\u016f\u0170\7)\2\2\u0170\u0172")
        buf.write("\7$\2\2\u0171\u016c\3\2\2\2\u0171\u016d\3\2\2\2\u0171")
        buf.write("\u016f\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3\2\2\2")
        buf.write("\u0173\u0174\3\2\2\2\u0174\u017a\3\2\2\2\u0175\u0173\3")
        buf.write("\2\2\2\u0176\u017b\7\2\2\3\u0177\u0178\7\17\2\2\u0178")
        buf.write("\u017b\7\f\2\2\u0179\u017b\7\f\2\2\u017a\u0176\3\2\2\2")
        buf.write("\u017a\u0177\3\2\2\2\u017a\u0179\3\2\2\2\u017b\u017c\3")
        buf.write("\2\2\2\u017c\u017d\b9\5\2\u017dr\3\2\2\2\u017e\u0186\7")
        buf.write("$\2\2\u017f\u0185\n\7\2\2\u0180\u0181\7^\2\2\u0181\u0185")
        buf.write("\t\b\2\2\u0182\u0183\7)\2\2\u0183\u0185\7$\2\2\u0184\u017f")
        buf.write("\3\2\2\2\u0184\u0180\3\2\2\2\u0184\u0182\3\2\2\2\u0185")
        buf.write("\u0188\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2")
        buf.write("\u0187\u018e\3\2\2\2\u0188\u0186\3\2\2\2\u0189\u018f\t")
        buf.write("\f\2\2\u018a\u018b\7^\2\2\u018b\u018f\n\b\2\2\u018c\u018d")
        buf.write("\7)\2\2\u018d\u018f\n\r\2\2\u018e\u0189\3\2\2\2\u018e")
        buf.write("\u018a\3\2\2\2\u018e\u018c\3\2\2\2\u018f\u0190\3\2\2\2")
        buf.write("\u0190\u0191\b:\6\2\u0191t\3\2\2\2\24\2\u0128\u0130\u0133")
        buf.write("\u0136\u013b\u013f\u0144\u014e\u0152\u015c\u0164\u0171")
        buf.write("\u0173\u017a\u0184\u0186\u018e\7\3\63\2\b\2\2\38\3\39")
        buf.write("\4\3:\5")
        return buf.getvalue()


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
        self.checkVersion("4.9.2")
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
     


