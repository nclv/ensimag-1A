#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
VINCENT Nicolas

labyrinthe.py
"""


import numpy as np
from random import shuffle, randrange


def make_maze(width=8, height=5):
    """Génération d'un labyrinthe de taille height * width.

    Modélisation par des listes de height+1 lignes par width+1 colonnes.
    La dernière ligne et la dernière colonne servent de limites.
    """
    # liste des positions visitées
    visited = np.array([[0] * width + [1] for _ in range(height)] + [[1] * (width + 1)])
    # on alterne une ligne sur deux entre les séparations horizontales et les séparations verticales en commençant et finissant par les horizontales
    vertical = [["|  "] * width + ["|"] for _ in range(height)] + [[]]
    horizontal = [["+--"] * width + ["+"] for _ in range(height + 1)]

    def walk(x, y):
        """Algorithme récursif de parcours dans le labyrinthe.

        On reste sur la verticale:
            Quand on va vers le bas on modifie la case du bas
            Quand on va vers le haut on modifie la case actuelle
            --> on modifie (max(y, next_y), x)
        On reste sur l'horizontale:
            Quand on va vers la gauche on modifie la case actuelle
            Quand on va vers la doite on modifie la case de droite
            --> on modifie (y, max(x, next_x))

        """
        # la position (x, y) est visitée
        visited[y][x] = 1
        print(visited)

        # liste des directions possibles à partir de la position (x, y)
        directions = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        # randomize directions
        shuffle(directions)
        for (next_x, next_y) in directions:
            # si la position suivante est déjà visitée on passe à la direction suivante, c'est aussi la condition d'arrêt de walk
            if visited[next_y][next_x]:
                continue
            if next_x == x:
                horizontal[max(y, next_y)][x] = "+  "
            if next_y == y:
                vertical[y][max(x, next_x)] = "   "
            print(affichage(horizontal, vertical))
            # appel récursif
            walk(next_x, next_y)

    # On initie le parcours à partir d'une position aléatoire
    walk(randrange(width), randrange(height))

    return affichage(horizontal, vertical)


def affichage(horizontal, vertical):
    """Affichage."""
    maze_string = ""
    for (a, b) in zip(horizontal, vertical):
        maze_string += "".join(a + ["\n"] + b + ["\n"])
    return maze_string


if __name__ == "__main__":
    print(make_maze())
