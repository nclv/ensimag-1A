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

    Parameters:
        tableau (list): //
        pivot (int): //

    Returns:
        (list): liste d'éléments

    """
    indice_sauv = 0
    pivot = tableau[indice_pivot]
    indices = range(len(tableau)) #stable

    zipped = zip(indices, tableau)

    #tableau[-1], tableau[indice_pivot] = tableau[indice_pivot], tableau[-1]
    #indices[-1], indices[indice_pivot] = indices[indice_pivot], indices[-1] #stable
    zipped[-1], zipped[indice_pivot] = zipped[indice_pivot], zipped[-1]
    for courant, _ in enumerate(tableau):
        #print(tableau, indices, indices[courant])
        #stable
        if tableau[courant] == pivot and indices[courant] > indices[-1]:
            #tableau[-1], tableau[courant] = tableau[courant], tableau[-1]
            #indices[-1], indices[courant] = indices[courant], indices[-1]
            zipped[-1], zipped[courant] = zipped[courant], zipped[-1]
            #tableau[indice_sauv], tableau[courant] = tableau[courant], tableau[indice_sauv]
            #indices[indice_sauv], indices[courant] = indices[courant], indices[indice_sauv] #stable
            zipped[indice_sauv], zipped[courant] = zipped[courant], zipped[indice_sauv]
            indice_sauv += 1
        elif tableau[courant] <= pivot:
            #tableau[indice_sauv], tableau[courant] = tableau[courant], tableau[indice_sauv]
            #indices[indice_sauv], indices[courant] = indices[courant], indices[indice_sauv] #stable
            zipped[indice_sauv], zipped[courant] = zipped[courant], zipped[indice_sauv]
            indice_sauv += 1

    #tableau[-1], tableau[indice_sauv] = tableau[indice_sauv], tableau[-1]
    #indices[-1], indices[indice_sauv] = indices[indice_sauv], indices[-1]
    zipped[-1], zipped[indice_sauv] = zipped[indice_sauv], zipped[-1]
    #stable
    print(tableau, indices)
    return zipped[1]

def main():
    """main function

    """

    liste = [8, 4, 2, 2, 1, 7, 10, 5]
    liste1 = [3, 5, 5, 5, 5, 5, 5, 5, 6, 8, 9, 25, 2, 35, 7, 3, 10]
    print(liste1)
    print(pivote1(liste1, 6), pivote2(liste1, 6))

main()
