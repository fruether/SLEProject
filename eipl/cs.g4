grammar cs;

@header {import facts}

scope : 'begin' (r_decl)* r_stmt 'end';

/* Declarations */
r_decl : VAR t = r_type NAME '=' expr ';'
         {facts.create_fact("typeOF", $t.text, $NAME.text)}
       | 'proc' NAME block;

/* Statements */
r_stmt : ';'
    | NAME '=' expr ';'
    | 'if' '(' expr ')' r_stmt ( 'else' r_stmt )?
    | 'while' '(' expr ')' r_stmt
    | scope
    | 'call' NAME ';'
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
        |  NAME
        | '(' expr ')' ;

r_type: INTEGER;

BOOLEAN : 'bool';
INTEGER : 'int';
CHAR : 'char';
VAR : 'var';
INT : [0-9]+;
NAME : [a-z]+;
WS : (' '|'\r'? '\n'|'\t')+ {self.skip();} ;