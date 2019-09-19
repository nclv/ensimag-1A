# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Nicolas Vincent
Jeu de plateau 8*8, rouge/bleu, tour par tour
 - mouvement sur une des 9 cases voisines --> duplication du pion
 - saut sur les deuxièmes cases voisines --> contamination sans duplication
"""


def valeur(plateau):
    """Calcul des points : nb.rouges - nb.bleus

    Dépendant de la modélisation

    Parameters:
        plateau (list): tableau 1D: 64 cases (0, 1, -1) <--> (rien, rouge, bleu)
    """
    return sum(plateau)

def blob(plateau, couleur):
    """Générateur des indices de placement d'une couleur

    """
    for indice, value in enumerate(plateau):
        if value == couleur:
            yield indice

def pos2d(position):
    """Passage de 1D à 2D

    """
    return position // 8, position % 8

def positions_voisines(position, portee=2):
    """Retourne les positions voisines dans un rayon de deux cases

    On boucle sur un carré autour de position, en faisant attention aux bornes

    Parameters:
        position (int): position du pion
        portee (int): //
    """
    ligne_courante, colonne_courante = pos2d(position)
    for ligne in range(max(0, ligne_courante - portee), min(8, ligne_courante + portee + 1)):
        for colonne in range(max(0, colonne_courante - portee), min(8, colonne_courante + portee + 1)):
            voisin = ligne*8 + colonne
            if voisin != position:
                yield voisin

def mouvements_possibles(plateau, couleur):
    """Renvoie tous les mouvements possibles d'une couleur

    """
    for posinitiale in blob(plateau, couleur):
        for posfinale in positions_voisines(plateau):
            yield posinitiale, posfinale
