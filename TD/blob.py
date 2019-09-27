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

    !Dépendant de la modélisation

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
        for colonne in range(max(0, colonne_courante - portee), \
        min(8, colonne_courante + portee + 1)):
            voisin = ligne*8 + colonne
            if voisin != position:
                yield voisin

def mouvements_possibles(plateau, couleur):
    """Renvoie tous les mouvements possibles d'une couleur

    """
    for posinitiale in blob(plateau, couleur):
        for posfinale in positions_voisines(plateau):
            yield posinitiale, posfinale

"""
Modélisation avec des bits:
 - stockage dans int 64bits (par couleur)
 - pions[bleu, rouge]

basculer bit n°9 en bleu
pions[0] |= 1 << 9 (ou logique)
enlever pion rouge sur la case 12
pions[1] &= ~(1 << 12)
"""

def get_position(entier):
    """Itérateur renvoyant la position là où il y a un 1.

    """
    bits = entier
    position = 0
    while bits != 0:
        if bits % 2:
            yield position
        bits >>= 1
        position += 1

def valeurb(pions):
    """Calcul des points: nb.rouges - nb.bleus

    !Dépendant de la modélisation

    Parameters:
        pions (list): tableau 1D: 2 cases (bleu, rouge)

    """

    total = 0
    for _ in get_position(pions[0]):
        total -= 1
    for _ in get_position(pions[1]):
        total += 1
    return total

def calcul_voisin(position):
    """Renvoie l'entier correspondant aux voisins
    sum(2^numéro_case_voisin)

    """
    bits = 0
    for voisin in positions_voisines(position, portee=1):
        bits += 1 << voisin
    return bits

def jouer_saut(pions, coup, couleur, voisins):
    """Modifie l'état des blobs pour que le coup (saut) du joueur

    0 sur case de départ
    1 sur case cible
    contamination voisins

    coup = (depart, arrivee)
    voisin case arrivée
    """

    depart, arrivee = coup
    pions[couleur] |= 1 << arrivee #pose arrivee
    pions[couleur] &= ~(1 << depart) #enlève depart
    adversaire = ~couleur #contamine les voisins
    voisins_changes = pions[adversaire] & voisins[arrivee]

    pions[adversaire] &= ~voisins_changes #enlève
    pions[couleur] |= voisins_changes #pose
