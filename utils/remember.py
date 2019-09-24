# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Patterns
"""

failed = False
for other_room in rooms:
    if test(other_room):
        failed = True
        break
failed = any(test(other_room) for other_room in rooms)


for room in rooms:
    if in_and_side_room((absc, ordo), room):
        board[absc][ordo] = 1
        break
board[absc][ordo] = any(in_and_side_room((absc, ordo), room) for room in rooms)
