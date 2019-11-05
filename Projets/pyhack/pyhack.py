# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Nicolas VINCENT / Alan Dione
Projet pyhack (voir pyhack.pdf)

On stocke l'état d'une case dans un array numpy 2D

Room représente une pièce sur la carte

On place les pièces. On crée ensuite un labyrinthe entre les pièces.
Finalement, on relie le tout et on supprime les couloirs inutiles

"""


from random import randrange, choice
from operator import add
from itertools import product
from collections import namedtuple
import subprocess
import platform
import time
import sys
import logging
import functools

import log


# Vérification de la version de l'installation
try:
    assert sys.version_info >= (3, 6)
except AssertionError:
    raise SystemExit(
        "Ce jeu ne supporte pas Python {}.".format(platform.python_version()),
        "Installer une version supérieure à 3.6 pour le faire tourner.",
    )

try:
    import numpy as np
except ImportError:
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
    raise SystemExit()

# pylint: disable=logging-format-interpolation
# pylint: disable=logging-fstring-interpolation
MAIN_LOGGER = "main"
LOGGER = log.setup_custom_logger(MAIN_LOGGER)  # pylint: disable=no-member
LOGGER.info("Setting up main logger.")

# TODO:  déplacer ce qui est au dessus dans le fichier main.py

AVANCER = "z"
RECULER = "s"
GAUCHE = "q"
DROITE = "d"

EMPTY = 0
VISITED = 1
PLAYER = 2
ROOM = 3
CORRIDOR = 4
GOAL = 5
CONNECTOR = 6
ENTRANCE = 7

WALKABLE = [ROOM, CORRIDOR, ENTRANCE, GOAL]
DIRECTIONS = set([(1, 0), (0, 1), (-1, 0), (0, -1)])

AFFICHAGE_DEBUG = {
    EMPTY: "#",
    VISITED: "v",
    PLAYER: "@",
    ROOM: "r",
    CORRIDOR: "c",
    GOAL: "!",
    CONNECTOR: "f",
    ENTRANCE: "e",
}

AFFICHAGE = {
    EMPTY: "#",
    VISITED: ".",
    PLAYER: "@",
    ROOM: ".",
    CORRIDOR: ".",
    GOAL: "!",
    CONNECTOR: "#",
    ENTRANCE: ".",
}

# TODO: réorganiser les classes avec SOLID


def add_tuple(tuple1, tuple2):
    """Ajoute les éléments de deux tuples.

    Parameters:
        tuple1/tuple2 (tuple): //

    """
    return tuple(map(add, tuple1, tuple2))


class Room:
    """Classe représentant une pièce.

    Une pièce est représentée par deux points de la diagonale de la pièce.

    Attributes:
         absc (int): //
         ordo (int): //
         bottom_right (int): //
         top_left (int): //

    """

    def __init__(self, abscisse, ordonnee, width, height):
        """Constructeur de la classe Room.

        Parameters:
            abscisse, ordonnee, width, height (int): //

        """
        self.logger = logging.getLogger(MAIN_LOGGER + "." + Room.__name__)
        self.logger.debug("Création d'une instance de Room.")

        self.absc_bottom_left = abscisse
        self.ordo_bottom_left = ordonnee
        self.absc_bottom_right = abscisse + width
        self.ordo_top_left = ordonnee + height

        self.logger.debug(f"La pièce comporte {self.nombre_de_cases} cases.")

    def intersect(self, room2):
        """Renvoie si deux pièces se chevauchent ou sont à côté.

        If the rectangles do not intersect, then at least one of the right sides
        will be to the left of the left side of the other rectangle (i.e. it will
        be a separating axis), or vice versa, or one of the top sides will be
        below the bottom side of the other rectange, or vice versa.

        On agrandit le premier rectangle pour empêcher les pièces d'être côte à côte

        self.cases.isdisjoint(room2.cases) ne prend pas en compte les pièces
        côte à côte

        Parameters:
            room2 (Room): deuxième pièce

        Returns:
            (bool): True si les pièces se chevauchent

        """
        return (
            self.absc_bottom_left - 1 <= room2.absc_bottom_right
            and self.absc_bottom_right + 1 >= room2.absc_bottom_left
            and self.ordo_bottom_left - 1 <= room2.ordo_top_left
            and self.ordo_top_left + 1 >= room2.ordo_bottom_left
        )

    @property
    def cases(self):
        """Retourne les cases d'une pièce.

        Returns:
            (set): cases

        """
        return set(
            product(
                range(self.absc_bottom_left, self.absc_bottom_right + 1),
                range(self.ordo_bottom_left, self.ordo_top_left + 1),
            )
        )

    @property
    def nombre_de_cases(self):
        """Retourne le nombre de cases dans une pièces.

        Indépendant de self.get_cases

        Returns:
            (int): nombre de cases

        """
        return (self.absc_bottom_right - self.absc_bottom_left + 1) * (
            self.ordo_top_left - self.ordo_bottom_left + 1
        )

    # TODO: room.get_connecteurs ?
    # TODO: room.get_count_entrance ?


class Map:
    """Carte du jeu.

    Attributes:
         (type): description

    """

    # pylint: disable=too-many-instance-attributes

    MAX_ROOMS = 100
    MIN_ROOM_SIZE = 3
    MAX_ROOM_SIZE = 7

    def __init__(self, width, height):
        """Initialise la carte.

        Parameters:
             width (int): largeur de la Carte
             height (int): hauteur de la Carte

        """
        self.logger = logging.getLogger(MAIN_LOGGER + "." + Map.__name__)
        self.logger.info("Création d'une instance de Map.")

        self.width = width
        self.height = height

        # tableau
        self.board = np.zeros(shape=(self.width, self.height))
        # ensemble des possibilités de génération (on exclut la limite du plateau)
        self.cases = set(product(range(1, self.width - 1), range(1, self.height - 1)))

        self.set_regions_parameters()

        self.start = None
        self.goal = None

        # variables modifiables
        self.localisation_player = self.start
        self.discovered = set()

    def set_regions_parameters(self):
        """Paramètres par défauts des pièces de la carte."""
        self.logger.info("Attribution des paramètres des pièces.")

        # [room1, room2, ...] où room1 est le set des cases (tuple) de room1
        self.rooms_positions = []
        self.mazes_positions = []

        self.all_voisins = self.get_voisins()

        # va contenir des namedtuple(position, liste des régions voisines) non
        # hashable donc pas de set
        self.connecteurs = []
        # contient toutes les cases que l'on peut parcourir
        self.connected = set()

    def set_game_parameters(self):
        """Paramètres par défauts du jeu.

        Les positions de départ et d'arrivée ne doivent pas se trouver dans
        la même pièce.

        """
        self.logger.info("Attribution des paramètres du jeu.")
        flat_rooms_positions = [
            position
            for room_positions in self.rooms_positions[1:]
            for position in room_positions
        ]
        self.start = choice(list(self.rooms_positions[0]))
        self.goal = choice(flat_rooms_positions)
        self.logger.info(f"Start: {self.start}, Goal: {self.goal}")

        self.localisation_player = self.start

    def gen_board(self):
        """Génère le plateau de jeu 2D.

        On représente une pièce par 1, un joueur par 2, rien par 0

        Parameters:
            carte (Map): carte pour laquelle est généré le plateau de jeu

        Returns:
            self.board (np.ndarray): tableau 2D représentant le plateau

        """
        self.logger.info("Génération du plateau de jeu.")
        # get rooms
        rooms = self.get_rooms()
        # set rooms
        self.place_rooms(rooms)
        # create maze corridors
        self.fill_maze()

        # get_connecteurs
        self.set_connecteurs()
        self.connect_regions()
        self.remove_dead_ends()

        self.set_game_parameters()
        # set initial player position in a room
        self.set_tile(self.start, PLAYER)
        self.set_tile(self.goal, GOAL)

    def place_rooms(self, rooms):
        """Place les pièces générées sur la carte.

        Parameters:
            carte (Map): carte pour laquelle est généré le plateau de jeu
            self.board (np.ndarray): tableau 2D représentant le plateau

        Returns:
            self.board (np.ndarray): tableau 2D contenant les pièces générées

        """
        self.logger.info(f"Positionnement des pièces sur la carte")
        for room in rooms:
            for position in room.cases:
                self.board[position] = ROOM
            self.rooms_positions.append(room.cases)

    def get_rooms(self):
        """Génère les pièces sur la carte.

        # TODO: implémenter BSP pour une meilleur répartition

        Returns:
            rooms (list): liste contenant les pièces générées

        """
        self.logger.info("Génération des pièces.")
        rooms = []

        for _ in range(self.MAX_ROOMS):
            width = randrange(self.MIN_ROOM_SIZE, self.MAX_ROOM_SIZE)
            height = randrange(self.MIN_ROOM_SIZE, self.MAX_ROOM_SIZE)
            # on veut une délimitation autour des pièces
            abscisse = randrange(1, self.width - width - 1)
            ordonnee = randrange(1, self.height - height - 1)

            new_room = Room(abscisse, ordonnee, width, height)

            # on ajoute la pièce si elle n'en chevauche aucune autre
            failed = any(new_room.intersect(other_room) for other_room in rooms)

            if not failed:
                rooms.append(new_room)

        return rooms

    def get_voisins(self):
        """Renvoie les voisins de toutes les cases de la carte.

        """
        all_voisins = dict()
        for position in self.cases:
            voisins = self.check_on_board(positions_voisines(position))
            all_voisins[position] = voisins
        return all_voisins

    def fill_maze(self):
        """Rempli la carte avec un labyrinthe serpentant entre les pièces.

        Parameters:
            carte (Map): carte pour laquelle est généré le plateau de jeu
            self.board (np.ndarray): tableau 2D représentant le plateau

        Returns:
            self.board (np.ndarray): tableau 2D contenant le labyrinthe des couloirs

        """
        self.logger.info("Remplissage de la carte par des labyrinthes.")
        for position in self.cases:
            voisins = self.all_voisins[position]
            # autorisé si on peut construire un labyrinthe à partir de position
            allowed = self.check_empty_voisins(
                voisins
            ) and self.check_more_than_one_case(position)

            if allowed:
                self.gen_maze(position)

    def get_possibles_directions(self, position):
        """Renvoie une liste des directions possibles.

        Parameters:
            position (tuple): //

        Returns:
            (list): possibles directions

        """
        return [
            direction
            for direction in DIRECTIONS
            if self.couloir_possible(position, direction)
        ]

    def check_empty_voisins(self, voisins):
        """Vérifie que les positions du set voisins sont vides.

        Parameters:
            voisins (set): //

        Returns:
            (boolean)

        """
        return all(self.board[voisin] == EMPTY for voisin in voisins)

    def check_more_than_one_case(self, position):
        """Vérifie que le labyrinthe construit à partir de position contient plus d'une case.

        Parameters:
            position (tuple): //

        Returns:
            (boolean)

        """
        return bool(self.get_possibles_directions(position))

    def couloir_possible(self, position, direction):
        """Renvoie si l'on peut aller dans cette direction.

         - on ne doit pas toucher de pièce ou d'autre couloir

        Parameters:
            position (tuple): //
            direction (tuple): //

        Returns:
            (boolean)

        """
        next_case = add_tuple(position, direction)
        voisins = positions_voisines(next_case)
        voisins.remove(position)
        voisins.add(next_case)

        correct_voisins = self.check_on_board(voisins)
        if not correct_voisins:
            return False
        return self.check_empty_voisins(correct_voisins)

    def check_on_board(self, cases):
        """Renvoie les valeurs de table qui sont sur la carte.

        Parameters:
            cases (set): cases du plateau sur lesquelles on peut construire/
                        se déplacer

        Returns:
            (set): intersection de cases avec les cases du plateau

        """
        return cases.intersection(self.cases)

    def gen_maze(self, position):
        """Génère un labyrinthe à partir de la position fournie.

        On crè une liste des cases du labyrinthe ne contenant que position initialement.
        On construit le labyrinthe à partir de la dernière case de ce tableau.
        Lorsque l'on ne peut plus continuer, supprime le dernier élément et on itère.

        Parameters:
            position (tuple): //

        """
        self.logger.debug("Génération d'un labyrinthe.")
        maze_cases = [position]
        maze_positions = set()
        maze_positions.add(position)

        last_direction = None
        self.board[position] = CORRIDOR

        while maze_cases:
            case = maze_cases[-1]
            possible_direction = self.get_possibles_directions(case)
            if possible_direction:
                direction = get_direction(possible_direction, last_direction)
                new_case = add_tuple(case, direction)
                self.board[new_case] = CORRIDOR
                maze_cases.append(new_case)
                maze_positions.add(new_case)
                last_direction = direction
            else:
                del maze_cases[-1]
                last_direction = None

        self.mazes_positions.append(maze_positions)
        self.logger.debug(f"Labyrinthe de taille {len(maze_positions)} généré.")

    def set_connecteurs(self):
        """Trouve toutes les cases pouvant servir de connecteurs.

        Optionnels
        # TODO: on ne veut pas plus de max_entrance entrée pour chaque pièce,
        on choisit donc seulement max_entrances connecteurs par pièce
        # TODO: min_entrance de 2 ?

        Parameters:
            self.cases (set): cases du plateau autorisées

        Returns:
            self.connecteurs (list): liste des connecteurs possibles

        """
        self.logger.debug(f"Getting possible connectors.")
        Connecteur = namedtuple("Connecteur", "position regions_voisines")
        for position in self.cases:
            regions_voisines = self.check_connecteur(position)
            # si plus de deux régions touchent position
            if len(regions_voisines) > 1:
                connecteur = Connecteur(position, regions_voisines)
                self.connecteurs.append(connecteur)
                self.board[position] = CONNECTOR

    def check_connecteur(self, position):
        """Renvoie les régions autour de la case position.

        (si la case position peut servir de connecteur)
        La case doit être EMPTY et adjacente d'au moins deux cases
        appartenant à deux régions différentes.

        Parameters:
            position (tuple): //

        Returns:
            regions_differentes_voisines (list): régions voisines du connecteur

        """
        if position is EMPTY:
            return None
        # non rajouté en attribut car modifié par la suite
        regions = self.rooms_positions + self.mazes_positions
        voisins = self.all_voisins[position]
        regions_differentes_voisines = []
        for voisin in voisins:
            for region in regions:
                if voisin in region:
                    regions.remove(region)
                    regions_differentes_voisines.append(region)
                    break
        return regions_differentes_voisines

    def connect_regions(self):
        """Regroupement des différentes régions avec un connecteur.

        Parameters:
            self.rooms_positions, self.mazes_positions (list): régions du plateau

        Returns:
            self.connected (set): set des cases connectées

        """
        self.logger.info("Connection des régions.")
        regions = self.rooms_positions + self.mazes_positions

        while regions:
            connecteur = choice(self.connecteurs)
            self.board[connecteur.position] = ENTRANCE
            # décrémente les régions qui restent à traiter
            regions = [
                region
                for region in regions
                if region not in connecteur.regions_voisines
            ]
            # TODO: coder à part la suppression des connecteurs adjacents
            # TODO: remove tous les connecteurs du même mur de la pièce ?
            # remove connecteur et les autres connecteurs juste à côté de lui
            voisins = self.check_on_board(positions_voisines(connecteur.position))
            voisins.add(connecteur.position)
            self.connecteurs = [
                connecteur
                for connecteur in self.connecteurs
                if connecteur.position not in voisins
            ]
            # add connected regions to connected
            self.connected.add(connecteur.position)
            for region in connecteur.regions_voisines:
                self.connected.update(region)

        self.logger.debug("Régions connectées.")

    def remove_dead_ends(self):
        """Supprime les portions de labyrinthe inutiles.

        """
        self.logger.debug("Suppression des portions de couloir inutiles.")
        done = False
        while not done:
            done = True
            for position in self.cases:
                # on ne traite pas les murs
                if self.board[position] == EMPTY:
                    continue
                # s'il n'y a qu'une sortie, c'est une case inutile
                exits_count = 0
                voisins = self.all_voisins[position]
                for voisin in voisins:
                    if self.board[voisin] in WALKABLE:
                        exits_count += 1
                if exits_count != 1:
                    continue

                done = False
                self.board[position] = EMPTY

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

    def move_entity(self, entity, position, previous_position):
        """Déplace le joueur sur la position.

        Parameters:
            entity (string): entité à déplacer
            position (tuple): //
            previous_position (tuple): //

        """
        self.logger.debug(f"Déplacement de l'entité {entity} sur la case {position}")
        self.set_tile(position, entity)
        self.set_tile(previous_position, VISITED)

    def bad_movement(self, direction, movements):
        """Vérification de la possibilité du mouvement sur le plateau.

        Parameters:
            direction (str): //
            movements (dict): movements possibles

        Returns:
            (bool): True si le mouvement n'emmène pas sur une pièce ou un couloir

        """
        absc, ordo = movements[direction]
        return not self.board[absc][ordo] in WALKABLE + [VISITED]


class OutOfWalkError(Exception):
    """Raised when you try to move in a wall."""


def positions_voisines(position):
    """Retourne les positions voisines de position.
    (haut/bas/gauche/droite)

    Parameters:
        position (tuple): case dont on veut connaitre les voisins

    Returns:
        voisins (set): position et ses voisins

    """
    voisins = {add_tuple(position, direction) for direction in DIRECTIONS}
    return voisins


def get_direction(possible_direction, last_direction):
    """Renvoie la direction suivante du labyrinthe.

    Parameters:
        possible_direction (list): //
        last_direction (tuple): //

    Returns:
        direction (tuple): prochaine direction

    """
    # on privilégie les couloirs droits avec une certaine probabilité
    choose_last_direction = last_direction in possible_direction and (
        randrange(0, 100) > 70
    )
    return last_direction if choose_last_direction else choice(possible_direction)


def draw_board(board, affichage):
    """Affiche le dongeon sur le terminal.

    # TODO: sauvegarder plusieurs plateaux de debug

    Parameters:
        self.board (np.ndarray): tableau 2D représentant le plateau
        affichage (dict): dictionnaire contenant les caractères affichés

    """
    for ordo in range(board.shape[1]):
        for absc in range(board.shape[0]):
            tile = board[absc][ordo]
            print(affichage[tile], end=" ")
        print()


def clear():
    """Modifie l'affichage."""
    LOGGER.debug("Clear terminal")
    subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)
    time.sleep(0.1)


def while_true(func):
    """Décore la fonction d'une boucle while True pour les inputs.

    Erreurs personnalisées OutOfWalkError

    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                res = func(*args, **kwargs)
                if res == "verif":
                    continue
                break
            except ValueError:
                LOGGER.warning("Entrer une direction valide.")
            except OutOfWalkError:
                LOGGER.warning("Un mur vous empêche d'avancer.")
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
    LOGGER.debug("Getting direction.")
    direction = input(
        f"Donner la direction ({AVANCER}, {RECULER}, {GAUCHE}, {DROITE}): "
    )
    movements = get_movements(carte.localisation_player)
    LOGGER.debug("Checking direction.")
    if direction in ["quit", "exit"]:
        return direction, movements
    if direction not in [AVANCER, RECULER, GAUCHE, DROITE]:
        raise ValueError()
    LOGGER.debug("Checking if movement is allowed.")
    if carte.bad_movement(direction, movements):
        raise OutOfWalkError()

    return direction, movements


def get_movements(current_localisation):
    """Renvoie un dictionnaire des mouvements possibles.

    Parameters:
        current_localisation (tuple): //

    """
    absc, ordo = current_localisation
    return {
        AVANCER: (absc, ordo - 1),
        RECULER: (absc, ordo + 1),
        GAUCHE: (absc - 1, ordo),
        DROITE: (absc + 1, ordo),
    }


def main():
    """main function."""
    carte = Map(60, 60)
    carte.gen_board()
    while carte.localisation_player != carte.goal:
        draw_board(carte.board, AFFICHAGE)
        direction, movements = get_input_direction(carte)
        if direction in ["quit", "exit"]:
            break
        carte.move_entity(PLAYER, movements[direction], carte.localisation_player)
        carte.localisation_player = movements[direction]
        carte.discovered.add(carte.localisation_player)
        clear()
    print("\nYou made it!")


if __name__ == "__main__":
    #main()
    carte = Map(200, 200)
    carte.gen_board()
