#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generic functions to test parsers
"""

import io
import parser

PARSER_NAME = None
PARSER_UNDER_TEST = None

def run(string):
    stream = io.StringIO(string)
    try:
        return PARSER_UNDER_TEST(io.StringIO(string))
    except Exception as e:
        stream.close()
        raise e

def test_result(calc_input, expected):
    print("@ test {0} on input:".format(PARSER_NAME), repr(calc_input))
    print("@ result expected:", repr(expected))
    found = run(calc_input)
    assert found == expected, "found {0} vs {1} expected".format(found, expected)
    print("@ => OK")
    print()

def test_parsing_error(calc_input):
    print("@ test {0} on input:".format(PARSER_NAME), repr(calc_input))
    print("@ parsing error expected")
    try:
        result=run(calc_input)
        print("@ unexpected result:", result)
        assert False
    except parser.Error as e:
        print("@ parsing error found:", e)
        pass
    print("@ => OK")
    print()
