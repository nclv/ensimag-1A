#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Nicolas Vincent
https://chamilo.grenoble-inp.fr/courses/ENSIMAG3MMBPI/document/tps/tpsse7.html
echiquier 8*8
"""

CASE_NUMBER = 8

BLACK = "#000000"
WHITE = "#ffffff"

WIDTH = 640
HEIGHT = 640

RECT_WIDTH = WIDTH//CASE_NUMBER
RECT_HEIGHT = HEIGHT//CASE_NUMBER

X_LIST = list(range(0, WIDTH, RECT_WIDTH))
Y_LIST = list(range(0, HEIGHT, RECT_HEIGHT))

def main():
    """main function

    """
    print(f"<svg width='{WIDTH}' height='{HEIGHT}'>")

    i = 1
    for ordonnee in Y_LIST:
        i += 1
        for abscisse in X_LIST:
            fill = (BLACK if i%2 == 0 else WHITE)
            print(f"<rect fill='{fill}' width='{RECT_WIDTH}' height='{RECT_HEIGHT}' \
             y='{ordonnee}' x='{abscisse}' />")
            i += 1

    print("</svg>")

main()
