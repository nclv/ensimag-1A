# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Nicolas VINCENT

import sys
sys.getrecursionlimit()

from functools import lru_cache
@lru_cache(maxsize=None)
"""


import math


def syracuse(n):
    """Suite de syracuse récursive."""

    if n == 1:
        return [1]
    elif n % 2:
        return [n] + syracuse(n * 3 + 1)
    else:
        return [n] + syracuse(n / 2)


def etapes(nombre):
    """Renvoie le nombre d'étapes pour arriver à la fin de l'algorithme."""

    if nombre == 1:
        return 0
    elif nombre % 2:
        return 1 + etapes(nombre * 3 + 1)
    else:
        return 1 + etapes(nombre / 2)


def exponentiation(nombre, exposant):
    """exponentiation."""

    if exposant == 0:
        return 1
    elif exposant == 1:
        return nombre
    elif exposant == 2:
        return nombre * nombre
    elif exposant % 2 != 0:
        return nombre * exponentiation(nombre, exposant - 1)
    elif exposant % 2 == 0:
        return exponentiation(nombre, exposant // 2) * exponentiation(
            nombre, exposant // 2
        )



def binarySearch(arr, l, r, x):
    """Returns index of x in arr if present, else -1"""
    # Check base case
    if r >= l:
        mid = l + (r - l) / 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        # Else the element can only be present in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1


def main():
    """main function"""

    nombre = 10
    print(etapes(nombre))


if __name__ == "__main__":
    main()
