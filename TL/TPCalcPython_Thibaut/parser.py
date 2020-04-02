#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generic functions for LL(1) parsing
"""

import lexer

# name of tokens in error message


def token_name():
    tn = list(lexer.TOKEN_PREFIX)
    tn[lexer.VAR] = 'VAR'
    tn[lexer.INT] = 'INT'
    tn[lexer.END] = 'END'
    return tn

TOKEN_NAME = token_name()


class Error(Exception):
    pass


def init_parser(stream):
    global current, value
    lexer.reinit(stream)
    current, value = lexer.next_token()
    # print("@ init parser on",  repr(lexer.str_attr_token(current, value)))


def parse_token(token):
    global current, value
    if current != token:
        raise Error('found token ' + repr(lexer.str_attr_token(current, value)) + ' but expected ' + repr(TOKEN_NAME[token]))
    if current != lexer.END:
        old = value
        current, value = lexer.next_token()
        return old


def select(rules):
    return rules[current]


def mk_rules(default_rule, directed_rules):
    rules = [default_rule]*len(lexer.TOKENS)
    for director, rule in directed_rules:
        for token in director:
            assert rules[token] is default_rule, "Incorrect director: token {0} both associated to rules {1} and {2}".format(repr(TOKEN_NAME[token]), rules[token], rule)
            rules[token] = rule
    return rules
