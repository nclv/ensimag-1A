#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculator in infix syntax
"""

import parser
import lexer
import sys
from parser import init_parser, parse_token, mk_rules, select


###################
# #the public function of the calculator
def parse(stream=sys.stdin):
    init_parser(stream)
    l = parse_input()
    parse_token(lexer.END)
    return l


#########################
# #parsing of input
def parse_input():
    l = parse_inputX([])
    return l


def parse_inputX(l0):
    if parser.current == lexer.END:
        return l0
    else:
        n = parse_exp2(l0)
        parse_token(lexer.QUEST)
        l0.append(n)
        l = parse_inputX(l0)
        return l


def parse_exp2(l):
    n1 = parse_exp1(l)
    n = parse_exp2X(l, n1)
    return n


def parse_exp2X(l, n1):
    if parser.current in {lexer.QUEST, lexer.CPAR}:
        return n1
    elif parser.current == lexer.PLUS:
        parse_token(lexer.PLUS)
        n2 = parse_exp1(l)
        n = parse_exp2X(l, n1+n2)
        return n
    else:
        print(parser.current)
        parse_token(lexer.MINUS)
        n2 = parse_exp1(l)
        n = parse_exp2X(l, n1-n2)
        return n


def parse_exp1(l):
    n1 = parse_exp0(l)
    n = parse_exp1X(l, n1)
    return n


def parse_exp1X(l, n1):
    if parser.current == lexer.MULT:
        parse_token(lexer.MULT)
        n2 = parse_exp0(l)
        n = parse_exp1X(l, n1*n2)
        return n
    elif parser.current == lexer.DIV:
        parse_token(lexer.DIV)
        n2 = parse_exp0(l)
        n = parse_exp1X(l, n1/n2)
        return n
    else:
        return n1


def parse_exp0(l):
    if parser.current == lexer.VAR:
        i = parse_token(lexer.VAR)
        return l[i-1]
    elif parser.current == lexer.MINUS:
        parse_token(lexer.MINUS)
        n0 = parse_exp0(l)
        return -n0
    elif parser.current == lexer.OPAR:
        parse_token(lexer.OPAR)
        n = parse_exp2(l)
        parse_token(lexer.CPAR)
        return n
    else:
        n = parse_token(lexer.INT)
        print(n)
        return n

#########################
# # run on the command-line

if __name__ == "__main__":
    print("@ Testing the calculator in infix syntax.")
    print("@ Type Ctrl-D to quit")
    l = parse()
    print("@ result = ", repr(l))
