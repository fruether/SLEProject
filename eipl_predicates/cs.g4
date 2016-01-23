grammar cs;

@header {
from libs import facts, semantic, variables

semantic.init()
semantic.add_scope("main")
variables.nameList = []
variables.staticOpt = None
}

scope : 'begin' (r_decl)* r_stmt 'end';

/* Declarations */
r_decl : (static)? VAR t = r_type (name ',')* name ('=' expr)? ';'
         {facts.create_fact("typeOF", $t.text, variables.nameList)}
         {{facts.if_not_empty(variables.staticOpt, [("Static", variables.nameList)])}}
         {semantic.release_node()}
       | 'proc' NAME {semantic.add_scope($NAME.text)} block {semantic.remove_scope()};

/* Statements */
r_stmt : ';'
    | NAME '=' expr ';'
    | 'if' '(' expr ')' r_stmt ( 'else' r_stmt )?
    | 'while' '(' expr ')' r_stmt
    | scope
    | 'call' NAME ';' {facts.create_fact("callTo", semantic.get_current_scope(), $NAME.text)}
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

name returns [nameElement]:  NAME
{nameElement = semantic.exec_block("name","List", $NAME.text)};

static returns [staticElement]: STATIC
{staticElement = semantic.exec_block("static","Opt", $STATIC.text)};


BOOLEAN : 'bool';
INTEGER : 'int';
CHAR : 'char';
STATIC : 'static';
VAR : 'var';
INT : [0-9]+;
NAME : [a-z]+;
WS : (' '|'\r'? '\n'|'\t')+ {self.skip();} ;