#!/usr/bin/env python3

"""
Somme deux entiers
"""

def entree():
    """
    Retourne un entier
    """
    return int(input("Entrer un entier: "))

def main():
    """
    main function
    """
    print(entree() + entree())

main()
