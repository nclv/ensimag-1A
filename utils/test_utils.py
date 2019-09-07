#!/usr/bin/env python3


"""
Module de test de la librairie utils
"""

from utils import Svg


def main():
    """main function

    """
    draw_all_shapes()


def draw_all_shapes():
    """Test du module SVG et sauvegarde du fichier final.

    """
    image = Svg()

    image.create(300, 300)

    image.fill("#A0A0FF")
    image.circle("#000080", 4, "#0000FF", 32, 64, 96)
    image.line("#000000", 2, 8, 8, 248, 184)
    image.rectangle(64, 64, 112, 32, "#00FF00", "#008000", 4, 4, 4)
    image.text(32, 16, "sans-serif", 16, "#000000", "#000000", "test")
    image.ellipse(64, 160, 32, 16, "#FF0000", "#800000", 4)

    image.end()

    try:
        image.save("allshapes.svg")
    except IOError as ioe:
        print(ioe)

    print(image)

main()
