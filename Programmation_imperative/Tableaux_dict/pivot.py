# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Nicolas VINCENT
https://chamilo.grenoble-inp.fr/courses/ENSIMAG3MMBPI/document/tps/tpsse13.html#tailtpsse13.html
"""

def pivote1(tableau, indice_pivot):
    """Renvoie deux listes d'éléments du tableau au dessus et en dessous du pivot

    Parameters:
        tableau (list): //
        pivot (int): //

    Returns:
        (list): listes d'éléments ordonnées autour du pivot

    """
    temp_tableau = tableau[:]
    pivot = temp_tableau[indice_pivot]
    temp_tableau.remove(pivot)
    list1, list2 = [], []
    for element in temp_tableau:
        if element <= pivot:
            list1.append(element)
        else:
            list2.append(element)

    #print(list1, list2)
    return list1 + [pivot] + list2

def pivote2(tableau, indice_pivot):
    """Renvoie deux listes d'éléments du tableau au dessus et en dessous du pivot
    (inplace sans le zip et stable)

    Parameters:
        tableau (list): //
        pivot (int): //

    Returns:
        (list): liste d'éléments

    """
    indice_sauv = 0
    pivot = tableau[indice_pivot]
    indices = range(len(tableau)) #pour la stabilité

    zipped = [list(couple) for couple in zip(indices, tableau)]

    zipped[-1], zipped[indice_pivot] = zipped[indice_pivot], zipped[-1]
    for courant, _ in enumerate(tableau):
        if zipped[courant][1] == pivot and zipped[courant][0] > zipped[-1][0]:
            zipped[-1], zipped[courant] = zipped[courant], zipped[-1]
            zipped[indice_sauv], zipped[courant] = zipped[courant], zipped[indice_sauv]
            indice_sauv += 1
        elif zipped[courant][1] <= pivot:
            zipped[indice_sauv], zipped[courant] = zipped[courant], zipped[indice_sauv]
            indice_sauv += 1

    zipped[-1], zipped[indice_sauv] = zipped[indice_sauv], zipped[-1]
    indices, tableau = list(zip(*zipped))
    #print(tableau, indices)
    return list(tableau)

def main():
    """main function

    """

    liste = [8, 4, 2, 2, 1, 7, 10, 5]
    liste1 = [3, 5, 5, 5, 5, 5, 5, 5, 6, 8, 9, 25, 2, 35, 7, 3, 10]
    print(liste1)
    print(pivote1(liste1, 6), pivote2(liste1, 6))

main()
