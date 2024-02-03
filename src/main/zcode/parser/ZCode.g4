grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}


// //! --------------------------  Lexical structure ----------------------- //

// declared 
program: NEWLINE* list_declared EOF;
list_declared:  declared list_declared |  declared;
declared: function | variables ignore;

//TODO declared variable
variables       : implicit_var | implicit_dynamic | keyword_var; 
implicit_var    : VAR ID ASSIGNINIT expression;
implicit_dynamic: DYNAMIC ID (ASSIGNINIT expression)?;
keyword_var     : ((BOOL | NUMBER | STRING) ID (ASSIGNINIT expression)?) | 'array' ID LBRACKET list_NUMBER_LIT RBRACKET ASSIGNINIT expression;
list_NUMBER_LIT : NUMBER_LIT COMMA list_NUMBER_LIT | NUMBER_LIT;


//TODO declared function
function: FUNC ID LPAREN prameters_list? RPAREN  (ignore? return_statement | ignore? block_statement | ignore);
prameters_list : list_expr | ;

//TODO Expression
list_expr   : expression COMMA list_expr | expression;
expression  : expression1 CONCAT expression1 | expression1;
expression1 : expression1 (ASSIGN | EQUAL | NOT_EQUAL | LESS_THAN | GREATER_THAN | LESS_OR_EQUAL | GREATER_OR_EQUAL) expression1 | expression2;
expression2 : expression2 (AND | OR) expression3 | expression3;
expression3 : expression3 (ADD | SUB) expression4 | expression4;
expression4 : expression4 (MUL | DIV | MODUL) expression5 | expression5;
expression5 : NOT expression5 | expression6;
expression6 : (ADD | SUB) expression6 | expression7;
expression7 : expression7 index_operator | expression8 ;
expression8 : ID | literal | LPAREN expression RPAREN | function;
index_operator	 :  expression LBRACKET expression RBRACKET;
//TODO Value
literal: NUMBER_LIT | STRING_LIT | TRUE | FALSE | array_literal;
array_literal: LPAREN list_literal? RPAREN;
list_literal :expression COMMA list_literal | expression;

//TODO  Statements
statement_list: statement statement_list | ; 
statement: declaration_statement | assignment_statement 
            | if_statement | for_statement 
            | break_statement | continue_statement 
            | return_statement  | call_statement | block_statement;
declaration_statement: variables ignore;
assignment_statement : lhs ASSIGNINIT expression ignore;
lhs 				 : ID | array_literal;
if_statement		 : IF LPAREN expression RPAREN statement (elif_statement)* (else_statement)? ;
elif_statement		 : ELIF LPAREN expression RPAREN statement;
else_statement		 : ELSE statement;
for_statement		 : FOR ID UNTIL expression BY expression ignore? statement;
break_statement		 : ignore? BREAK;
continue_statement	 : ignore? CONTINUE;
return_statement 	 : RETURN expression?;
call_statement	 	 : function;
block_statement		 : 'begin' ignore statement_list ignore 'end' ignore;
// kí tự bỏ qua
ignore: (COMMENTS | NEWLINE)+;
//! --------------------------  Lexical structure ----------------------- //
// TODO KeyWord
TRUE    :   'true';
FALSE   :   'false';
NUMBER	: 	'number';
BOOL	: 	'bool';
STRING	: 	'string';
RETURN 	:	'return';
VAR		:	'var';
DYNAMIC	:	'dynamic';
FUNC	:	'func';
FOR 	:	'for';
UNTIL	:	'until';
BY		:	'by';
BREAK	:	'break';
CONTINUE:	'continue';
IF 		:	'if';
ELSE	: 	'else';
ELIF	:	'elif';
BEGIN	:	'begin';
END 	:	'end';
NOT		:	'not';
AND		:	'and';
OR 		:	'or';

// TODO Operators
ASSIGNINIT: '<-';
ADD		: 	'+';
SUB		:	'-';
MUL 	:	'*';
DIV 	: 	'/';
MODUL 	: 	'%';
NOT_OP 	: 	'!';
AND_OP	: 	'&&';
OR_OP	: 	'||';
ASSIGN 	: 	'=';
NOT_EQUAL 		 :	'!=';
LESS_THAN 		 : 	'<';
LESS_OR_EQUAL 	 : 	'<=';
GREATER_THAN 	 : 	'>';
GREATER_OR_EQUAL : 	'>=';
CONCAT 		     : 	'...';
EQUAL 			 : 	'==';

// TODO Separators
LBRACKET: '[';
RBRACKET: ']';
LPAREN  : '(';
RPAREN  : ')';
COMMA   : ',';


// TODO Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// TODO Literal 
//! STRING_LIT nhớ dùng python bỏ đi " " đầu và cuối
NUMBER_LIT		:	INT ('.' INT*)? EXP?;
fragment INT	:	[0-9]+;
fragment EXP 	:	([eE] [-+]? [0-9]+);
STRING_LIT		:	'"' ~[\r\n\f\\'"] | '\\' [bfrnt'\\] | '\'"' {self.text = self.text[1:-1];};
BOOLEAN_LIT		:	TRUE|FALSE;

// NEWLINE COMMENTS WS
//! vì NEWLINE là kí tự kết thúc giống với ';' trong C nên lấy để xử lí bước sau
//! vì ngôn ngữ này COMMENTS chỉ 1 hàng không chung với mấy biểu thức khác nên bắt để xử lí thứ tự các bước sau
//! COMMENTS lên lớp nghe thử thầy nói gì không nha vì này nén lỗi phần lexer cũng được mà nhưng thứ tự ngữ pháp và ở phần tiếp theo -> này tùy thầy thôi
NEWLINE: [\n]; // 
COMMENTS: '##' ~[\n\r\f]* -> skip; // Comments
WS : [ \t\r\f\b]+ -> skip ; // skip spaces, tabs

// TODO ERROR
//! hiện thực  UNCLOSE_STRING và ILLEGAL_ESCAPE code antlr và python tận dụng lại ý tưởng STRING_LIT
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' (~[\r\n\f\\'"] | '\\' [bfrnt'\\] | '\'"')* (EOF | '\r\n' | '\n')
	{
		if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
			raise UncloseString(self.text[1:-2])
		elif(self.text[-1] == '\n'):
			raise UncloseString(self.text[1:-1])
		else:
			raise UncloseString(slef.text[1:])
	};
ILLEGAL_ESCAPE: '"' (~[\r\n\f\\'"] | '\\' [bfrnt'\\] | '\'"')* ([\r\f'] | '\\' ~[bfrnt'\\] | '\'' ~["]) 
	{raise IllegalEscape(self.text[1:]);};
//!  -------------------------- end Lexical structure ------------------- //