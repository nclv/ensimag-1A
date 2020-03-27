#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced tests for the infix calculator like computing Ackermann function 
"""

import test_parser
from calc import parse
test_parser.PARSER_NAME='calc'
test_parser.PARSER_UNDER_TEST=parse
from test_parser import test_result

# a few basic tests
test_result("7 ? - #-1 ? -2: 130 + #(1-2) ?", [123, -7])
test_result("1?p#-2(-2:0?#-1)",[0, 3])

# test of functions

def test(f, code, arg):
    test_result(str(arg) + "?" + code, [f(arg)])

def test2(f, code, arg1, arg2):
    test_result(str(arg1) + "?" + str(arg2) + "?" + code, [f(arg1, arg2)])


ABS = """
- #-1 ?
#-1
   (-2: #-1 ?)
0: -1 ?
"""

test(abs, ABS, 7)
test(abs, ABS, 0)
test(abs, ABS, -9)


FACT = """
#-1 ?
p
-2: #-2 - 1 ?
#-2
   ( -3: #-2 * #-3 ?
     #-1 )
0:-2 ?
"""

def fact(n):
    if n > 1:
        return n*fact(n-1)
    return n

test(fact, FACT, -1)
test(fact, FACT, 7)

#########################################################
# auxiliary functions to build programs for the calculator

def program(fundef, main, numargs=1):
    start = numargs+1
    code = ["0 ?"]
    for f in fundef:
        code.append("p")
        add_if(code, "#{0}".format(start), f)
    code.append("{0}: 1 ?".format(start))
    for i in main:
        code.append(i)
    code.append("1: #-1 ?")
    code.append("0: 1 ?\n")
    return "\n".join(code)

def add_if(code, exp, block):
    code.append(exp + " (")
    for i in block:
        code.append("  " + i)

def add_goto(code, f):
    code.append("#{0} )".format(f))

def add_call(code, f):
    code.append("1 ?") # not_returned = 1
    code.append("p")  # return_address
    add_if(code, "#-2", ["#{0} )".format(f)]) # if not_returned, goto f
    code.append("0: -2 ?") # pop 2

def add_ret(code):
    code.append("-2: 0 ?") # is_return = 0
    code.append("#-1 )")

def name_fun(i,numargs=1):
    return i+numargs+1

######################################
# Example of the quad function below

def quad(x):
    def double(y):
        return 2*y
    return double(double(x))

def mk_quad():
    double = name_fun(1)
    double_code = ["-3: 2 * #-3 ?"]
    add_ret(double_code)
    main_code = ["#1 ?"]
    add_call(main_code, double)
    add_call(main_code, double)
    return program([double_code], main_code)

QUAD=mk_quad()

print("QUAD = ")
print(QUAD)
print()

test(quad, QUAD, 7)

##########################################
# Example of the Ackermann function below

def ack(m,n):
    """Ackermann function"""
    if m <= 0:
        return n + 1
    elif n <= 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))

def mk_ack():
    # m = 1 et n = 2
    ack = name_fun(1, 2)
    # locally m = -4 n = -3 -- res = -4
    ack_code = []
    # first if
    next_if = ["-4: #-3 + 1 ?"] # res=n+1
    add_ret(next_if)
    add_if(ack_code, "1-#-4", next_if) # if 1 <= m
    # second if
    next_if = ["-4: #-4 - 1 ?"]  # m=m-1
    next_if.append("-3: 1 ?") # n=1
    add_goto(next_if, ack)
    add_if(ack_code, "1-#-3", next_if) # if 1 <= n
    # else
    ack_code.append("#-4 ?") # push m
    ack_code.append("#-4 - 1 ?") # param n-1
    add_call(ack_code, ack)
    ack_code.append("-5: #-2 ?") # n = res_call
    ack_code.append("0: -2 ?") # pop
    ack_code.append("-4: #-4 - 1 ?") # m=m-1
    add_goto(ack_code, ack)
    #
    main_code = ["#1 ?"]
    main_code.append("#2 ?")
    add_call(main_code, ack)
    main_code.append("0: -1 ?") # pop n
    return program([ack_code], main_code, numargs=2)

ACK = mk_ack()
print("ACK = ")
print(ACK)

test2(ack, ACK, 0, 7)
test2(ack, ACK, 1, 7)
test2(ack, ACK, 2, 7)


#########################################
# Variant of the Ackermann function (even more increasing)

def big(m,n):
    """Ackermann function (variant)"""
    if m <= 0:
        return n * n
    elif n <= 0:
        return big(m - 1, 2)
    else:
        return big(m - 1, big(m, n - 1))

def mk_big():
    # m = 1 et n = 2
    ack = name_fun(1, 2)
    # locally m = -4 n = -3 -- res = -4
    ack_code = []
    # first if
    next_if = ["-4: #-3 * #-3 ?"] # res=n*n
    add_ret(next_if)
    add_if(ack_code, "1-#-4", next_if) # if 1 <= m
    # second if
    next_if = ["-4: #-4 - 1 ?"]  # m=m-1
    next_if.append("-3: 2 ?") # n=2
    add_goto(next_if, ack)
    add_if(ack_code, "1-#-3", next_if) # if 1 <= n
    # else
    ack_code.append("#-4 ?") # push m
    ack_code.append("#-4 - 1 ?") # param n-1
    add_call(ack_code, ack)
    ack_code.append("-5: #-2 ?") # n = res_call
    ack_code.append("0: -2 ?") # pop
    ack_code.append("-4: #-4 - 1 ?") # m=m-1
    add_goto(ack_code, ack)
    #
    main_code = ["#1 ?"]
    main_code.append("#2 ?")
    add_call(main_code, ack)
    main_code.append("0: -1 ?") # pop n
    return program([ack_code], main_code, numargs=2)

BIG = mk_big()
print("BIG = ")
print(BIG)
test2(big, BIG, 0, 8)
test2(big, BIG, 1, 15)
