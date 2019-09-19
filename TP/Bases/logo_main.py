#!/usr/bin/env python3
"""
dessin : logo
"""

from logo import Logo


def main():
    """
    on cree un dessin a l’aide de l’objet logo.
    """
    tortue = Logo()
    tortue.leve_crayon()
    tortue.tourne_droite(180.0)
    tortue.avance(50.0)
    tortue.tourne_gauche(90.0)
    tortue.avance(50.0)
    tortue.tourne_gauche(90.0)
    tortue.baisse_crayon()

    tortue.avance(20.0)
    tortue.tourne_droite(90.0)
    tortue.avance(20.0)
    tortue.tourne_droite(90.0)
    tortue.avance(20.0)
    tortue.tourne_droite(90.0)
    tortue.avance(20.0)

    tortue.leve_crayon()
    tortue.avance(20.0)
    tortue.baisse_crayon()

    tortue.avance(20.0)
    tortue.tourne_droite(90.0)
    tortue.avance(20.0)
    tortue.tourne_droite(90.0)
    tortue.avance(20.0)
    tortue.tourne_droite(90.0)
    tortue.avance(20.0)

    tortue.leve_crayon()
    tortue.tourne_droite(90.0)
    tortue.avance(20.0)
    tortue.tourne_gauche(90.0)
    tortue.avance(10.0)
    tortue.baisse_crayon()

    tortue.tourne_gauche(45.0)
    tortue.avance(30.0)
    tortue.tourne_gauche(45.0)
    tortue.avance(30.0)
    tortue.tourne_gauche(45.0)
    tortue.avance(30.0)

main()
