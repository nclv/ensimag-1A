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
GOAL = 5

DIRECTIONS = set([(1, 0), (0, 1), (-1, 0), (0, -1)])


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

    def contain(self, point: tuple) -> bool:
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

        #tableau
        self.board = np.zeros(shape=(self.width, self.height))
        #ensemble des possibilités de génération (on exclut la limite du plateau)
        self.cases = set(product(range(1, self.width - 1), range(1, self.height - 1)))

        self.set_rooms_parameters()

        self.start = None
        self.goal = None

        #variables modifiables
        self.localisation_player = self.start
        self.discovered = set()

    def set_rooms_parameters(self):
        """Paramètres par défauts des pièces de la carte

        """
        self.max_rooms = 100
        self.min_room_size = 3
        self.max_room_size = 7

        self.room_positions = []

    # TODO: set_corridors_parameters

    def set_game_parameters(self):
        """Paramètres par défauts du jeu

        """
        self.start = choice(self.room_positions)
        self.goal = choice(self.room_positions)

        self.localisation_player = self.start

    def gen_board(self) -> np.ndarray:
        """Génère le plateau de jeu 2D.

        On représente une pièce par 1, un joueur par 2, rien par 0

        Parameters:
            carte (Map): carte pour laquelle est généré le plateau de jeu

        Returns:
            self.board (np.ndarray): tableau 2D représentant le plateau

        """
        #set rooms
        self.place_rooms()
        #create maze corridors
        self.fill_maze()

        self.set_game_parameters()
        #set initial player position in a room
        self.set_tile(self.start, PLAYER)
        self.set_tile(self.goal, GOAL)

    def place_rooms(self) -> np.ndarray:
        """Place les pièces générées sur la carte

        Parameters:
            carte (Map): carte pour laquelle est généré le plateau de jeu
            self.board (np.ndarray): tableau 2D représentant le plateau

        Returns:
            self.board (np.ndarray): tableau 2D contenant les pièces générées

        """
        rooms = self.get_rooms()
        #placement des pièces
        for position, _ in np.ndenumerate(self.board):
            for room in rooms:
                if room.contain(position):
                    self.board[position] = ROOM
                    self.room_positions.append(position)
                    break

    def get_rooms(self) -> list:
        """Génère les pièces sur la carte.

        # TODO: implémenter BSP pour une meilleur répartition

        Returns:
            rooms (list): liste contenant les pièces générées

        """
        rooms = []

        for _ in range(self.max_rooms):
            width = randrange(self.min_room_size, self.max_room_size)
            height = randrange(self.min_room_size, self.max_room_size)
            #on veut une délimitation autour des pièces
            abscisse = randrange(1, self.width - width - 1)
            ordonnee = randrange(1, self.height - height - 1)

            new_room = Room(abscisse, ordonnee, width, height)

            #on ajoute la pièce si elle n'en chevauche aucune autre
            failed = any(new_room.intersect(other_room) for other_room in rooms)

            if not failed:
                rooms.append(new_room)

        return rooms

    def fill_maze(self):
        """Rempli la carte avec un labyrinthe serpentant entre les pièces

        Parameters:
            carte (Map): carte pour laquelle est généré le plateau de jeu
            self.board (np.ndarray): tableau 2D représentant le plateau

        Returns:
            self.board (np.ndarray): tableau 2D contenant le labyrinthe des couloirs

        """
        for ordo in range(1, self.width - 1):
            for absc in range(1, self.height - 1):
                position = absc, ordo
                voisins = self.check_on_board(positions_voisines(position))
                allowed = all(not self.board[voisin] for voisin in voisins)
                if allowed:
                    self.gen_maze(position)

    def couloir_possible(self, position, direction):
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

        correct_voisins = self.check_on_board(voisins)
        if not correct_voisins:
            return False
        return all(not self.board[case] for case in correct_voisins)

    def check_on_board(self, cases):
        """Renvoie les valeurs de table qui sont sur la carte.

        Parameters:
            carte (Map): carte pour laquelle est généré le plateau de jeu
            cases (set): cases du plateau sur lesquelles on peut construire/se déplacer

        """
        return cases.intersection(self.cases)

    def gen_maze(self, position):
        """Génère un labyrinthe à partir de la position fournie

        """
        maze_cases = [position]
        last_direction = None

        self.board[position] = CORRIDOR

        while maze_cases:
            case = maze_cases[-1]

            possible_direction = [direction for direction in DIRECTIONS \
            if self.couloir_possible(case, direction)]

            if possible_direction:
                direction = get_direction(possible_direction, last_direction)
                new_case = add_tuple(case, direction)
                self.board[new_case] = CORRIDOR
                maze_cases.append(new_case)
                last_direction = direction
            else:
                #aucune case adjacente libre
                del maze_cases[-1]
                last_direction = None

    def set_tile(self, position, tile_type):
        """Assigne tile_type sur la position du plateau.

        Parameters:
            position (tuple): position du plateau
            self.board (np.ndarray): tableau 2D représentant le plateau
            tile_type (int): type de case

        Returns:
            self.board (np.ndarray): tableau 2D avec tile_type sur position

        """
        absc, ordo = position
        self.board[absc][ordo] = tile_type

    def move_player(self, position, previous_position):
        """Déplace le joueur sur la position

        """
        self.set_tile(position, PLAYER)
        self.set_tile(previous_position, WALKABLE)

    def bad_movement(self, direction, movements):
        """Vérification de la possibilité du mouvement sur le plateau.

        Returns:
            (bool): True si le mouvement n'emmène pas sur une pièce ou un couloir

        """
        absc, ordo = movements[direction]
        return not self.board[absc][ordo] in [ROOM, CORRIDOR, WALKABLE]



class OutOfWalkError(Exception):
    """Raised when you try to move in a wall"""

###

def positions_voisines(position):
    """Retourne position et les positions voisines de position (haut/bas/gauche/droite)

    Parameters:
        position (tuple): case dont on veut connaitre les voisins

    Returns:
        voisins (set): position et ses voisins

    """
    voisins = {add_tuple(position, direction) for direction in DIRECTIONS}
    voisins.add(position)
    return voisins

def get_direction(possible_direction, last_direction):
    """Renvoie la direction suivante du labyrinthe.

    Parameters:
        possible_direction (list): //
        last_direction (tuple): //

    Returns:
        direction (tuple): prochaine direction

    """
    #on privilégie les couloirs droits avec une certaine probabilité
    choose_last_direction = last_direction in possible_direction and (randrange(0, 100) > 70)
    return last_direction if choose_last_direction else choice(possible_direction)


###

def connect_rooms():
    """Trouve toutes les cases pouvant servir de connecteurs

    Parameters:

    """



###



def draw_board(board: np.ndarray):
    """Affiche le dongeon

    Parameters:
        self.board (np.ndarray): tableau 2D représentant le plateau

    """
    # TODO: timeit
    #for position, _ in np.ndenumerate(self.board):
    for ordo in range(board.shape[1]):
        for absc in range(board.shape[0]):
            tile = board[absc][ordo]
            if tile == EMPTY:
                print('#', end=" ")
            elif tile == WALKABLE:
                print('.', end=" ")
            elif tile == PLAYER:
                print('@', end=" ")
            elif tile == ROOM:
                print('.', end=" ")
            elif tile == CORRIDOR:
                print('c', end=" ")
            elif tile == GOAL:
                print('!', end=" ")
        print()

def clear():
    """Modifie l'affichage

    """
    subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)
    time.sleep(.01)

def while_true(func):
    """ Décore la fonction d'une boucle while True pour les inputs.

    Erreurs personnalisées OutOfWalkError

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
def get_input_direction(carte):
    """Prend en entrée la direction.

    Parameters:
        carte (Map): carte pour laquelle est généré le plateau de jeu
        self.board (np.ndarray): tableau 2D représentant le plateau

    Returns:
        direction (str): //
        movements (dict): coordonnées des mouvements possibles

    """
    direction = input("Donner la direction (z, s, q, d): ")
    movements = get_movements(carte.localisation_player)
    if direction not in ['z', 's', 'q', 'd']:
        raise ValueError()
    if carte.bad_movement(direction, movements):
        raise OutOfWalkError()

    return direction, movements

def get_movements(current_localisation):
    """Renvoie un dictionnaire des mouvements possibles

    """
    absc, ordo = current_localisation
    return {AVANCER: (absc, ordo - 1), RECULER: (absc, ordo + 1), \
    GAUCHE: (absc - 1, ordo), DROITE: (absc + 1, ordo)}


def main():
    """main function

    """
    carte = Map(60, 60)
    carte.gen_board()
    while carte.localisation_player != carte.goal:
        draw_board(carte.board)
        direction, movements = get_input_direction(carte)
        carte.move_player(movements[direction], carte.localisation_player)
        carte.localisation_player = movements[direction]
        clear()
    print("You made it!")

if __name__ == '__main__':
    main()
