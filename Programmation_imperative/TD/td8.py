# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Nicolas VINCENT
"""


from random import random, randrange
from itertools import combinations
from math import sqrt


LIMIT = 10e9


def create_float(maximum):
    """Crè n flottants aléatoires

    """
    return [LIMIT * random() for _ in range(maximum)]

def leq_seuil(tableau, seuil):
    """Renvoie les éléments du tableau inférieurs au seuil

    """
    return list(filter(lambda x: x <= seuil, tableau))

def random_points(maximum):
    """Renvoie un tableau de n points aléatoires

    """
    return [(randrange(0, 50), randrange(0, 50)) for _ in range(maximum)]

def calcule_distance(point1, point2):
    """Calcule la distance entre deux points

    """
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def points_plus_proches(points):
    """Renvoie les deux points les plus proches

    """
    dist_min = float("+ inf")
    for point1, point2 in combinations(points, 2):
        distance = calcule_distance(point1, point2)
        if distance < dist_min:
            dist_min = distance
            plus_proches = (point1, point2)

    return plus_proches

def est_premier(candidat, premiers_connus):
    """Renvoie si le nombre est premier (divisible par un premier)

    """
    indice_courant = 0
    while premiers_connus[indice_courant] <= sqrt(candidat):
        if candidat % premiers_connus[indice_courant] == 0:
            return False
        indice_courant += 1
    return True


def calcul_premier(nombre):
    """Renvoie une liste de nombres premiers

    """
    premiers = [2]
    courant = 3
    while len(premiers) < nombre:
        if est_premier(courant, premiers):
            premiers.append(courant)
        courant += 2
    return premiers

def main():
    """main function

    """

    print(create_float(10))
    print(leq_seuil(range(10), 5))

main()
