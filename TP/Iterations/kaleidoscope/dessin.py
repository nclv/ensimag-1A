# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Classe dessin
"""


from random import randint


def entete(largeur, hauteur):
    """Affiche l'en-tête.

    Parameters:
        largeur (float): largeur de l'image
        hauteur (float); hauteur de l'image

    Returns:
        (type): en-tête

    """
    print(f"<svg height='{hauteur}' width='{largeur}'>")

def pied():
    """Pieds svg

    """
    print("</svg>")

def couleur_aleatoire():
    """Oneline description.

    Returns:
        (type): description

    """
    random_color = lambda: randint(0, 255)

    return f'#{random_color():02X}{random_color():02X}{random_color():02X}'

def affiche_triangle(triangle, couleur):
    """Oneline description.

    Parameters:
        triangle (type): description
        couleur ():

    Returns:
        (type): description

    """
    format_point = lambda i: str(triangle.points[i].absc) + "," + str(triangle.points[i].ord)

    print(f"<polygon points='{format_point(0)} {format_point(1)} {format_point(2)}' \
        style='fill:{couleur};stroke:{couleur};stroke-width:1' />")
