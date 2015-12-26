grammar cs;
scope : 'begin' (r_decl)* r_stmt 'end';

/* Declarations */
r_decl : 'var' r_type NAME '=' expr ';'
       | 'proc' NAME r_stmt ';';

/* Statements */
r_stmt : ';'
    | NAME '=' expr ';'
    | 'if' '(' expr ')' r_stmt ( 'else' r_stmt )?
    | 'while' '(' expr ')' r_stmt
    | '{' ( r_stmt )* '}'
    | scope
    | 'call' NAME ';'
    | 'write' expr ';'
    ;

/* Expressions */
 expr : aexpr ( '>=' expr )? ;
aexpr : term ( '+' aexpr )?
      | term ( '-' aexpr )?
      ;
term : factor ( '*' term )? ;
factor : INT
        |  NAME
        | '(' expr ')' ;

r_type: BOOLEAN | INTEGER  | CHAR;

NAME : [a-z]+;
BOOLEAN : 'bool';
INTEGER : 'int';
CHAR : 'char';
INT : [0-9]+;
WS : (' '|'\r'? '\n'|'\t')+ {self.skip();} ;