# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Classe point
"""


from random import randint


class Point:

    """Classe Point

    Attributes:
        coordonnee (list): coordonnee du Point

    """

    def __init__(self, coordonnee):
        """Constructeur.

        Parameters:
            coordonnee (type): description

        """
        self.absc, self.ord = coordonnee

def random_point(delimitation_x, delimitation_y):
    """Crèe un point aléatoire

    """
    return Point([randint(*delimitation_x), randint(*delimitation_y)])
