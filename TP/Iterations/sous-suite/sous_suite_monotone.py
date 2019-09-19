# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Nicolas Vincent
https://chamilo.grenoble-inp.fr/courses/ENSIMAG3MMBPI/document/tps/tpsse11.html
"""


import sys


def get_numbers():
    """Renvoie les nombres du (ou des) fichier(s) dans une seule liste

    """
    with open(sys.argv[1], 'r') as file:
        return iter(file.read().split())

def get_suites():
    """Renvoie les suites monotones

    """

    numbers = get_numbers()
    suite = [next(numbers, None)]
    monotonie = None
    while numbers:
        try:
            first = suite[-1]
            second = next(numbers)
            #print("second", second)
            if second < first:
                #print("décroissante")
                if monotonie: #détecte le changement de monotonie
                    yield suite
                    suite = [first]
                suite.append(second)
                #print(suite)
                monotonie = 0
            elif second > first:
                #print("croissante")
                if not monotonie: #détecte le changement de monotonie
                    yield suite
                    suite = [first]
                suite.append(second)
                #print(suite)
                monotonie = 1
            elif second == first:
                suite.append(second)
                #print(suite)
            else:
                yield suite
                suite = [first]
        except StopIteration:
            yield suite
            break

def get_max_suite():
    """Get the biggest sequence

    """
    return max([suite for suite in get_suites()], key=len)

def main():
    """main function

    """

    biggest_suite = get_max_suite()
    print(biggest_suite)

main()
