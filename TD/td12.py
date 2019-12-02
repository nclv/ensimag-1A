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


from exceptions import Empty


class DoublyLinkedList:
    class _Node:
        __slots__ = "_data", "_previous", "_next"

        def __init__(self, data, prev, suivant):
            self._data = data
            self._previous = prev
            self._next = suivant

    def __init__(self):
        self._head = self._Node(None, None, None)
        self._tail = self._Node(None, None, None)
        self._head._next = self._tail
        self._tail._previous = self._head
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, element, precedent, suivant):
        new_node = self._Node(element, precedent, suivant)
        precedent._next = new_node
        suivant._previous = new_node
        self._size += 1
        return new_node

    def _delete_node(self, node):
        precedent = node._previous
        suivant = node._next
        precedent._next = suivant
        suivant._previous = precedent
        self._size -= 1
        element = node._data
        node._previous = node._next = node._data = None
        return element

    def insert_first(self, element):
        self._insert_between(element, self._head, self._head._next)

    def insert_last(self, element):
        self._insert_between(element, self._tail._previous, self._tail)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is  empty")
        return self._delete_node(self._head._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is  empty")
        return self._delete_node(self._tail._previous)

    def cells(self):
        """Yield les cellules de la liste chaînée."""
        actualcellule = self._head
        size = self._size
        while size:
            suivant = actualcellule._next
            yield actualcellule
            actualcellule = suivant
            size -= 1

    def removeDuplicateNode(self):
        # Checks whether list is empty
        if self.is_empty():
            return
        else:
            # Initially, current will point to head node
            actualcellule = self._head
            while actualcellule is not None:
                # index will point to node next to actualcellule
                nextactualcellule = actualcellule._next
                while nextactualcellule is not None:
                    if actualcellule._data == nextactualcellule._data:
                        # Store the duplicate node in temp
                        tmp = nextactualcellule
                        # nextactualcellule's previous node will point to node next to nextactualcellule thus, removes the duplicate node
                        nextactualcellule.previous._next = nextactualcellule._next
                        if nextactualcellule.next is not None:
                            nextactualcellule._next._previous = (
                                nextactualcellule._previous
                            )
                        # Delete duplicate node by making tmp to None
                        tmp = None
                    nextactualcellule = nextactualcellule._next
                actualcellule = actualcellule._next


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
                self.insert_end(element)

    # O(1) !!!
    def insert_start(self, valeur):
        """Insertion d'une cellule en tête.

        Parameters:
            valeur ():

        """
        self.head = Cellule(valeur, self.head)

        if self.tail is None:
            self.tail = self.head

    # O(1)
    def insert_end(self, valeur):
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

        actualcellule = self.head
        previouscellule = None

        while actualcellule.valeur != valeur:
            previouscellule = actualcellule
            actualcellule = actualcellule.nextcellule

        if previouscellule is None:
            self.head = actualcellule.nextcellule
        else:
            previouscellule.nextcellule = actualcellule.nextcellule

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
        while current is not None:
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
        """Initialisation de la class.

        Parameters:
            valeurs (list): //

        """
        self.tail = Cellule(float("+inf"))  # c'est une sentinelle de queue
        self.head = Cellule(float("-inf"), self.tail)  # c'est une sentinelle de tête
        self.taille = 0
        # on insère en tête
        if valeurs is not None:
            for valeur in sorted(valeurs, reverse=True):
                self.insert_start(valeur)

    def insert_start(self, valeur):
        """Ajoût en tête"""
        self.head.nextcellule = Cellule(valeur, self.head.nextcellule)
        self.taille += 1

    def insert(self, valeur):
        """Ajoût dans la liste triée"""
        actualcellule = self.head
        # la sentinelle de fin préserve d'un ajoût en queue
        while actualcellule.nextcellule.valeur < valeur:
            actualcellule = actualcellule.nextcellule

        actualcellule.nextcellule = Cellule(valeur, actualcellule.nextcellule)
        self.taille += 1

    def cells(self):
        """Yield les cellules de la liste chaînée (sans sentinelles)."""
        actualcellule = self.head.nextcellule
        while actualcellule != self.tail:
            yield actualcellule
            actualcellule = actualcellule.nextcellule

    def valeurs(self):
        """Itère sur les valeurs."""
        for cellule in self.cells():
            yield cellule.valeur

    def del_cellule(self):
        """Supprimer les doublons."""
        actualcellule = self.head
        while actualcellule != self.tail:
            cellulesuivant = actualcellule.nextcellule
            if cellulesuivant.valeur == actualcellule.valeur:
                actualcellule.nextcellule = cellulesuivant.nextcellule
                self.taille -= 1
            else:
                actualcellule = cellulesuivant.nextcellule

    def fusion(self, autre):
        """Fusionne deux listes."""
        res = LinkedListSentinelle()
        actualcellules = [self.head.nextcellule, autre.head.nextcellule]
        last_cellule = res.head

        for _ in range(self.taille + autre.taille):
            valeurs = [cellule.valeurs for cellule in actualcellules]
            indice_min = valeurs[1] < valeurs[0]
            last_cellule.nextcellule = actualcellules[indice_min]
            actualcellules[indice_min] = actualcellules[indice_min].nextcellule
            last_cellule = last_cellule.nextcellule

        last_cellule.nextcellule = res.tail
        self.head, self.tail = res.head, res.tail
        self.taille += autre.taille
        autre.head.nextcellule = autre.tail
