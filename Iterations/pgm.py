#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Nicolas Vincent
https://chamilo.grenoble-inp.fr/courses/ENSIMAG3MMBPI/document/tps/tpsse8.html
"""


from random import randint


def en_tete(width, height):
    """Affiche l'en-tête de l'image bitmap

    """
    print("P2")
    print(width, height)
    print("255")

def disque_aleat(width, height):
    """Crèe un disque dans le rectangle délimité par image_dimension

    """
    centre = [randint(0, max(width, height)), randint(0, max(width, height))]
    rayon = randint(0, max(width, height)/2)
    return centre, rayon

def main():
    """main function

    """
    print("Entrer les dimensions de l'image (largeur hauteur): ")
    width, height = int(input()), int(input())

    en_tete(width, height)
    centre, rayon = disque_aleat(width, height)

    for pixel_x in range(width):
        for pixel_y in range(height):
            if (pixel_x - centre[0])**2 + (pixel_y - centre[1])**2 <= rayon**2:
                print(randint(0, 255), end=" ")
            else:
                print(255, end=" ")
        print()

main()
