# -*- coding: utf-8 -*-
#!/usr/bin/env python3


"""
Nicolas VINCENT
"""

from functools import lru_cache

def evalue(poly, inconnue):
    """Evaluation d'un polynôme par schéma de Horner

    x^5 + 3x^2 - 8x + 3 = 3 + x(-8 + x(3 + x(1 + 0x)))
    s'écrit [3, -8, 3, 1]

    Parameters:
        poly (list): coeffciients du polynôme
        inconnue (float): valeur évaluée

    Returns:
        P(x)
    """
    somme = 0
    for coeff in reversed(poly):
        somme = somme * inconnue + coeff
    return somme

def indice_max1(tableau):
    """Renvoie le(s)indice(s) du maximum du tableau

    Parameters:
        tableau (list): //

    """
    return [indice for indice, value in enumerate(tableau) if value == max(tableau)]

def indice_max2(tableau):
    """Renvoie le(s)indice(s) du maximum du tableau

    Parameters:
        tableau (list): //

    """
    maximum = float("-inf")
    indices = []
    for indice, value in enumerate(tableau):
        if value > maximum:
            maximum = value
            indices = []
        if value == maximum:
            indices.append(indice)
    return indices

@lru_cache(maxsize=1000)
def syracuse_cached(terme_i):
    """Conjecture de Syracuse

    u(i) pair : u(i+1) = u(i)/2
    u(i) impair : u(i+1) = 3u(i) + 2

    Parameters:
        terme_i (int): u(i)

    Returns:
        Renvoie le terme suivant de la suite

    """
    return terme_i / 2 if not terme_i % 2 else 3 * terme_i + 1

def syracuse(terme_i):
    """Conjecture de Syracuse

    u(i) pair : u(i+1) = u(i)/2
    u(i) impair : u(i+1) = 3u(i) + 2

    Parameters:
        terme_i (int): u(i)

    Returns:
        Renvoie le terme suivant de la suite

    """
    return terme_i / 2 if not terme_i % 2 else 3 * terme_i + 1

def etapes_av_1(terme_0):
    """Renvoie le nombre d'étapes jusqu'à atteindre 1

    Parameters:
        terme_0 (int): valeur initiale

    """
    compteur = 0
    next_terme = terme_0
    while next_terme != 1:
        next_terme = syracuse(next_terme)
        compteur += 1
    return compteur

def etapes_av_1_cached(terme_0, cache):
    """Renvoie le nombre d'étapes jusqu'à atteindre 1

    Parameters:
        terme_0 (int): valeur initiale

    """
    compteur = 0
    next_terme = terme_0
    while next_terme != 1:
        if next_terme in cache:
            compteur += cache[next_terme]
            break
        next_terme = syracuse(next_terme)
        compteur += 1
        cache[terme_0] = compteur
    return compteur

def est_injective(cache):
    """Renvoie si la fonction est injective

    Parameters:
        cache (dict): (x: f(x))

    """
    return len(cache.values()) == len(set(cache.values()))

def length_leq_1():
    """Crè 100 points aléatoires, filtre les points de distance à l'origine inférieure à 1

    """
    from random import random

    rand_numbers = [(random(), random()) for _ in range(100)]
    filtre_points = (p for p in rand_numbers if p[0] * p[0] + p[1]* p[1] <= 1.0)


def main():
    """main function

    """

    import time

    start = time.time()
    print(indice_max1([1, 2, 3, 2, 3, 4, 5, 4, 5]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(indice_max2([1, 2, 3, 2, 3, 4, 5, 4, 5]))
    end = time.time()
    print(end - start)

    start = time.time()
    print("syr", syracuse(203547858932))
    end = time.time()
    print(end - start)

    start = time.time()
    print("syr_cached", syracuse_cached(203547858932))
    end = time.time()
    print(end - start)

    start = time.time()
    print("etape", etapes_av_1(2035478589323834990494984848))
    end = time.time()
    print(end - start)

    start = time.time()
    print("etape_cached", etapes_av_1_cached(2035478589323834990494984848, {}))
    end = time.time()
    print(end - start)


main()
