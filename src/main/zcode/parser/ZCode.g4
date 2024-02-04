//
// Ho va ten: Tran Trong Bach
// MSSV : 2112847
//
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}


//  --------------------------  begin ----------------------- //

// declared 
program: NEWLINE* list_declared EOF;
list_declared:  declared list_declared |  declared;
declared: function | variables ignore;

// Declared variable
variables       : implicit_var | implicit_dynamic | keyword_var; 
implicit_var    : VAR ID ASSIGNINIT expression;
implicit_dynamic: DYNAMIC ID (ASSIGNINIT expression)?;
keyword_var     : (BOOL | NUMBER | STRING) ID (LBRACKET list_NUMBER_LIT RBRACKET)? (ASSIGNINIT expression)?;
list_NUMBER_LIT : NUMBER_LIT COMMA list_NUMBER_LIT | NUMBER_LIT;


// Declared function
function: FUNC ID LPAREN parameters_list? RPAREN  (ignore? return_statement | ignore? block_statement | ignore);
parameters_list : list_expr | ;

// Expression
list_expr   : expression COMMA list_expr | expression;
expression  : expression1 CONCAT expression1 | expression1;
expression1 : expression2 (ASSIGN | EQUAL | NOT_EQUAL | LESS_THAN | GREATER_THAN | LESS_OR_EQUAL | GREATER_OR_EQUAL) expression2 | expression2;
expression2 : expression2 (AND | OR) expression3 | expression3;
expression3 : expression3 (ADD | SUB) expression4 | expression4;
expression4 : expression4 (MUL | DIV | MODUL) expression5 | expression5;
expression5 : NOT expression5 | expression6;
expression6 : (ADD | SUB) expression6 | expression7;
expression7 : (ID | funcall) LBRACKET list_expr RBRACKET | ID | literal | LPAREN expression RPAREN | funcall;
funcall		: ID LPAREN list_expr? RPAREN;

// Value
literal: NUMBER_LIT | STRING_LIT | TRUE | FALSE | array_literal;
array_literal: LBRACKET list_expr RBRACKET;

// Statements
statement_list: statement statement_list | ; 
statement: declaration_statement | assignment_statement 
            | if_statement | for_statement 
            | break_statement | continue_statement 
            | return_statement  | call_statement | block_statement;
declaration_statement: variables ignore;
assignment_statement : lhs ASSIGNINIT expression ignore;
lhs 				 : ID | array_literal;
if_statement		 : IF LPAREN expression RPAREN statement (elif_statement)? (else_statement)? ;
elif_statement		 : ELIF LPAREN expression RPAREN statement;
else_statement		 : ELSE statement;
for_statement		 : FOR ID UNTIL expression BY expression ignore? statement;
break_statement		 : BREAK ignore;
continue_statement	 : CONTINUE ignore;
return_statement 	 : RETURN (list_expr)? ignore;
call_statement	 	 : funcall ignore;
block_statement		 : BEGIN ignore statement_list END ignore;

ignore: (COMMENTS | NEWLINE)+; // ignore

// KeyWord
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

// Operators
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

// Separators
LBRACKET: '[';
RBRACKET: ']';
LPAREN  : '(';
RPAREN  : ')';
COMMA   : ',';


//Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

//Literal 
NUMBER_LIT		:	INT ('.' INT*)? EXP?;
fragment INT	:	[0-9]+;
fragment EXP 	:	([eE] [-+]? [0-9]+);
STRING_LIT		:	'"' (~[\r\n\\"] | '\\' [bfrnt'\\] | '\'"')* '"' {self.text = self.text[1:-1]};
BOOLEAN_LIT		:	TRUE|FALSE;

NEWLINE: [\n]; 					 // 
COMMENTS: '##' ~[\n\r]* -> skip; // Comments
WS : [ \t\r\f\b]+ -> skip ; 	 // Spaces, tabs

//ERROR
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' (~[\r\n\\"] | '\\' [bfrnt'\\] | '\'"')* (EOF | '\r\n' | '\n')
	{
		if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
			raise UncloseString(self.text[1:-2])
		elif(self.text[-1] == '\n'):
			raise UncloseString(self.text[1:-1])
		else:
			raise UncloseString(self.text[1:])
	};
ILLEGAL_ESCAPE: '"' (~[\r\n\\"] | '\\' [bfrnt'\\] | '\'"')* ([\r] | '\\' ~[bfrnt'\\]) 
	{raise IllegalEscape(self.text[1:])};
//  -------------------------- end ------------------- //