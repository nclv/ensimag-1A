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


def parse(stream=sys.stdin):
    init_parser(stream)
    return parse_input([])


#########################
## parsing of input


def parse_input(l):
    if lexer.current == "":
        parse_token(lexer.END)
        return l
    parse_token(lexer.QUEST)
    n = parse_exp(l)
    l.append(n)
    return parse_input(l)


#########################
## parsing of expressions


def parse_exp_INT(l):
    return parse_token(lexer.INT)


def parse_exp_VAR(l):
    i = parse_token(lexer.VAR)
    return l[i - 1]


def parse_exp_PLUS(l):
    parse_token(lexer.PLUS)
    n1 = parse_exp(l)
    n2 = parse_exp(l)
    return n1 + n2


def parse_exp_MINUS(l):
    parse_token(lexer.MINUS)
    n1 = parse_exp(l)
    return -n1


def parse_exp_MULT(l):
    parse_token(lexer.MULT)
    n1 = parse_exp(l)
    n2 = parse_exp(l)
    return n1 * n2


def parse_exp_DIV(l):
    parse_token(lexer.DIV)
    n1 = parse_exp(l)
    n2 = parse_exp(l)
    return n1 / n2


# la liste des tokens_prefix
EXP_RULES = mk_rules(
    parse_exp_INT,
    [
        ([lexer.VAR], parse_exp_VAR),
        ([lexer.PLUS], parse_exp_PLUS),
        ([lexer.MINUS], parse_exp_MINUS),
        ([lexer.MULT], parse_exp_MULT),
        ([lexer.DIV], parse_exp_DIV),
    ],
)


def parse_exp(l):
    return select(EXP_RULES)(l)


#########################
## run on the command-line

if __name__ == "__main__":
    print("@ Testing the calculator in prefix syntax.")
    print("@ Type Ctrl-D to quit")
    l = parse()
    print("@ result = ", repr(l))
