# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Nicolas VINCENT
https://chamilo.grenoble-inp.fr/courses/ENSIMAG3MMBPI/document/tps/tpsse12.html
"""

import sys
import functools
import itertools
import numpy as np

def get_numbers():
    """Renvoie le contenu du niveau

    """
    with open(sys.argv[1], 'r') as file:
        return iter(file.read().split())

def gen_board():
    """Génère le plateau

    """
    board = np.zeros(shape=(5, 5))
    for absc, line in enumerate(get_numbers()):
        for ordo, value in enumerate(line):
            if value == ".":
                board[absc][ordo] = 1
    return board

def get_voisins(case):
    """Retourne les voisins

    """
    absc, ordo = case
    return [(absc + 1, ordo), (absc - 1, ordo), (absc, ordo - 1), (absc, ordo + 1)]

def filter_voisins(voisins):
    """Filtre les voisins

    """
    indice_lst = []
    for indice, coord in enumerate(voisins):
        for value in coord:
            if value < 0:
                indice_lst.append(indice)
    #filter by index

def play(board, case):
    """Routine de jeu

    """
    print(case)
    voisins = get_voisins(case)
    print(voisins)


def draw(board):
    """Dessine la plateau

    """

    letters = iter("ABCDE")

    print("    ", *range(1, 6), " ")
    print("  +", "-"*11, "+")

    for absc in range(board.shape[1]):
        print(next(letters), "|  ", end="")
        for ordo in range(board.shape[0]):
            tile = board[absc][ordo]
            if tile:
                print("b ", end="")
            else:
                print("r ", end="")
        print(" |")

    print("  +", "-"*11, "+")

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
                print("Entrer une case valide")
        return res
    return wrapper

@while_true
def get_input():
    """Get direction input.

    """
    case = input("Choisisser une case à jouer: \n")
    possibilities = list(map("".join, itertools.product("ABCDE", "12345")))
    if case not in possibilities:
        raise ValueError()
    indice = possibilities.index(case)
    return indice // 5, indice % 5

def main():
    """main function

    """
    case = get_input()
    board = gen_board()
    play(board, case)
    draw(board)

main()
