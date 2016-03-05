grammar cs;


scope : 'begin' (r_decl)* r_stmt 'end';

/* Declarations */
r_decl : (STATIC)? VAR  r_type (IDENTIFIER ',')* IDENTIFIER ('=' expr)? ';'
       | 'proc' IDENTIFIER  block;

/* Statements */
r_stmt : ';'
    | IDENTIFIER '=' expr ';'
    | 'if' '(' expr ')' r_stmt ( 'else' r_stmt )?
    | 'while' '(' expr ')' r_stmt
    | scope
    | 'call' IDENTIFIER ';'
    | 'write' expr ';'
    | block
    ;

block : '{' ( r_stmt )* '}';
/* Expressions */
expr : aexpr ( '>=' expr )? ;
aexpr : term ( '+' aexpr )?
      | term ( '-' aexpr )?
      ;
term : factor ( '*' term )? ;
factor : INT
        |  IDENTIFIER
        | '(' expr ')' ;

r_type: INTEGER | BOOLEAN | CHAR;

BOOLEAN : 'bool';
INTEGER : 'int';
CHAR : 'char';
STATIC : 'static';
VAR : 'var';
INT : [0-9]+;
IDENTIFIER : [a-z]+;
WS : (' '|'\r'? '\n'|'\t')+ {self.skip();} ;