#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Nicolas VINCENT
"""


import random


def somme_alea(nombre_des):
    """Renvoie la somme du résultat du lancer de nombre_des.

    Les dés sont à 6 faces.

    Parameters:
        nombre_des (int): //

    """
    return random.randint(1, 6) + somme_alea(nombre_des - 1) if nombre_des else 0


def lancers(nombre_des, des):
    """Affiche toutes les combinaisons possibles.

    Parameters:
        nombre_des (int): //
        des (list): stocke la combinaison courante des dés jetés.

    """
    if nombre_des:
        for resultat in range(1, 7):
            des[nombre_des - 1] = resultat
            lancers(nombre_des - 1, des)
    else:
        print(des)


def lancers_somme_contrainte(nombre_des, des, somme_demandee):
    """Affiche toutes les combinaisons.

    Celles contenant la somme demandée seront encadrées par **.

    """
    if nombre_des:
        for resultat in range(1, 7):
            des[nombre_des - 1] = resultat
            lancers_somme_contrainte(nombre_des - 1, des, somme_demandee)
    else:
        if sum(des) == somme_demandee:
            print("*", des, "*")
        else:
            print(des)


def occurences_somme(nombre_des, somme_demandee):
    """Renvoie le nombre de combinaisons atteignant la somme donnée."""
    if nombre_des:
        if nombre_des * 6 < somme_demandee < nombre_des:
            return 0
        compteur = 0
        for resultat in range(1, 7):
            compteur += occurences_somme(nombre_des - 1, somme_demandee - resultat)
        return compteur
    else:
        if somme_demandee == 0:
            return 1
        else:
            return 0


def combinaisons_valides(nombre_des, des, fonction_validation):
    """Renvoie le nombre de combinaisons vérifiant la fonction de validation."""
    if nombre_des:
        compteur = 0
        for resultat in range(1, 7):
            des[nombre_des - 1] = resultat
            compteur += lancers_somme_contrainte(nombre_des - 1, des, fonction_validation)
        return compteur
    else:
        return bool(fonction_validation(des))


def main():
    """main function."""
    lancers(3, [0] * 3)
    #lancers_somme_contrainte(3, [0] * 3, 18)
    print(occurences_somme(3, 4))


if __name__ == "__main__":
    main()
