#!/bin/sh
alias antlr4='java -jar /usr/local/lib/antlr-4.5.1-complete.jar'
$(antlr4 -Dlanguage=Python3 cs.g4) && python3 eval.py cs_input.txt
