#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test the calculator in infix syntax
"""

import test_parser
from calc import parse

test_parser.PARSER_NAME='calc'
test_parser.PARSER_UNDER_TEST=parse

from test_parser import test_result, test_parsing_error

# exemples basiques
test_result("  \n \n  ",[])
test_result("7?",[7])
test_result("123+321?",[444])

test_result("3 * 4 + 1 - 3 ? #1 * (#1 / 2) ?", [10, 50])
test_result("1 + 2 * 3 ? -4 + #1 * #1 ?", [7, 45])
test_result("2*3 + 1 ? #1 * #1 - 4 ?", [7, 45])
test_result("1 - 1 - 1 ? 1 - (1 - 1) ?", [-1, 1])  
test_result("1 - - 1 - 1 ? 1 - (-1 - 1) ? 1 - -(1 - 1) ?", [1, 3, 1])          
test_result("60 / 10 / 2 ? 60 / (10 / 2) ?", [3, 12])
test_result("- ((1 + 2) * - ((3 - 5))) ? ", [-6])
           
# tests autour de n*(n+1)/2
N1 = 20
test_result("1?" + "".join(["{0}+#{1}?".format(i,i-1) for i in range(2,N1)]),
            [i * (i+1)//2 for i in range(1,N1)])
    
r = [i for i in range(1,N1)]
r.append((N1-1)*N1//2)
l = [str(i)+"?" for i in range(1,N1)]
for i in range(1, N1-1):
    l.append("#{0}+".format(i))
l.append("#{0}?".format(N1-1))
test_result("".join(l), r)

test_parsing_error("?")
test_parsing_error("123+321")
test_parsing_error("123+321? 1")
test_parsing_error("3 * 4 + 1 - 3 ? #1 (#1 / 2) ?")
test_parsing_error("3 * / 1 - 3 ? #1 * (#1 / 2) ?")
test_parsing_error("3 * 4 + 1 - 3 #1 * (#1 / 2) ?")
test_parsing_error("(1 2 ?")
test_parsing_error("- ((1 + 2 * - ((3 - 5))) ? ")
test_parsing_error("- (1 + 2)) * - ((3 - 5)) ? ")
