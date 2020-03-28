#!/usr/bin/env python3

def image(tuple):
        return "(" + ", ".join(tuple) + ")"

import sys

def exec_arg(proc, arg2):

    def usage(nom_arg):
        print("Usage :", sys.argv[0], "fichier_MT", nom_arg, "[ T | P]",
              file = sys.stderr)
        print("        (T pour tracer l'execution)",
              file = sys.stderr)
        print("        (P pour tracer en pas à pas l'execution)",
              file = sys.stderr)
        sys.exit(1)

    if not (3 <= len(sys.argv) <= 4):
        usage(arg2)
    try:
        if len(sys.argv) == 3:
            proc(sys.argv[1], sys.argv[2], False, False)
        elif (sys.argv[3] == 'T'):
            proc(sys.argv[1], sys.argv[2], True, False)
        elif (sys.argv[3] == 'P'):
            proc(sys.argv[1], sys.argv[2], True, True)
        else:
            usage(arg2)
    except AssertionError as err:
        print("ERREUR : " + err.args[0], file = sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    print(image (("bonjour", "42, ", "au revoir")))

    def test(arg1, arg2, arg3, arg4):
        print("test", arg1, arg2, arg3, arg4)
    exec_arg(test, "l_arg2")
