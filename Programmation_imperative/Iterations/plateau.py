# -*- coding: utf-8 -*-
#!/usr/bin/env python3


"""
plateau.
"""

import sys


BLACK = "#000000"
WHITE = "#ffffff"


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

def plateau(largeur, hauteur):
    """Oneline description.

    Parameters:
        largeur, hauteur (int): /

    """
    entete(largeur, hauteur)

    square = 40

    x_list = list(range(0, largeur, square))[:largeur//square]
    y_list = list(range(hauteur, -1, -square))

    for indicey, ordonnee in enumerate(y_list):
        for abscisse in x_list:
            if indicey % 2 == 1:
                print(f"<rect fill='{WHITE}' stroke='{BLACK}' width='{square}' height='{square}' \
                    y='{ordonnee}' x='{abscisse}' />")
            elif abscisse == 0 and indicey % 4 == 0:
                print(f"<rect fill='{WHITE}' stroke='{BLACK}' width='{square}' height='{square}' \
                    y='{ordonnee}' x='{abscisse}' />")
            elif abscisse == square * (len(x_list) - 1) and indicey % 4 != 0:
                print(f"<rect fill='{WHITE}' stroke='{BLACK}' width='{square}' height='{square}' \
                    y='{ordonnee}' x='{abscisse}' />")

    pied()

def main():
    """on genere un svg plateau.

    """
    if len(sys.argv) != 3 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("utilisation:", sys.argv[0], "largeur hauteur > plateau.svg")
        sys.exit(1)

    largeur = int(sys.argv[1])
    hauteur = int(sys.argv[2])

    plateau(largeur, hauteur)


if __name__ == "__main__":
    main()
