# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Nicolas VINCENT

linked_list avec iterable
"""


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

    def __init__(self, iterable=None):
        """Constructeur de la cellule

        Parameters:
            iterable (Iterable): //

        """
        self.create(iterable=iterable)

    def create(self, iterable=None):
        """Création d'une liste chaînée."""
        self.head = None
        self.tail = None
        if iterable:
            for element in iterable:
                self.insertEnd(element)

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

    def transformation(self, fonction):
        """Remplace valeur par fonction(valeur) pour chaque élément de la liste.

        Parameters:
            fonction (function): //

        """
        for cellule_courante in self.cells():
            cellule_courante.valeur = fonction(cellule_courante.valeur)

    def iterateur_filtre(self, fonction):
        """Itérateur qui renvoie tout élément dont fonction(valeur) est vrai.

        Parameters:
            fonction (function): fonction qui retourne un booléen

        """

        for cellule_courante in self.cells():
            if fonction(cellule_courante.valeur):
                yield cellule_courante

    def filtre(self, fonction):
        """Renvoie tout élément dont fonction(valeur) est vrai.

        Parameters:
            fonction (function): fonction qui retourne un booléen

        """
        # self.create(iterable=self.iterateur_filtre(fonction))
        cellules_gardees = self.iterateur_filtre(fonction)
        try:
            self.head = next(cellules_gardees)
        except StopIteration:
            self.head, self.tail = None, None

        self.tail = self.head
        for cellule_gardee in cellules_gardees:
            self.tail.nextcellule = cellule_gardee
            self.tail = cellule_gardee

        self.tail.nextcellule = None

    def concatenation(self, liste_fin):
        """Concatène la liste_fin à la liste chaînée.

        Parameters:
            liste_fin (LinkedList): //

        """
        if self.tail:
            self.tail.nextcellule = liste_fin.head
        else:
            self.head = liste_fin.head

        if liste_fin.tail:
            self.tail = liste_fin.tail

        liste_fin.head, liste_fin.tail = None, None

    def reverse(self):
        """Function to reverse the linked list."""
        prev = None
        current = self.head
        while (current is not None):
            next = current.nextcellule
            current.nextcellule = prev
            prev = current
            current = next
        self.head = prev

    def decoupe(self, fonction):
        """Tri des éléments selon fonction().

        Parameters:
            fonction (function): fonction qui retourne un booléen

        """
        listes = [LinkedList() for _ in range(2)]

        # TODO:

        for liste in listes:
            liste.tail.nextcellule = None
        self.head, self.tail = None, None

        return listes

    def ordo(self, fonction):
        """Ordonne les valeurs selon fonction.

        Parameters:
            fonction (function): fonction qui retourne un booléen

        """
        pairs, impairs = self.decoupe(fonction)
        pairs.concatenation(impairs)

class LinkedListSentinelle:

    """Liste chaînée avec sentinelle.
    """

    def __init__(self, valeurs=None):
        """Initialisation de la class."""
        self.head = Cellule(None) #c'est une sentinelle
        self.tail = self.head
        if valeurs is not None:
            for valeur in valeurs:
                self.insertEnd(valeur)

    def insertEnd(self, valeur):
        """Ajoût en queue"""
        self.tail.nextcellule = Cellule(valeur)
        self.tail = self.tail.nextcellule

    def insertStart(self, valeur):
        """Ajoût en tête"""
        self.head.nextcellule = Cellule(valeur, self.head.nextcellule)

        if self.tail == self.head:
            self.tail = self.head.nextcellule

    def cells(self):
        """Yield les cellules de la liste chaînée."""
        actualcellule = self.head

        while actualcellule is not None:
            yield actualcellule
            actualcellule = actualcellule.nextcellule

    def valeurs(self):
        """Itère sur les valeurs."""
        cellules = self.cells()
        next(cellules)
        for cellule in cellules:
            yield cellule.valeur

    def del_cellule(self, valeur):
        """Supprimer la première cellule de valeur valeur."""
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
