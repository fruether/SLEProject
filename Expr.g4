grammar Expr;		
prog:	(expr NEWLINE)*;
expr:	expr ('*'|'/') expr
    |	expr ('+'|'-') expr
    |	'(' expr ')'
    |   decl
    ;
decl: (x=identifier {print($x.text)}', ')* b = identifier {print($b.text)};
identifier : INT;
NEWLINE : [\r\n]+ ;
INT     : [0-9]+ ;
WS : (' '|'\r'? '\n'|'\t')+;