"""
Fournit une classe Segment codant un segment du plan.
"""
from random import random


def point_aleatoire():
    """
    renvoie un point du plan de coordonnees aleatoires
    entre 0 et 800
    """
    return (random()*800, random()*800)


def segment_aleatoire():
    """
    renvoie un segment du plan de coordonnees aleatoires
    entre 0 et 800
    """
    return Segment(point_aleatoire(), point_aleatoire())


class Segment:
    """
    Un segment du plan.
    """

    def __init__(self, debut, fin):
        """
        Prend deux points (couples de coordonnees flottantes) en argument
        et cree un nouveau segment.
        """
        self.debut = debut
        self.fin = fin

    def affiche(self):
        print('<line x1="{}" x2="{}" y1="{}" y2="{}" \
stroke="orange" fill="transparent" stroke-width="5"/>'.format(self.debut[0], self.fin[0], self.debut[1], self.fin[1]))
