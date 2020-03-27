#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lexer for the various calculators of TL2
"""

import sys

###############################
# Definition of TOKENS and SPACES
# Update the range here in order to add new tokens
# You should then probably also update functions
#     'str_attr_token' and 'mk_switch' below
TOKENS = tuple(range(8))
QUEST, PLUS, MINUS, MULT, DIV, INT, VAR, END = TOKENS
TOKEN_PREFIX = ('?', '+', '-', '*', '/', "", '#', '')
SPACES = { ' ', '\n', '\t' }


#################################
# private functions and variables of the lexer
def is_digit(char):
    return '0' <= char and char <= '9'

def parse_END(token):
    return (token, None)

def parse_digit():
    if not is_digit(current):
        raise unknown_digit_error(current)
    value = ord(current) - ord('0')
    update_current()
    return value

def parse_INT(token):
    # print("@ATTENTION: lexer.parse_INT à finir !") # LIGNE A SUPPRIMER
    value = 0
    while is_digit(current):
        value = value * 10 + parse_digit()
    return (token, value)

def parse_DEFAULT(token):
    update_current()
    return (token, None)

def parse_VAR(token):
    update_current()
    if is_digit(current):
        return parse_INT(token)
    return (token, parse_digit())

def mk_switch():
    # print("@ATTENTION: lexer.mk_switch à finir !") # LIGNE A SUPPRIMER
    PARSERS = (parse_DEFAULT, parse_DEFAULT, parse_DEFAULT, parse_DEFAULT, parse_DEFAULT, parse_INT, parse_VAR, parse_END)
    d = {}
    for indice, token in enumerate(TOKENS):
        if indice == 5:
            for digit in range(10):
                d[str(digit)] = (token, PARSERS[indice])
        else:
            d[TOKEN_PREFIX[indice]] = (token, PARSERS[indice])

    return d


SWITCH = mk_switch()
in_stream = sys.stdin
current = ''

def update_current():
    global current
    current = in_stream.read(1)
    print("@", repr(current))  # decomment this line may help debugging

def init_current():
    global current
    if current == '':
        update_current()


#################################
# public functions of the lexer

class Error(Exception):
    pass

def unknown_digit_error(char):
    return Error('Expected a digit, but found ' + repr(char))

def unknown_token_error(char):
    return Error('Unknown start of token ' + repr(char))

def str_attr_token(token, value):
    s = TOKEN_PREFIX[token]
    if token in (INT, VAR):
        assert type(value) is int and value >= 0
        s += str(value)
    else:
        assert value is None
    return s


def reinit(stream = sys.stdin):
    global in_stream, current
    assert stream.readable()
    in_stream = stream
    current = ''


def next_token():
    init_current() # init current if 'reinit' has been called (or a previous Error has closed in_stream)
    while current in SPACES:
        update_current()
    try:
        token, parser = SWITCH[current]
        return parser(token)
    except KeyError:
        raise unknown_token_error(current)

if __name__ == "__main__":
    print("@ Testing the lexer. Just type TOKENS and SPACES.")
    print("@ Each token should appear once by line")
    print("@ Type Ctrl-D to quit")
    while True:
        token, value = next_token()
        print("@", str_attr_token(token, value))
        if token == END:
            break
