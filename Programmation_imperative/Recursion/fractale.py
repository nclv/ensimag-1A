#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
VINCENT Nicolas

Arbre fractal svg.
"""


import math
import random


def drawTree(x1, y1, angle, depth, taille=8.0, stroke_width=16):
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * taille)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * taille)
        drawline(x1, y1, x2, y2, stroke_width=stroke_width)
        if random.random() < 0.8:
            drawTree(x2, y2, angle - 20, depth - 1, stroke_width=stroke_width / 1.5)
        drawTree(x2, y2, angle + 20, depth - 1, stroke_width=stroke_width / 1.4)


def set_up(height=500, width=500):
    """Initialize svg image."""
    print(f"<svg height='{height}' width='{width}'>")


def tear_down():
    """Close svg."""
    print("</svg>")


def drawline(x1, y1, x2, y2, color="rgb(192,192,192)", stroke_width=2):
    """Draw a svg line."""
    print(
        f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' style='stroke:{color};stroke-width:{stroke_width}' />"
    )


def main():
    """main function."""
    height, width = 1000, 1000
    set_up(height, width)
    drawTree(width // 2, height - 1, -90, 12)
    tear_down()


if __name__ == "__main__":
    main()
