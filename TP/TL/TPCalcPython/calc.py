#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculator in infix syntax
"""

import lexer
import sys

from parser import init_parser, parse_token, mk_rules, select

###################
## the public function of the calculator


def parse(stream=sys.stdin):
    init_parser(stream)
    l = parse_input()
    parse_token(lexer.END)
    return l


#########################
## parsing of input


def parse_input():
    return parse_inputx([])


def parse_inputx(l0):
    if lexer.current == "":
        return l0
    n = parse_exp2(l0)
    parse_token(lexer.QUEST)
    l0.append(n)
    return parse_inputx(l0)


#########################
## parsing of expressions


def parse_exp_INT(l):
    return parse_token(lexer.INT)


def parse_exp_VAR(l):
    i = parse_token(lexer.VAR)
    return l[i - 1]


def parse_exp_MINUS(l):
    parse_token(lexer.MINUS)
    n0 = parse_exp0(l)
    return -n0


def parse_exp_OPAR(l):
    parse_token(lexer.OPAR)
    n = parse_exp2(l)
    parse_token(lexer.CPAR)
    return n


# la liste des tokens_prefix
EXP_RULES = mk_rules(
    parse_exp_INT,
    [
        ([lexer.VAR], parse_exp_VAR),
        ([lexer.MINUS], parse_exp_MINUS),
        ([lexer.OPAR], parse_exp_OPAR),
    ],
)


def parse_exp0(l):
    return select(EXP_RULES)(l)


def parse_exp2(l):
    n1 = parse_exp1(l)
    n = parse_exp2x(l, n1)
    return n


def parse_exp2x(l, n1):
    if lexer.current in ["?", ")"]:
        return n1
    elif lexer.current == "+":
        parse_token(lexer.PLUS)
        n2 = parse_exp1(l)
        return parse_exp2x(l, n1 + n2)
    elif lexer.current == "-":
        parse_token(lexer.MINUS)
        n2 = parse_exp1(l)
        return parse_exp2x(l, n1 - n2)


def parse_exp1(l):
    n1 = parse_exp0(l)
    n = parse_exp1x(l, n1)
    return n


def parse_exp1x(l, n1):
    if lexer.current in ["+", "-", "?", ")"]:
        return n1
    elif lexer.current == "*":
        parse_token(lexer.MULT)
        n2 = parse_exp0(l)
        return parse_exp1x(l, n1 * n2)
    elif lexer.current == "/":
        parse_token(lexer.DIV)
        n2 = parse_exp0(l)
        return parse_exp1x(l, n1 / n2)


#########################
## run on the command-line

if __name__ == "__main__":
    print("@ Testing the calculator in infix syntax.")
    print("@ Type Ctrl-D to quit")
    l = parse()
    print("@ result = ", repr(l))
