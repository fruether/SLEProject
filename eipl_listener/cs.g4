grammar cs;


scope : 'begin' (r_decl)* r_stmt 'end';

/* Declarations */
<<<<<<< HEAD
r_decl : (STATIC)? VAR r_type (IDENTIFIER ',')* IDENTIFIER ('=' expr)? ';'
       | 'proc' IDENTIFIER  block;
=======
r_decl : (STATIC)? VAR r_type (NAME ',')* NAME ('=' expr)? ';'
       | 'proc' NAME  block;
>>>>>>> 9abb0dce708159b39b343d668bd5d4033e3b3cef

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
<<<<<<< HEAD
IDENTIFIER : [a-z]+;
WS : (' '|'\r'? '\n'|'\t')+ {self.skip();} ;
=======
NAME : [a-z]+;
WS : (' '|'\r'? '\n'|'\t')+ {self.skip();} ;
>>>>>>> 9abb0dce708159b39b343d668bd5d4033e3b3cef
