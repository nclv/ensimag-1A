# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Nicolas VINCENT
Projet pyhack (voir pyhack.pdf)

On stocke l'état d'une case dans un array numpy 2D
Il est ensuite affiché

Room représente une pièce sur la carte

"""


from random import randint
import subprocess
import platform
import time
import functools
import numpy as np


# TODO: réorganiser les classes avec SOLID


class Room:

    """Classe représentant une pièce

    Attributes:
         (type): description

    """

    def __init__(self, abscisse: int, ordonnee: int, width: int, height: int):
        """constructeur de la classe

        Parameters:
            abscisse, ordonnee, width, height (int): description

        Returns:
            (type): description

        """
        self.absc_top_right = abscisse
        self.ord_top_right = ordonnee
        self.absc_bottom_left = abscisse + width
        self.ord_bottom_left = ordonnee + height

    def intersect(self, room2: 'Room') -> bool:
        """Renvoie si deux pièces se chevauchent

        If the rectangles do not intersect, then at least one of the right sides will be
        to the left of the left side of the other rectangle (i.e. it will be a separating axis),
        or vice versa, or one of the top sides will be below the bottom side of the other
        rectange, or vice versa.

        Parameters:
            room2 (Room): deuxième pièce

        Returns:
            (bool): True si les pièces se chevauchent

        """
        return self.absc_top_right <= room2.absc_bottom_left and \
        self.absc_bottom_left >= room2.absc_top_right and \
        self.ord_top_right <= room2.ord_bottom_left and \
        room2.ord_bottom_left >= room2.ord_top_right

    def in_and_side(self, point: tuple) -> bool:
        """Vérifie que le point est dans la pièce (intérieur et côté)

        Parameters:
             point (tuple): point
             room (Room): pièce

        Returns:
            (boolean): True if the point is in the room

        """
        return self.absc_top_right <= point[0] <= self.absc_bottom_left and \
        self.ord_top_right <= point[1] <= self.ord_bottom_left

class Map:

    """Carte du jeu.

    Attributes:
         (type): description

    """

    # pylint: disable=too-many-instance-attributes

    def __init__(self, width: int, height: int):
        """Initialisation de la carte.

        Parameters:
             width (int): largeur de la Carte
             height (int): hauteur de la Carte

        """
        self.width = width
        self.height = height

        self.set_rooms_parameters()
        self.set_game_parameters()

    def set_rooms_parameters(self):
        """Paramètres par défauts des pièces de la carte

        """
        self.max_rooms = 100
        self.min_room_size = 3
        self.max_room_size = 8

    def set_game_parameters(self):
        """Paramètres par défauts du jeu

        """
        self.start = (0, 0)
        self.goal = ()

        self.localisation_player = (0, 0)

def place_room(carte: Map) -> list:
    """Génère les pièces sur la carte.



    Returns:
        rooms (list): liste contenant les pièces générée

    """
    rooms = []

    for _ in range(carte.max_rooms):
        width = randint(carte.min_room_size, carte.max_room_size - carte.min_room_size + 1)
        height = randint(carte.min_room_size, carte.max_room_size - carte.min_room_size + 1)
        abscisse = randint(0, carte.width - width - 1) + 1
        ordonnee = randint(0, carte.height - height - 1) + 1

        new_room = Room(abscisse, ordonnee, width, height)

        #on ajoute la pièce si elle n'en chevauche aucune autre
        failed = any(new_room.intersect(other_room) for other_room in rooms)

        if not failed:
            rooms.append(new_room)

    return rooms

def gen_board(carte: Map) -> np.ndarray:
    """Génère le plateau de jeu 2D.

    On représente une pièce par 1.

    Parameters:
        carte (Map): carte pour laquelle est généré le plateau de jeu

    Returns:
        board (np.ndarray): tableau 2D représentant le plateau

    """
    board = np.zeros(shape=(carte.width, carte.height))
    rooms = place_room(carte)

    for (absc, ordo), _ in np.ndenumerate(board):
        board[absc][ordo] = any(room.in_and_side((absc, ordo)) for room in rooms)

    return board

def draw_board(board: np.ndarray):
    """Affiche le dongeon

    Parameters:
        board (np.ndarray): tableau 2D représentant le plateau

    """
    for ordo in range(board.shape[1]):
        for absc in range(board.shape[0]):
            if board[absc][ordo]:
                print('#', end=" ")
            else:
                print('.', end=" ")
        print()

def clear():
    """Modifie l'affichage

    """
    subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)
    time.sleep(.01)

def while_true(func):
    """ Décore la fonction d'une boucle while True pour les inputs.

    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                res = func(*args, **kwargs)
                if res == 'verif':
                    continue
                break
            except ValueError:
                print("Rentrer une direction valide")
        return res
    return wrapper

@while_true
def get_direction():
    """Get direction input.

    """
    direction = input("Donner la direction (z, s, q, d): ")
    if direction not in ['z', 's', 'q', 'd']:
        raise ValueError()

    return direction

def main():
    """main function

    """
    carte = Map(60, 60)
    board = gen_board(carte)
    while carte.localisation_player != carte.goal:
        draw_board(board)
        direction = get_direction()
        board.move_player(direction)
        clear()
    print("You made it!")

if __name__ == '__main__':
    main()
