#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test the calculator in prefix syntax
"""

import test_parser
from pcalc import parse

test_parser.PARSER_NAME='pcalc'
test_parser.PARSER_UNDER_TEST=parse

from test_parser import test_result, test_parsing_error

# exemples basiques
test_result("?7",[7])
test_result("?+123 321",[444])



# exemple du sujet
test_result("? + * 3 4 + 1 -3 ? * #1 / #1 2", [10, 50])

# tests autour de n*(n+1)/2
N1 = 20
test_result("?1" + "".join(["?+{0}#{1}".format(i,i-1) for i in range(2,N1)]),
            [i * (i+1)//2 for i in range(1,N1)])

l = ["?"+str(i) for i in range(1,N1)]
l.append("?")
l.append("+"*(N1-2))
for i in range(1, N1):
    l.append("#"+str(i))
r = [i for i in range(1,N1)]
r.append((N1-1)*N1//2)
test_result("".join(l), r)

l = ["?"+str(i) for i in range(1,N1)]
l.append("?")
for i in range(1, N1-1):
    l.append("+#"+str(i))
l.append("#"+str(N1-1))
test_result("".join(l), r)



# erreur basique
test_parsing_error("?")

# erreurs à partir de l'exemple du sujet
test_parsing_error("? + + 3 4 + 1 3 * #1 / #1 2")
test_parsing_error("? + + 3 4 + 1 3 ? ? * #1 / #1 2")
test_parsing_error("? + + 3 4 + 1 3 ? #1 / #1 2")
test_parsing_error("? + * 3 4 + 1 ? * #1 / #1 2")
test_parsing_error("? + * 3 4 + 1 3 5 ? * #1 / #1 2")
