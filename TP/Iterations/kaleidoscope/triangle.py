# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Classe triangle
"""


from math import sin, cos
from point import Point, random_point


class Triangle_aleatoire:
    """Oneline description.

    Attributes:
        points (list): 3 points du triangle

    Returns:
        triangle (): triangle aléatoire

    """
    def __init__(self, delimitation_x, delimitation_y):
        """Constructeur

        Parameters:
             delimitation_x/ delimitation_y (tuple): largeur/hauteur du cadrant dans lequel se
             trouve le triangle

        """
        self.points = [random_point(delimitation_x, delimitation_y), random_point(delimitation_x, delimitation_y), random_point(delimitation_x, delimitation_y)]


    def rotation_autour(self, centre, angle):
        """Rotation du triangle.

        Parameters:
            centre (type): centre de rotation
            angle (float): angle de la rotation

        """

        rot_x = lambda x, y: (x - centre.absc) * cos(angle) - (y - centre.ord) * sin(angle) + centre.absc
        rot_y = lambda x, y: (x - centre.absc) * sin(angle) + (y - centre.ord) * cos(angle) + centre.ord

        for indice, point in enumerate(self.points):
            new_point = Point((rot_x(point.absc, point.ord), rot_y(point.absc, point.ord)))
            self.points[indice] = new_point

        return self
