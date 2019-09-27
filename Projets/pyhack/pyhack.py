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


AVANCER = "z"
RECULER = "s"
GAUCHE = "q"
DROITE = "d"

EMPTY = 0
WALKABLE = 1
PLAYER = 2


# TODO: réorganiser les classes avec SOLID


class Structure:

    """Classe représentant une structure sur la carte

    """

    def intersect(self, other_struct: 'Structure'):
        """Renvoie si deux structurent s'intersectent

        Parameters:
            other_struct (Structure): deuxième structure

        Returns:
            (bool): True si les pièces se chevauchent

        """
        raise NotImplementedError




class Corridor(Structure):

    """Classe représentant un couloir entre deux pièces

    Attributes:
         entree/sortie (Room): entrée/sortie du couloir

    """

    def __init__(self, room1: 'Room', room2: 'Room'):
        """oneline description.

        Parameters:
             room1/rooms2 (Room): pièces d'entrée/sortie du couloir

        """
        self.entree = room1
        self.sortie = room2


class Room(Structure):

    """Classe représentant une pièce

    Une pièce est représentée par deux points de la diagonale de la pièce.

    Attributes:
         absc_top_right (int): //
         ord_top_right (int): //
         absc_bottom_left (int): //
         ord_bottom_left (int): //

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

    # TODO: set_corridors_parameters

    def set_game_parameters(self):
        """Paramètres par défauts du jeu

        """
        self.start = (0, 0)
        self.goal = ()

        self.localisation_player = (0, 0)


class OutOfWalkError(Exception):
    """Raised when you try to move in a wall"""


def place_rooms(carte: Map) -> list:
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

def place_corridors(carte: Map) -> list:
    """Génère les corridors sur la carte.

    Choix d'une entrée/sortie aléatoire dans chacune des deux pièces

    Returns:
        corridors (list): liste contenant les pièces générée

    """
    corridors = []

    # TODO:

    return corridors

def gen_board(carte: Map) -> np.ndarray:
    """Génère le plateau de jeu 2D.

    On représente une pièce par 1, un joueur par 2, rien par 0

    Parameters:
        carte (Map): carte pour laquelle est généré le plateau de jeu

    Returns:
        board (np.ndarray): tableau 2D représentant le plateau

    """
    board = np.zeros(shape=(carte.width, carte.height))
    rooms = place_rooms(carte)
    #corridors = place_corridors(carte)

    #placement des pièces/corridors
    for (absc, ordo), _ in np.ndenumerate(board):
        board[absc][ordo] = any(room.in_and_side((absc, ordo)) for room in rooms)

    #placement du joueur
    absc, ordo = carte.localisation_player
    board[absc][ordo] = PLAYER

    return board

def draw_board(board: np.ndarray):
    """Affiche le dongeon

    Parameters:
        board (np.ndarray): tableau 2D représentant le plateau

    """
    for ordo in range(board.shape[1]):
        for absc in range(board.shape[0]):
            tile = board[absc][ordo]
            if tile == WALKABLE:
                print('#', end=" ")
            elif tile == PLAYER:
                print('@', end=" ")
            elif tile == EMPTY:
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
                print("Entrer une direction valide")
            except OutOfWalkError:
                print("Un mur vous empêche d'avancer")
        return res
    return wrapper

@while_true
def get_input_direction(carte, board):
    """Get direction input.

    """
    direction = input("Donner la direction (z, s, q, d): ")
    movements = get_movements(carte.localisation_player)
    if direction not in ['z', 's', 'q', 'd']:
        raise ValueError()
    if bad_movement(direction, movements, board):
        raise OutOfWalkError()

    return direction, movements

def get_movements(current_localisation):
    """Renvoie un dictionnaire des mouvements possibles

    """
    absc, ordo = current_localisation
    return {AVANCER: (absc, ordo + 1), RECULER: (absc, ordo - 1), \
    GAUCHE: (absc - 1, ordo), DROITE: (absc + 1, ordo)}

def bad_movement(direction, movements, board):
    """Vérification de la possibilité du mouvement sur le plateau

    Returns:
        (bool): True si la pièce du plateau est à 1 (pièce/couloir)

    """
    absc, ordo = movements[direction]
    return not board[absc][ordo]

def set_new_localisation(new_localisation, board):
    """Déplace le joueur dans la direction donnée

    Parameters:
        direction (str): //
        movements (dict): coordonnées des mouvements possibles

    Returns:
        (tuple): nouvelles coordonnées du joueur

    """
    absc, ordo = new_localisation
    board[absc][ordo] = PLAYER
    return board


def main():
    """main function

    """
    carte = Map(60, 60)
    board = gen_board(carte)
    while carte.localisation_player != carte.goal:
        draw_board(board)
        direction, movements = get_input_direction(carte, board)
        board = set_new_localisation(movements[direction], board)
        clear()
    print("You made it!")

if __name__ == '__main__':
    main()
