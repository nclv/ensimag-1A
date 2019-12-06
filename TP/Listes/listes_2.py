# -*- coding: utf-8 -*-
#!/usr/bin/env python3


"""
listes triees, circulaires avec sentinelle.
"""


class Cellule:

    """Classe représentant un noeud

    Attributes:
         valeur ():
         suivante ():

    """

    __slots__ = "valeur", "suivante"

    #pylint: disable=too-few-public-methods
    def __init__(self, valeur, suivante=None):
        self.valeur = valeur
        self.suivante = suivante


class LinkedList:

    """Classe représentant une liste chaînée

    A linked list is a string of nodes, sort of like a string of pearls,
    with each node containing both data and a reference to the next node
    in the list (Note: This is a singly linked list. The nodes in a
    doubly linked list will contain references to both the next node
    and the previous node). The main advantage of using a linked list
    over a similar data structure, like the static array, is the linked
    list’s dynamic memory allocation: if you don’t know the amount of
    data you want to store before hand, the linked list can adjust on
    the fly.* Of course this advantage comes at a price: dynamic
    memory allocation requires more space and commands slower
    look up times.

    Attributes:
         head ():
         tail ():

    """

    def __init__(self, sentinelle, iterable=None):
        """Constructeur de la cellule

        Parameters:
            iterable (Iterable): //

        """
        self.head = Cellule(sentinelle)
        self.tail = None

        # on insère en tête
        if iterable:
            for valeur in sorted(iterable, reverse=True):
                self.insert_start(valeur)

    def insert_start(self, valeur):
        """Ajoût en tête"""
        self.head.suivante = Cellule(valeur, self.head.suivante)
        if self.tail is None:
            self.tail = self.head.suivante

    def insert_end(self, valeur):
        """Insertion d'une cellule en queue.

        Parameters:
            valeur ():

        """
        newtail = Cellule(valeur)
        if self.tail:
            self.tail.suivante = newtail
        else:
            self.head = newtail
        self.tail = newtail

    def insert(self, valeur):
        """Ajoût dans la liste triée"""
        assert valeur != self.head.valeur

        actualcellule = self.head.suivante
        while actualcellule.valeur < actualcellule.suivante.valeur:
            actualcellule = actualcellule.suivante

        actualcellule.suivante = Cellule(valeur, actualcellule.suivante)

    def remove(self, valeur):
        """Enlève la cellule contenant la valeur.

        Parameters:
            valeur ():

        """
        assert valeur != self.head.valeur

        if self.head is None:
            return

        currentcellule = self.head
        previouscellule = None

        while currentcellule.valeur != valeur:
            previouscellule = currentcellule
            currentcellule = currentcellule.suivante

        if previouscellule is None:
            self.head = currentcellule.suivante
        else:
            previouscellule.suivante = currentcellule.suivante

    def cells(self, inclure_sentinelle=False):
        """Yield les cellules de la liste chaînée

        """
        actualcellule = self.head if inclure_sentinelle else self.head.suivant

        while actualcellule is not None:
            yield actualcellule
            actualcellule = actualcellule.suivante

    def __str__(self):
        """
        affiche (val1, val2, val3....)
        """
        valeurs = [cellule.valeur for cellule in self.cells()]
        return f"{valeurs}"


def test():
    """
    tests simples des differentes methodes (a completer).
    """
    entiers = LinkedList(float("inf"), range(8))
    pairs, impairs = entiers.decoupe()
    print(pairs, impairs)
    print(entiers)
    pairs.supprimer(4)
    pairs.supprimer(0)
    pairs.supprimer(2)
    pairs.supprimer(6)
    impairs.ajouter(6)
    impairs.ajouter(0)

if __name__ == "__main__":
    test()
