# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Nicolas VINCENT / Alan Dione
Projet pyhack (voir pyhack.pdf)

On stocke l'état d'une case dans un array numpy 2D

Room représente une pièce sur la carte

On place les pièces. On crè ensuite un labyrinthe entre les pièces.
Finalement, on relie le tout et on supprime les couloirs inutiles

"""


from random import randrange, choice
from operator import add
from itertools import product
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
ROOM = 3
CORRIDOR = 4


# TODO: réorganiser les classes avec SOLID

def add_tuple(tuple1, tuple2):
    """Ajoute les éléments de deux tuples

    """
    return tuple(map(add, tuple1, tuple2))

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
        """Constructeur d'un couloir entre deux pièces.

        Parameters:
             room1/rooms2 (Room): pièces d'entrée/sortie du couloir

        """
        self.entree = room1
        self.sortie = room2


class Room(Structure):

    """Classe représentant une pièce

    Une pièce est représentée par deux points de la diagonale de la pièce.

    Attributes:
         absc (int): //
         ordo (int): //
         bottom_right (int): //
         top_left (int): //

    """

    def __init__(self, abscisse: int, ordonnee: int, width: int, height: int):
        """constructeur de la classe Room

        Parameters:
            abscisse, ordonnee, width, height (int): description

        """
        self.absc_bottom_left = abscisse
        self.ordo_bottom_left = ordonnee
        self.absc_bottom_right = abscisse + width
        self.ordo_top_left = ordonnee + height

    def intersect(self, room2: 'Room') -> bool:
        """Renvoie si deux pièces se chevauchent ou sont à côté

        If the rectangles do not intersect, then at least one of the right sides will be
        to the left of the left side of the other rectangle (i.e. it will be a separating axis),
        or vice versa, or one of the top sides will be below the bottom side of the other
        rectange, or vice versa.

        On agrandit le premier rectangle pour empêcher les pièces d'être côte-à-côte

        Parameters:
            room2 (Room): deuxième pièce

        Returns:
            (bool): True si les pièces se chevauchent

        """
        return self.absc_bottom_left - 1 <= room2.absc_bottom_right and \
        self.absc_bottom_right + 1 >= room2.absc_bottom_left and \
        self.ordo_bottom_left - 1 <= room2.ordo_top_left and \
        self.ordo_top_left + 1 >= room2.ordo_bottom_left

    def in_and_side(self, point: tuple) -> bool:
        """Vérifie que le point est dans la pièce (intérieur et côté)

        Parameters:
             point (tuple): point

        Returns:
            (boolean): True if the point is in the room

        """
        return self.absc_bottom_left <= point[0] <= self.absc_bottom_right and \
        self.ordo_bottom_left <= point[1] <= self.ordo_top_left


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

        #set des possibilités
        self.cases = set(product(range(self.width), range(self.height)))

        self.set_rooms_parameters()
        self.set_game_parameters()

    def set_rooms_parameters(self):
        """Paramètres par défauts des pièces de la carte

        """
        self.max_rooms = 100
        self.min_room_size = 3
        self.max_room_size = 7

    # TODO: set_corridors_parameters

    def set_game_parameters(self):
        """Paramètres par défauts du jeu

        """
        self.start = (0, 0)
        self.goal = ()

        #variables modifiables
        self.localisation_player = (0, 0)
        self.discovered = set()


class OutOfWalkError(Exception):
    """Raised when you try to move in a wall"""

###

def positions_voisines(position):
    """Retourne les positions voisines de position (haut/bas/gauche/droite)
    avec position

    """

    directions = set([(1, 0), (0, 1), (-1, 0), (0, -1)])
    voisins = {add_tuple(position, direction) for direction in directions}
    voisins.add(position)
    return voisins

def check_on_board(carte, cases):
    """Renvoie les valeurs de table qui sont sur la carte.

    Parameters:
        cases (set): set des cases

    """
    return cases.intersection(carte.cases)

def fill_maze(carte, board):
    """Rempli la carte avec un labyrinthe serpentant entre les pièces

    """
    for ordo in range(1, carte.width - 1):
        for absc in range(1, carte.height - 1):
            position = absc, ordo
            voisins = check_on_board(carte, positions_voisines(position))
            allowed = all(not board[voisin] for voisin in voisins)
            if allowed:
                board = gen_maze(carte, board, position)

    return board

def couloir_possible(carte, board, position, direction):
    """Renvoie si l'on peut aller dans cette direction

     - on ne doit pas toucher de pièce ou d'autre couloir

    Parameters:
        ()

    Returns:
        (boolean):

    """
    next_case = add_tuple(position, direction)
    voisins = positions_voisines(next_case)
    voisins.remove(position)
    voisins.add(next_case)

    correct_voisins = check_on_board(carte, voisins)
    if not correct_voisins:
        return False
    return all(not board[case] for case in correct_voisins)


def gen_maze(carte, board, position):
    """Génère un labyrinthe à partir de la position fournie

    """
    maze_cases = [position]
    last_direction = None

    board[position] = CORRIDOR

    while maze_cases:
        case = maze_cases[-1]

        #print(case)
        #draw_board(board)
        #time.sleep(0.4)

        possible_direction = []
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for direction in directions:
            if couloir_possible(carte, board, case, direction):
                possible_direction.append(direction)

        if possible_direction:
            direction = None
            #on privilégie les couloirs droits avec une certaine probabilité
            if last_direction in possible_direction and (randrange(0, 100) > 70):
                direction = last_direction
            else:
                direction = choice(possible_direction)

            new_case = add_tuple(case, direction)
            board[new_case] = CORRIDOR
            maze_cases.append(new_case)
            last_direction = direction
        else:
            #aucune case adjacente libre
            del maze_cases[-1]
            last_direction = None

    return board

###



###

def place_rooms(carte: Map) -> list:
    """Génère les pièces sur la carte.

    # TODO: implémenter BSP pour une meilleur répartition

    Returns:
        rooms (list): liste contenant les pièces générée

    """
    rooms = []

    for _ in range(carte.max_rooms):
        width = randrange(carte.min_room_size, carte.max_room_size)
        height = randrange(carte.min_room_size, carte.max_room_size)
        abscisse = randrange(0, carte.width - width)
        ordonnee = randrange(0, carte.height - height)

        new_room = Room(abscisse, ordonnee, width, height)

        #on ajoute la pièce si elle n'en chevauche aucune autre
        failed = any(new_room.intersect(other_room) for other_room in rooms)

        if not failed:
            rooms.append(new_room)

    return rooms

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

    #placement des pièces/corridors (mise à 1)
    for (absc, ordo), _ in np.ndenumerate(board):
        board[absc][ordo] = any(room.in_and_side((absc, ordo)) for room in rooms)

    #set initial player position
    board = set_player_localisation(carte.start, board)
    board = fill_maze(carte, board)

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
                print('.', end=" ")
            elif tile == PLAYER:
                print('@', end=" ")
            elif tile == EMPTY:
                print('#', end=" ")
            elif tile == CORRIDOR:
                print('c', end=" ")
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
                print("Entrer une direction valide.")
            except OutOfWalkError:
                print("Un mur vous empêche d'avancer.")
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

def set_player_localisation(new_localisation, board):
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
        board = set_player_localisation(movements[direction], board)
        clear()
    print("You made it!")

if __name__ == '__main__':
    main()
