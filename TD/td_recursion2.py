# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Nicolas VINCENT
"""


class Cellule:

    """Classe représentant un noeud

    Attributes:
         valeur ():
         nextcellule ():

    """

    def __init__(self, bit, suivante=None):
        """Constructeur de la cellule

        """
        self.bit = bit
        self.suivante = suivante

    def __str__(self):
        """Affichage."""
        return self.suivante.__str__() + str(self.bit) if self.suivante else str(self.bit)


def valeur(entier_liste):
    """Renvoie l'entier sous forme décimale.

    Parameters:
        entier_liste (Cellule): entier codé avec la liste de bits

    """
    return 2 * valeur(entier_liste.suivante) + entier_liste.bit if entier_liste else 0


def construit_liste(entier):
    """Construit une liste à partir de l'entier sous forme décimale."""
    return Cellule(entier % 2, construit_liste(entier // 2)) if entier else None


def successeur(entier_liste):
    """Renvoie entier_liste + 1.

    Parameters:
        entier_liste (Cellule): entier codé avec la liste de bits

    """
    if not entier_liste:
        return Cellule(1)
    # cas impair
    if entier_liste.bit:
        entier_liste.suivante = successeur(entier_liste.suivante)

    entier_liste.bit = 1 - entier_liste.bit
    return entier_liste


def ajout(liste1, liste2):
    """Renvoie liste1 + liste2."""

    if liste2 is None:
        return liste1
    if liste1 is None:
        return liste2
    # vaut 0, 1 ou 2
    addition_bits = liste1.bit + liste2.bit
    bit_faible = addition_bits % 2
    bits_forts = ajout(liste1.suivant, liste2.suivant)
    # propagation de la retenue
    if addition_bits == 2:
        bits_forts = successeur(bits_forts)

    return Cellule(bit_faible, bits_forts)
