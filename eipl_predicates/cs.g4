grammar cs;

@header {
from libs import facts, semantic, variables

semantic.init()
semantic.add_scope("main")
variables.nameList = []
variables.staticOpt = None
}

scope : 'begin' (statement)* r_stmt 'end';

/* Declarations */
statement : (static)? VAR rtype = r_type (identifier ',')* identifier ('=' expr)? ';'
         {facts.create_fact("typeOF", $rtype.text, variables.IdentifierList)}
         {{facts.if_not_empty(variables.staticOpt, [("Static", variables.IdentifierList)])}}
         {semantic.release_node()}
       | 'proc' IDENTIFIER {semantic.add_scope($IDENTIFIER.text)} block {semantic.remove_scope()};

/* Statements */
r_stmt : ';'
    | IDENTIFIER '=' expr ';'
    | 'if' '(' expr ')' r_stmt ( 'else' r_stmt )?
    | 'while' '(' expr ')' r_stmt
    | scope
    | 'call' IDENTIFIER ';' {facts.create_fact("callTo", semantic.get_current_scope(), $IDENTIFIER.text)}
    | 'write' expr ';'
    | block
    ;

block : '{' (s=r_stmt {{semantic.exec_block("block","List", $s.text)}})* '}'
         {{facts.create_fact("succ", facts.next(variables.blockList, []))}}
         {{semantic.release_node()}}
;
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

identifier returns [nameElement]:  IDENTIFIER
{nameElement = semantic.exec_block("Identifier","List", $IDENTIFIER.text)};

static returns [staticElement]: STATIC
{staticElement = semantic.exec_block("static","Opt", $STATIC.text)};


BOOLEAN : 'bool';
INTEGER : 'int';
CHAR : 'char';
STATIC : 'static';
VAR : 'var';
INT : [0-9]+;
IDENTIFIER : [a-z]+;
WS : (' '|'\r'? '\n'|'\t')+ {self.skip();} ;