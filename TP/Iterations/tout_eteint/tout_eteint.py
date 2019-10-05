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
    cases = set(itertools.product(range(0, 5), range(0, 5)))
    for absc, line in enumerate(get_numbers()):
        for ordo, value in enumerate(line):
            if value == ".":
                board[absc][ordo] = 1
    return board, cases

def get_voisins(case):
    """Retourne les voisins

    """
    absc, ordo = case
    return [(absc + 1, ordo), (absc - 1, ordo), (absc, ordo - 1), (absc, ordo + 1)]

def play(board, cases_auth, case):
    """Routine de jeu

    """
    voisins = set(get_voisins(case)).intersection(cases_auth)
    board[case] = 0
    for voisin in voisins:
        board[voisin] = 0
    return board

def end_game(board):
    return all(not tile for _, tile in np.ndenumerate(board))

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
    case = input("Choisisser une case à jouer: [A-E][1-5]\n")
    possibilities = list(map("".join, itertools.product("ABCDE", "12345")))
    if case not in possibilities:
        raise ValueError()
    indice = possibilities.index(case)
    return indice // 5, indice % 5

def main():
    """main function

    """
    board, cases_auth = gen_board()
    while not end_game(board):
        draw(board)
        case = get_input()
        board = play(board, cases_auth, case)

main()
