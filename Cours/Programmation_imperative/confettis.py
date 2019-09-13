#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from tycat import data_tycat

class Disque:
    def __init__(self, rayon):
        self.rayon = rayon
        self.couleur = couleur_aleatoire()
        self.centre = randint(0, 100), randint(0, 100)

    def affiche(self):
        print('<circle cx="{}" cy="{}" r="{}" fill="rgb{}"/>'.format(self.centre[0], self.centre[1], self.rayon, self.couleur))

def couleur_aleatoire():
    return randint(0, 255), randint(0, 255), randint(0, 255)


class Image:
    def __init__(self):
        self.disques = []

    def __bool__(self):
        return len(self.disques) != 0

    def ajout_disque(self, rayon):
        self.disques.append(Disque(rayon))

    def affiche(self):
        if self:
            print("<svg height=\"100\" width=\"100\">")
            for disque in self.disques:
                disque.affiche()
            print("</svg>")


def main():
    image = Image()
    for _ in range(200):
        image.ajout_disque(randint(5, 20))
    image.affiche()
    # data_tycat(disques)

main()
