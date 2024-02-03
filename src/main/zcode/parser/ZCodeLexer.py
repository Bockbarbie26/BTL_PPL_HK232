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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\28")
        buf.write("\u018c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%")
        buf.write("\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write(",\3,\3-\3-\3.\3.\7.\u011f\n.\f.\16.\u0122\13.\3/\3/\3")
        buf.write("/\7/\u0127\n/\f/\16/\u012a\13/\5/\u012c\n/\3/\5/\u012f")
        buf.write("\n/\3\60\6\60\u0132\n\60\r\60\16\60\u0133\3\61\3\61\5")
        buf.write("\61\u0138\n\61\3\61\6\61\u013b\n\61\r\61\16\61\u013c\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\7\62\u0145\n\62\f\62\16\62")
        buf.write("\u0148\13\62\3\62\3\62\3\62\3\63\3\63\5\63\u014f\n\63")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\65\7\65\u0157\n\65\f\65\16")
        buf.write("\65\u015a\13\65\3\65\3\65\3\66\6\66\u015f\n\66\r\66\16")
        buf.write("\66\u0160\3\66\3\66\3\67\3\67\3\67\38\38\38\38\38\38\7")
        buf.write("8\u016e\n8\f8\168\u0171\138\38\38\38\38\58\u0177\n8\3")
        buf.write("8\38\39\39\39\39\39\39\79\u0181\n9\f9\169\u0184\139\3")
        buf.write("9\39\39\59\u0189\n9\39\39\2\2:\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\2a")
        buf.write("\2c\61e\62g\63i\64k\65m\66o\67q8\3\2\r\5\2C\\aac|\6\2")
        buf.write("\62;C\\aac|\3\2\62;\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^")
        buf.write("\t\2))^^ddhhppttvv\3\2\f\f\4\2\f\f\17\17\5\2\n\13\16\17")
        buf.write("\"\"\3\2\17\17\2\u019f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g")
        buf.write("\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2")
        buf.write("q\3\2\2\2\3s\3\2\2\2\5x\3\2\2\2\7~\3\2\2\2\t\u0085\3\2")
        buf.write("\2\2\13\u008a\3\2\2\2\r\u0091\3\2\2\2\17\u0098\3\2\2\2")
        buf.write("\21\u009c\3\2\2\2\23\u00a4\3\2\2\2\25\u00a9\3\2\2\2\27")
        buf.write("\u00ad\3\2\2\2\31\u00b3\3\2\2\2\33\u00b6\3\2\2\2\35\u00bc")
        buf.write("\3\2\2\2\37\u00c5\3\2\2\2!\u00c8\3\2\2\2#\u00cd\3\2\2")
        buf.write("\2%\u00d2\3\2\2\2\'\u00d8\3\2\2\2)\u00dc\3\2\2\2+\u00e0")
        buf.write("\3\2\2\2-\u00e4\3\2\2\2/\u00e7\3\2\2\2\61\u00ea\3\2\2")
        buf.write("\2\63\u00ec\3\2\2\2\65\u00ee\3\2\2\2\67\u00f0\3\2\2\2")
        buf.write("9\u00f2\3\2\2\2;\u00f4\3\2\2\2=\u00f6\3\2\2\2?\u00f9\3")
        buf.write("\2\2\2A\u00fc\3\2\2\2C\u00fe\3\2\2\2E\u0101\3\2\2\2G\u0103")
        buf.write("\3\2\2\2I\u0106\3\2\2\2K\u0108\3\2\2\2M\u010b\3\2\2\2")
        buf.write("O\u010f\3\2\2\2Q\u0112\3\2\2\2S\u0114\3\2\2\2U\u0116\3")
        buf.write("\2\2\2W\u0118\3\2\2\2Y\u011a\3\2\2\2[\u011c\3\2\2\2]\u0123")
        buf.write("\3\2\2\2_\u0131\3\2\2\2a\u0135\3\2\2\2c\u013e\3\2\2\2")
        buf.write("e\u014e\3\2\2\2g\u0150\3\2\2\2i\u0152\3\2\2\2k\u015e\3")
        buf.write("\2\2\2m\u0164\3\2\2\2o\u0167\3\2\2\2q\u017a\3\2\2\2st")
        buf.write("\7v\2\2tu\7t\2\2uv\7w\2\2vw\7g\2\2w\4\3\2\2\2xy\7h\2\2")
        buf.write("yz\7c\2\2z{\7n\2\2{|\7u\2\2|}\7g\2\2}\6\3\2\2\2~\177\7")
        buf.write("p\2\2\177\u0080\7w\2\2\u0080\u0081\7o\2\2\u0081\u0082")
        buf.write("\7d\2\2\u0082\u0083\7g\2\2\u0083\u0084\7t\2\2\u0084\b")
        buf.write("\3\2\2\2\u0085\u0086\7d\2\2\u0086\u0087\7q\2\2\u0087\u0088")
        buf.write("\7q\2\2\u0088\u0089\7n\2\2\u0089\n\3\2\2\2\u008a\u008b")
        buf.write("\7u\2\2\u008b\u008c\7v\2\2\u008c\u008d\7t\2\2\u008d\u008e")
        buf.write("\7k\2\2\u008e\u008f\7p\2\2\u008f\u0090\7i\2\2\u0090\f")
        buf.write("\3\2\2\2\u0091\u0092\7t\2\2\u0092\u0093\7g\2\2\u0093\u0094")
        buf.write("\7v\2\2\u0094\u0095\7w\2\2\u0095\u0096\7t\2\2\u0096\u0097")
        buf.write("\7p\2\2\u0097\16\3\2\2\2\u0098\u0099\7x\2\2\u0099\u009a")
        buf.write("\7c\2\2\u009a\u009b\7t\2\2\u009b\20\3\2\2\2\u009c\u009d")
        buf.write("\7f\2\2\u009d\u009e\7{\2\2\u009e\u009f\7p\2\2\u009f\u00a0")
        buf.write("\7c\2\2\u00a0\u00a1\7o\2\2\u00a1\u00a2\7k\2\2\u00a2\u00a3")
        buf.write("\7e\2\2\u00a3\22\3\2\2\2\u00a4\u00a5\7h\2\2\u00a5\u00a6")
        buf.write("\7w\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8\7e\2\2\u00a8\24")
        buf.write("\3\2\2\2\u00a9\u00aa\7h\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac")
        buf.write("\7t\2\2\u00ac\26\3\2\2\2\u00ad\u00ae\7w\2\2\u00ae\u00af")
        buf.write("\7p\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2")
        buf.write("\7n\2\2\u00b2\30\3\2\2\2\u00b3\u00b4\7d\2\2\u00b4\u00b5")
        buf.write("\7{\2\2\u00b5\32\3\2\2\2\u00b6\u00b7\7d\2\2\u00b7\u00b8")
        buf.write("\7t\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb")
        buf.write("\7m\2\2\u00bb\34\3\2\2\2\u00bc\u00bd\7e\2\2\u00bd\u00be")
        buf.write("\7q\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1")
        buf.write("\7k\2\2\u00c1\u00c2\7p\2\2\u00c2\u00c3\7w\2\2\u00c3\u00c4")
        buf.write("\7g\2\2\u00c4\36\3\2\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7")
        buf.write("\7h\2\2\u00c7 \3\2\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca")
        buf.write("\7n\2\2\u00ca\u00cb\7u\2\2\u00cb\u00cc\7g\2\2\u00cc\"")
        buf.write("\3\2\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf\7n\2\2\u00cf\u00d0")
        buf.write("\7k\2\2\u00d0\u00d1\7h\2\2\u00d1$\3\2\2\2\u00d2\u00d3")
        buf.write("\7d\2\2\u00d3\u00d4\7g\2\2\u00d4\u00d5\7i\2\2\u00d5\u00d6")
        buf.write("\7k\2\2\u00d6\u00d7\7p\2\2\u00d7&\3\2\2\2\u00d8\u00d9")
        buf.write("\7g\2\2\u00d9\u00da\7p\2\2\u00da\u00db\7f\2\2\u00db(\3")
        buf.write("\2\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de\7q\2\2\u00de\u00df")
        buf.write("\7v\2\2\u00df*\3\2\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2")
        buf.write("\7p\2\2\u00e2\u00e3\7f\2\2\u00e3,\3\2\2\2\u00e4\u00e5")
        buf.write("\7q\2\2\u00e5\u00e6\7t\2\2\u00e6.\3\2\2\2\u00e7\u00e8")
        buf.write("\7>\2\2\u00e8\u00e9\7/\2\2\u00e9\60\3\2\2\2\u00ea\u00eb")
        buf.write("\7-\2\2\u00eb\62\3\2\2\2\u00ec\u00ed\7/\2\2\u00ed\64\3")
        buf.write("\2\2\2\u00ee\u00ef\7,\2\2\u00ef\66\3\2\2\2\u00f0\u00f1")
        buf.write("\7\61\2\2\u00f18\3\2\2\2\u00f2\u00f3\7\'\2\2\u00f3:\3")
        buf.write("\2\2\2\u00f4\u00f5\7#\2\2\u00f5<\3\2\2\2\u00f6\u00f7\7")
        buf.write("(\2\2\u00f7\u00f8\7(\2\2\u00f8>\3\2\2\2\u00f9\u00fa\7")
        buf.write("~\2\2\u00fa\u00fb\7~\2\2\u00fb@\3\2\2\2\u00fc\u00fd\7")
        buf.write("?\2\2\u00fdB\3\2\2\2\u00fe\u00ff\7#\2\2\u00ff\u0100\7")
        buf.write("?\2\2\u0100D\3\2\2\2\u0101\u0102\7>\2\2\u0102F\3\2\2\2")
        buf.write("\u0103\u0104\7>\2\2\u0104\u0105\7?\2\2\u0105H\3\2\2\2")
        buf.write("\u0106\u0107\7@\2\2\u0107J\3\2\2\2\u0108\u0109\7@\2\2")
        buf.write("\u0109\u010a\7?\2\2\u010aL\3\2\2\2\u010b\u010c\7\60\2")
        buf.write("\2\u010c\u010d\7\60\2\2\u010d\u010e\7\60\2\2\u010eN\3")
        buf.write("\2\2\2\u010f\u0110\7?\2\2\u0110\u0111\7?\2\2\u0111P\3")
        buf.write("\2\2\2\u0112\u0113\7]\2\2\u0113R\3\2\2\2\u0114\u0115\7")
        buf.write("_\2\2\u0115T\3\2\2\2\u0116\u0117\7*\2\2\u0117V\3\2\2\2")
        buf.write("\u0118\u0119\7+\2\2\u0119X\3\2\2\2\u011a\u011b\7.\2\2")
        buf.write("\u011bZ\3\2\2\2\u011c\u0120\t\2\2\2\u011d\u011f\t\3\2")
        buf.write("\2\u011e\u011d\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e")
        buf.write("\3\2\2\2\u0120\u0121\3\2\2\2\u0121\\\3\2\2\2\u0122\u0120")
        buf.write("\3\2\2\2\u0123\u012b\5_\60\2\u0124\u0128\7\60\2\2\u0125")
        buf.write("\u0127\5_\60\2\u0126\u0125\3\2\2\2\u0127\u012a\3\2\2\2")
        buf.write("\u0128\u0126\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012c\3")
        buf.write("\2\2\2\u012a\u0128\3\2\2\2\u012b\u0124\3\2\2\2\u012b\u012c")
        buf.write("\3\2\2\2\u012c\u012e\3\2\2\2\u012d\u012f\5a\61\2\u012e")
        buf.write("\u012d\3\2\2\2\u012e\u012f\3\2\2\2\u012f^\3\2\2\2\u0130")
        buf.write("\u0132\t\4\2\2\u0131\u0130\3\2\2\2\u0132\u0133\3\2\2\2")
        buf.write("\u0133\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134`\3\2\2")
        buf.write("\2\u0135\u0137\t\5\2\2\u0136\u0138\t\6\2\2\u0137\u0136")
        buf.write("\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u013a\3\2\2\2\u0139")
        buf.write("\u013b\t\4\2\2\u013a\u0139\3\2\2\2\u013b\u013c\3\2\2\2")
        buf.write("\u013c\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013db\3\2\2")
        buf.write("\2\u013e\u0146\7$\2\2\u013f\u0145\n\7\2\2\u0140\u0141")
        buf.write("\7^\2\2\u0141\u0145\t\b\2\2\u0142\u0143\7)\2\2\u0143\u0145")
        buf.write("\7$\2\2\u0144\u013f\3\2\2\2\u0144\u0140\3\2\2\2\u0144")
        buf.write("\u0142\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2")
        buf.write("\u0146\u0147\3\2\2\2\u0147\u0149\3\2\2\2\u0148\u0146\3")
        buf.write("\2\2\2\u0149\u014a\7$\2\2\u014a\u014b\b\62\2\2\u014bd")
        buf.write("\3\2\2\2\u014c\u014f\5\3\2\2\u014d\u014f\5\5\3\2\u014e")
        buf.write("\u014c\3\2\2\2\u014e\u014d\3\2\2\2\u014ff\3\2\2\2\u0150")
        buf.write("\u0151\t\t\2\2\u0151h\3\2\2\2\u0152\u0153\7%\2\2\u0153")
        buf.write("\u0154\7%\2\2\u0154\u0158\3\2\2\2\u0155\u0157\n\n\2\2")
        buf.write("\u0156\u0155\3\2\2\2\u0157\u015a\3\2\2\2\u0158\u0156\3")
        buf.write("\2\2\2\u0158\u0159\3\2\2\2\u0159\u015b\3\2\2\2\u015a\u0158")
        buf.write("\3\2\2\2\u015b\u015c\b\65\3\2\u015cj\3\2\2\2\u015d\u015f")
        buf.write("\t\13\2\2\u015e\u015d\3\2\2\2\u015f\u0160\3\2\2\2\u0160")
        buf.write("\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0162\3\2\2\2")
        buf.write("\u0162\u0163\b\66\3\2\u0163l\3\2\2\2\u0164\u0165\13\2")
        buf.write("\2\2\u0165\u0166\b\67\4\2\u0166n\3\2\2\2\u0167\u016f\7")
        buf.write("$\2\2\u0168\u016e\n\7\2\2\u0169\u016a\7^\2\2\u016a\u016e")
        buf.write("\t\b\2\2\u016b\u016c\7)\2\2\u016c\u016e\7$\2\2\u016d\u0168")
        buf.write("\3\2\2\2\u016d\u0169\3\2\2\2\u016d\u016b\3\2\2\2\u016e")
        buf.write("\u0171\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2")
        buf.write("\u0170\u0176\3\2\2\2\u0171\u016f\3\2\2\2\u0172\u0177\7")
        buf.write("\2\2\3\u0173\u0174\7\17\2\2\u0174\u0177\7\f\2\2\u0175")
        buf.write("\u0177\7\f\2\2\u0176\u0172\3\2\2\2\u0176\u0173\3\2\2\2")
        buf.write("\u0176\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u0179\b")
        buf.write("8\5\2\u0179p\3\2\2\2\u017a\u0182\7$\2\2\u017b\u0181\n")
        buf.write("\7\2\2\u017c\u017d\7^\2\2\u017d\u0181\t\b\2\2\u017e\u017f")
        buf.write("\7)\2\2\u017f\u0181\7$\2\2\u0180\u017b\3\2\2\2\u0180\u017c")
        buf.write("\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0184\3\2\2\2\u0182")
        buf.write("\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0188\3\2\2\2")
        buf.write("\u0184\u0182\3\2\2\2\u0185\u0189\t\f\2\2\u0186\u0187\7")
        buf.write("^\2\2\u0187\u0189\n\b\2\2\u0188\u0185\3\2\2\2\u0188\u0186")
        buf.write("\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018b\b9\6\2\u018b")
        buf.write("r\3\2\2\2\25\2\u0120\u0128\u012b\u012e\u0133\u0137\u013c")
        buf.write("\u0144\u0146\u014e\u0158\u0160\u016d\u016f\u0176\u0180")
        buf.write("\u0182\u0188\7\3\62\2\b\2\2\3\67\3\38\4\39\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    NUMBER = 3
    BOOL = 4
    STRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    NOT = 20
    AND = 21
    OR = 22
    ASSIGNINIT = 23
    ADD = 24
    SUB = 25
    MUL = 26
    DIV = 27
    MODUL = 28
    NOT_OP = 29
    AND_OP = 30
    OR_OP = 31
    ASSIGN = 32
    NOT_EQUAL = 33
    LESS_THAN = 34
    LESS_OR_EQUAL = 35
    GREATER_THAN = 36
    GREATER_OR_EQUAL = 37
    CONCAT = 38
    EQUAL = 39
    LBRACKET = 40
    RBRACKET = 41
    LPAREN = 42
    RPAREN = 43
    COMMA = 44
    ID = 45
    NUMBER_LIT = 46
    STRING_LIT = 47
    BOOLEAN_LIT = 48
    NEWLINE = 49
    COMMENTS = 50
    WS = 51
    ERROR_CHAR = 52
    UNCLOSE_STRING = 53
    ILLEGAL_ESCAPE = 54

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'<-'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'!'", "'&&'", "'||'", "'='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'...'", "'=='", "'['", "']'", "'('", "')'", 
            "','" ]

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

    ruleNames = [ "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
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
            actions[48] = self.STRING_LIT_action 
            actions[53] = self.ERROR_CHAR_action 
            actions[54] = self.UNCLOSE_STRING_action 
            actions[55] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

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
            			raise UncloseString(self.text[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text[1:])
     


