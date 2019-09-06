#!/usr/bin/env python3

"""
Classe triangle
"""

from random import randint


class Point:
    """docstring for Point."""

    def __init__(self):
        self.coordonnees = [randint(0, 100), randint(0, 100)]

    def svg(self):
        """
        Affiche le point en svg
        """
        print(f"""<circle cx="{self.coordonnees[0]}" cy="{self.coordonnees[1]}" r="5" stroke="black" stroke-width="3" fill="red" />""")

def main():
    """ main function"""

    print('<svg height="100" width="100">')
    triangle = [Point(), Point(), Point()]
    triangle[0].svg()
    triangle[1].svg()
    triangle[2].svg()
    print('</svg>')

main()
