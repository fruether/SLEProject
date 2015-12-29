grammar cs;

@header {
from libs import facts, semantic

semantic.init()
semantic.add_scope("main")
}

scope : 'begin' (r_decl)* r_stmt 'end';

/* Declarations */
r_decl : VAR t = r_type (name ',')* l = name ('=' expr)? ';'
         {facts.create_fact("typeOF", $t.text, $l.nameList)}
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

name returns [nameList]:  NAME{
semantic.add_context("Name", $NAME.text)
$nameList = semantic.terminal_list("Name")
};


BOOLEAN : 'bool';
INTEGER : 'int';
CHAR : 'char';
VAR : 'var';
INT : [0-9]+;
NAME : [a-z]+;
WS : (' '|'\r'? '\n'|'\t')+ {self.skip();} ;