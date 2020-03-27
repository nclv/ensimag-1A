#!/usr/bin/env python3
"""
manipulations complexes de tableaux : listes d'intervalles.
"""


import itertools


# Utility Generator Function
def groupc(test_list):
    """group values

    """
    for _, element in itertools.groupby(enumerate(test_list), lambda value: value[1] - value[0]):
        element = list(element)
        yield [element[0][1], element[-1][1] + 1]

class Ressources:
    """
    On stocke une liste de ressources, compressee par plages contigues.
    """
    def __init__(self, nombre_ressources, intervalles=None):
        # requiert : si intervalles is not None, alors :
        #            - les intervalles sont non vides
        #            - les intervalles sont non contigus
        #            - les intervalles sont tries par indices croissants
        #            - intervalles[-1][1] <= nombre_ressources
        self.nombre_ressources = nombre_ressources
        if intervalles is not None:
            self.intervalles = intervalles
        else:
            self.intervalles = [[0, nombre_ressources]]

    def get_indices(self):
        """flatten self.intervalles

        """
        return [r for intervalle in self.intervalles for r in list(range(intervalle[0], intervalle[-1]))]

    def disponible(self, indice):
        """renvoie si l'indice donne est disponible dans la ressource.

        """
        return any(indice in range(intervalle[0], intervalle[-1]) for intervalle in self.intervalles)

    def reserve(self, ressources_demandees):
        """enleve le nombre de ressources demandees (premieres disponibles).
        renvoie les ressources correspondant aux plages reservees.

        """
        #oneline extend
        indices = self.get_indices()
        self.intervalles = list(groupc(indices[ressources_demandees:]))
        self.nombre_ressources -= ressources_demandees

        return Ressources(ressources_demandees, intervalles=list(groupc(indices[:ressources_demandees])))


    def retourne(self, ressources_rendues):
        """remet les plages de ressources donnees dans le systeme.

        """
        self.intervalles.extend(ressources_rendues.intervalles)
        self.intervalles.sort() #utile ?
        self.nombre_ressources += ressources_rendues.nombre_ressources

    def __str__(self):
        """renvoie une chaine 'visuelle' des ressources contenues dans self.
        par exemple, '|x..xxxxx..|' indique qu'il y a 10 ressources,
        les ressources 0, 3-7 sont disponibles.

        """
        indices = self.get_indices()
        representation = ["x"]*(indices[-1] + 1) if indices else []
        for indice, _ in enumerate(representation):
            if indice not in indices:
                representation[indice] = "."
        return f"{''.join(representation)}"

def test():
    """on teste en gruyerisant une ressource.

    """
    print(list(groupc([1, 2, 3, 5, 6, 7, 9, 10])))

    ressources = Ressources(10)
    print("Disponibles :", ressources)
    reservees = [ressources.reserve(c) for c in (2, 2, 3, 2, 1)]
    for reservee in reservees:
        print("Reservées :", reservee)
    print("Disponibles :", ressources)
    ressources.retourne(reservees[1])
    print("Disponibles :", ressources)
    ressources.retourne(reservees[3])
    print("Disponibles :", ressources)
    print("Reservees   :", ressources.reserve(3))
    print("Disponibles :", ressources)
    print("Les intervalles :", ressources.intervalles)

if __name__ == "__main__":
    test()
