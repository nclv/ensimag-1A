#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Nicolas Vincent
https://chamilo.grenoble-inp.fr/courses/ENSIMAG3MMBPI/document/tps/tpsse8.html
"""


from random import randint


def en_tete(width, height):
    """Affiche l'en-tête de l'image bitmap

    Parameters:
        width (int): largeur
        height (int): hauteur

    """
    print("P2")
    print(width, height)
    print("255")


def disque_aleat(width, height):
    """Crèe un disque dans le rectangle

    Parameters:
        width (int): largeur
        height (int): hauteur

    Returns:
        centre (list): coordonnées (x, y)
        rayon (int)

    """
    centre = [randint(1, width), randint(1, height)]
    rayon = randint(1, min(centre[0], centre[1], width - centre[0], height - centre[1]))
    #print(centre, rayon)

    return centre, rayon

def test_in_circle(cercle, point):
    """Test si le pixel est dans le cercle

    Parameters:
        cercle (list): coordonnées du cercle (x, y) et son rayon
        point (int): coordonnées du point à tester (x, y)

    Returns:
        (bool): is_in_circle

    TODO: Implémenter avec les objets cercle et point pour plus de lisibilite

    """

    return (point[0] - cercle[0][0])**2 + (point[1] - cercle[0][1])**2 <= cercle[1]**2

def main():
    """main function

    """
    #print("Entrer les dimensions de l'image (largeur hauteur): ")
    width, height = int(input()), int(input())

    en_tete(width, height)
    cercle_1 = disque_aleat(width, height)
    cercle_2 = disque_aleat(width, height)

    for pixel_y in range(height):
        for pixel_x in range(width):
            point = (pixel_x, pixel_y)
            if test_in_circle(cercle_1, point) or test_in_circle(cercle_2, point):
                print(randint(0, 255), end=" ")
            else:
                print(255, end=" ")
        print()

main()
