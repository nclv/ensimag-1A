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

def parse(stream = sys.stdin):
    init_parser(stream)
    l = parse_input()
    parse_token(lexer.END)
    return l


#########################
## parsing of input
    
def parse_input():
    print("@ATTENTION: calc.parse_input à corriger !") # LIGNE A SUPPRIMER
    return []


#########################
## run on the command-line

if __name__ == "__main__":
    print("@ Testing the calculator in infix syntax.")
    print("@ Type Ctrl-D to quit")
    l=parse()
    print("@ result = ", repr(l))
