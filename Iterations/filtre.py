#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Nicolas Vincent

https://chamilo.grenoble-inp.fr/courses/ENSIMAG3MMBPI/document/tps/tpsse6.html#x9-80002.1
"""


class Point:

    """Représentation d'un Point

    Attributes:
        coordonnees (tuple): coordonnees du point

    """

    def __init__(self):
        """Constructeur de la classe Point initialisant un point en (0, 0)

        """

        self.coordonnees = (0, 0)

    def set_coords(self):
        """Modifie les coordonnées du point.

        """
        self.coordonnees = (input(), input())

    def draw_svg(self):
        """Affiche le point en svg

        """
        print(f"""<circle cx="{self.coordonnees[0]}" cy="{self.coordonnees[1]}" \
        r="5" stroke="black" stroke-width="3" fill="red" />""")


def main():
    """main function
    """

    print("<svg width='640' height='480'>")

    while True:
        try:
            point = Point()
            point.set_coords()
            point.draw_svg()
        except EOFError:
            break

    print("</svg>")

main()
