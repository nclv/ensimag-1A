#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculator in prefix syntax
"""

import lexer
import sys

from parser import init_parser, parse_token, mk_rules, select

###################
## the public function of the calculator

def parse(stream = sys.stdin):
    init_parser(stream)
    return parse_input([])

#########################
## parsing of input

def parse_input(l):
    print("@ATTENTION: pcalc.parse_input à corriger !") # LIGNE A SUPPRIMER
    print(l)
    n = parse_exp(l)
    print(n)
    return l + [n]

#########################
## parsing of expressions

def parse_exp_INT(l):
    return parse_token(lexer.INT)

def parse_exp_QUEST(l):
    pass

def parse_exp_PLUS(l):
    pass

def parse_exp_MINUS(l):
    pass

# la liste des tokens_prefix
EXP_RULES = mk_rules(parse_exp_INT, [[lexer.PLUS, parse_exp_PLUS], [lexer.MINUS, parse_exp_MINUS]])

def parse_exp(l):
    return select(EXP_RULES)(l)

#########################
## run on the command-line

if __name__ == "__main__":
    print("@ Testing the calculator in prefix syntax.")
    print("@ Type Ctrl-D to quit")
    l = parse()
    print("@ result = ", repr(l))
