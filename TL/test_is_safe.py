#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ci-dessous une tentative d'implémentation d'un programme "is_safe(val, prog)" qui étant donné:
#   1) une chaine de nom "val"
#   2) une chaîne de nom "prog" représentant un programme Python qui termine toujours
#      (et dont le code comporte éventuellement une variable de nom "arg")
# détermine si l'exécution de "prog" termine sans erreur sous la précondition "arg==val".

def is_safe(val, prog):
    run_prog = "arg={0};{1}".format(repr(val), prog)
    try:
        exec(run_prog)
        print(repr(run_prog), "terminates without error.")
        return True
    except Exception as e:
        print(repr(run_prog), "fails on", repr(e))
        return False

is_safe('5', "assert arg == '5'")
print("---")

is_safe('4', "assert arg == '5'")
print("---")

is_safe('4', "assert not arg == arg")
print("---")

is_safe('assert 2+2=4', "assert arg")
print("---")

is_safe('arg', "arg")
print("---")

is_safe('False', "assert is_safe(arg, arg)")
print("---")

# Question subsidiaire 1: qu'affiche cette ligne ?
# is_safe("assert is_safe(arg, arg)", "assert is_safe(arg, arg)")

# Question subsidiaire 2: trouver une entrée "(val, prog)" de "is_safe" pour laquelle son résultat est faux
# (Elle ne fait pas ce qu'elle prétend faire).
