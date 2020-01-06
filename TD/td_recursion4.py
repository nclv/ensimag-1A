#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Nicolas VINCENT

Partitionner l'ensemble E en deux ensembles tels que:
 - E1 inter E2 = 0
 - E1 U E2 = E
 - sum(E1) = sum(E2)

on stocke une partition par n bits (1 si dans E1, 0 si dans E2)
"""


def solutions_valides_rec(entiers, cible):
    """Renvoie le nombre de solutions valides différentes.
    """
    if entiers:
        if sum(entiers) < cible:
            return 0
        else:
            entier = entiers.pop()
            # partition atteindre avec ou sans entier
            compte = solutions_valides_rec(entiers, cible) + solutions_valides_rec(
                entiers, cible - entier
            )
            entiers.append(entier)
            return compte
    else:
        if cible == 0:
            return 1  # une solution de plus
        else:
            return 0


def solutions_valides_it(entiers, cible):
    """Même fonction en itératif.

    bits énumere les bits d'un entier
    """
    compte = 0
    premier = entiers.pop()
    cible -= premier
    for solution in range(0, 2**len(entiers)):
        valeur = sum([b * entiers[i] for i, b in enumerate(bits(solution))])
        if valeur == cible:
            compte += 1
    entiers.append(premier)
    return compte


"""
échiquier n*n
n reines
menace : pas deux reines sur les mêmes lignes, colonnes, diagonales
fonction récursive
"""

def n_reines(reines, taille):
    """Placer n reines sur un échiquier n*n. taille=n
    reines est la liste des positions des reines
    """
    if configuration_invalide(reines):
        return 0
    if len(reines) == taille:
        return 1
    compte = 0
    for colonne in range(taille):
        reines.append(colonne)
        compte += n_reines(reines, taille)
        reines.pop()
    return compte


def main():
    entiers = [20, 4, 7, 20, 16, 5]
    n = solutions_valides_rec(entiers, 20)
    print(n)


if __name__ == "__main__":
    main()
