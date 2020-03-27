# -*- coding: utf-8 -*-
#!/usr/bin/env python3


class Cellule:
    """
    une cellule d’une liste. contient une valeur, un pointeur
    vers la cellule suivante, un compteur comptabilisant
    combien de listes ou de cellules pointent dessus.
    """

    # pylint: disable=too-few-public-methods
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant
        self.utilisation = 1


class Liste:
    """
    liste de cellules.
    des listes differentes peuvent partager des cellules communes.
    """

    def __init__(self, mot):
        """
        transforme un mot en liste non-partagee.
        """
        premiere_cellule = None
        self.taille = 0
        for lettre in reversed(mot):
            premiere_cellule = Cellule(lettre, premiere_cellule)
            self.taille += 1
        self.tete = premiere_cellule

    def cellules(self):
        """
        iterateur sur toute les cellules de la liste.
        """
        cellule_courante = self.tete
        while cellule_courante is not None:
            yield cellule_courante
            cellule_courante = cellule_courante.suivant

    def suffixe(self, autre):
        """
        ajoute la liste autre a la fin de la liste self
        (en partageant les cellules communes).
        si la fin de self etait deja partagee avec quelqu’un, alors
        on dedouble toute la partie partagee avant l’ajout.
        """
        # TODO
        pass

    def __del__(self):
        """
        destructeur.
        """
        # TODO
        pass
