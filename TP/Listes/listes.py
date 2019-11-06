#!/usr/bin/env python3
"""
listes simplements chainees + quelques operations
"""
#from tycat import trace

class Cellule:

    """Classe représentant un noeud

    Attributes:
         valeur ():
         nextcellule ():

    """

    def __init__(self, valeur, suivante=None):
        """Constructeur de la cellule

        """
        self.valeur = valeur
        self.nextcellule = suivante


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

    def __init__(self):
        """Constructeur de la cellule

        Parameters:
            iterable (Iterable): //

        """
        self.head = None
        self.tail = None
        self.taille = 0

    # O(1) !!!
    def insertStart(self, valeur):
        """Insertion d'une cellule en tête.

        Parameters:
            valeur ():

        """
        self.head = Cellule(valeur, self.head)

        if self.tail is None:
            self.tail = self.head

    # O(1)
    def insertEnd(self, valeur):
        """Insertion d'une cellule en queue.

        Parameters:
            valeur ():

        """
        newtail = Cellule(valeur, None)
        if self.tail:
            self.tail.nextcellule = newtail
        else:
            self.head = newtail
        self.tail = newtail

    def remove(self, valeur):
        """Enlève la cellule contenant la valeur.

        Parameters:
            valeur ():

        """

        if self.head is None:
            return

        currentcellule = self.head
        previouscellule = None

        while currentcellule.valeur != valeur:
            previouscellule = currentcellule
            currentcellule = currentcellule.nextcellule

        if previouscellule is None:
            self.head = currentcellule.nextcellule
        else:
            previouscellule.nextcellule = currentcellule.nextcellule

    def cells(self):
        """Yield les cellules de la liste chaînée

        """
        actualcellule = self.head

        while actualcellule is not None:
            yield actualcellule
            actualcellule = actualcellule.nextcellule

    def recherche(self, valeur):
        """Recherche une valeur dans la liste chaînée

        """
        for cellule in self.cells():
            if cellule.valeur == valeur:
                return cellule
        return None

    def __str__(self):
        """
        affiche (val1, val2, val3....)
        """
        valeurs = [cellule.valeur for cellule in self.cells()]
        return f"{valeurs}"


def test_listes():
    """
    on teste toutes les operations de base, dans differentes configurations.
    """
    exemple = LinkedList()
    exemple.insertStart(3)
    exemple.insertStart(5)
    exemple.insertEnd(2)
    exemple.insertEnd(4)
    print("exemple : ", exemple)
    print("recherche : ", exemple.recherche(3).valeur)
    print("adresses des cellules : ",
          ",".join([hex(id(c))for c in exemple.cells()]))
    exemple.remove(5)
    print("apres suppression de 5 : ", exemple)
    exemple.remove(4)
    print("apres suppression de 4 : ", exemple)

if __name__ == "__main__":
    test_listes()
