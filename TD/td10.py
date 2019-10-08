# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Nicolas Vincent - Tri

En place : modification du tableau à trier
Stable : if two objects with equal keys appear in the same order in sorted output
as they appear in the input array to be sorted.
"""

def insertionsort(a):
    """Tri par insertion

    L'objectif d'une étape est d'insérer le i-ème élément à sa place parmi ceux qui précèdent.
    Il faut pour cela trouver où l'élément doit être inséré en le comparant aux autres,
    puis décaler les éléments afin de pouvoir effectuer l'insertion.
    En pratique, ces deux actions sont fréquemment effectuées en une passe,
    qui consiste à faire « remonter » l'élément au fur et à mesure jusqu'à rencontrer
    un élément plus petit.

    >>> insertionsort([6, 4, 8, 2, 1, 9, 10])
    [1, 2, 4, 6, 8, 9, 10]

    """
    for i, item in enumerate(a):
        #item = a[i]
        j = i
        while j > 0 and a[j - 1] > item:
            a[j] = a[j - 1]
            j -= 1
        a[j] = item
    return a

def selection_sort(lst):
    for i, value in enumerate(lst):
        mn = min(range(i, len(lst)), key=lst.__getitem__)
        lst[i], lst[mn] = lst[mn], value
    return lst

def selection_sort1(seq):
    """Trie par sélection - in-place comparison

    rechercher le plus petit élément du tableau, et l'échanger avec l'élément d'indice 0 ;
    rechercher le second plus petit élément du tableau, et l'échanger avec l'élément d'indice 1 ;
    continuer de cette façon jusqu'à ce que le tableau soit entièrement trié.

    """
    for i in range(0, len(seq)):
        iMin = i
        for j in range(i + 1, len(seq)):
            if seq[iMin] > seq[j]:
                iMin = j
        if i != iMin:
            seq[i], seq[iMin] = seq[iMin], seq[i]

    return seq

def merge(left, right):
    """Takes two sorted sub lists and merges them in to a single sorted sub list.

    """
    result = []
    n, m = 0, 0
    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            result.append(left[n])
            n += 1
        else:
            result.append(right[m])
            m += 1

    result += left[n:]
    result += right[m:]
    return result


def merge_sort(seq):
    """Tri fusion

    Si le tableau n'a qu'un élément, il est déjà trié.
    Sinon, séparer le tableau en deux parties à peu près égales.
    Trier récursivement les deux parties avec l'algorithme du tri fusion.
    Fusionner les deux tableaux triés en un seul tableau trié.

    """
    if len(seq) <= 1:
        return seq

    middle = int(len(seq) // 2)
    left = merge_sort(seq[:middle])
    right = merge_sort(seq[middle:])
    return merge(left, right)

### COURS ###

def tri_insertion(tableau):
    """Trie par insertion - del/insert BAD

    """
    for indice, value in enumerate(tableau):
        del tableau[indice]
        tableau.insert(bonne_place(tableau[:indice], value), value)

def bonne_place(sorted_table, value):
    """Renvoie l'indice où insérer l'élément

    """
    for indice, sorted_value in enumerate(sorted_table):
        if sorted_value > value:
            return indice
    return len(sorted_table)

def tri_selection(tableau):
    """Trie sélection

    """
    for indice in range(len(tableau) - 1):
        indice_min = indice + trouve_min(tableau[indice:])
        tableau[indice_min], tableau[indice] = tableau[indice], tableau[indice_min]

def trouve_min(tableau):
    return tableau.index(min(tableau))

def fusion_tableaux(tableaux):
    fusion = []
    positions = [0]*len(tableaux)
    while True:
        el_courants = [t, positions[i] for i, t in enumerate(tableaux)]
        indice_plus_petit = el_courants.index(min(el_courants))

        fusion.append(el_courants[indice_plus_petit])
        positions[indice_plus_petit] += 1
        if positions[indice_plus_petit] >= len(tableaux[indice_plus_petit]):
            autre = 1 - indice_plus_petit
            fusion.extend(tableaux[autre][positions[autre:]])
            return False
