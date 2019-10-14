# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Nicolas VINCENT

Tableau de tuple(note, etudiant)
donnees[note][0] : nombre d'étudiants de note < note
donnees[note][1] : ordre alphabétique d'étudiants de note note
"""


import random


NOMBRE_NOTES = 101 # de 0 à 100 inclu
LISTE_ETUDIANTS = 1

def conversion(etudiants):
    """Renvoie le tableau donnees

    Parameters:
        etudiants (tuple): (note, etudiant)

    Returns:
        donnees (list): //

    """
    donnees = [[None, []] for _ in range(NOMBRE_NOTES)]
    for note, etudiant in etudiants:
        donnees[note][LISTE_ETUDIANTS].append(etudiant)

    compteur = 0
    for note, listes in enumerate(donnees):
        listes[0] = compteur
        listes[LISTE_ETUDIANTS] = sorted(listes[LISTE_ETUDIANTS])
        compteur += len(listes[LISTE_ETUDIANTS])

    return donnees

def etudiant_aleatoire(donnees, note):
    """Renvoie un étudiant aléatoire de de note note

    Parameters:
        donnees (list): //

    Returns:
        etudiant (str) aléatoire ou None

    """
    etudiants = donnees[note][LISTE_ETUDIANTS]
    return random.choice(etudiants) if etudiants else None

def moyenne(donnees):
    """Fais la moyenne des notes

    Parameters:
        donnees (list): //

    """
    somme, nb_etudiant = 0, 0
    for note, couple in enumerate(donnees):
        for _ in couple[1]:
            somme += note
            nb_etudiant += 1

    return somme/nb_etudiant


def seuil(donnees, limite):
    """Renvoie le nombre d'étudiants en dessus de limite

    Parameters:
        donnees (list): //
        limite (int): seuil à ne pas dépasser

    """
    nb_etudiant = donnees[-1][0] + len(donnees[-1][1])
    return nb_etudiant - donnees[limite][0]

def dichotomie_notes(donnees, rang):
    """Renvoie la note correspondant au rang donné

    """
    portee = [0, len(donnees) - 1]
    index = portee[1]//2
    compte, etudiants = donnees[index]
    while compte >= rang or compte + len(etudiants) < rang:
        if compte >= rang:
            portee[1] = index - 1
        else:
            portee[0] = index + 1
        index = (portee[0] + portee[1])//2
        compte, etudiants = donnees[index]
    return index

def mediane(donnees):
    """Renvoie la médiane des notes

    Parameters:
        donnees (list): //

    """
    nb_etudiant = donnees[-1][0] + len(donnees[-1][1])
    rang = nb_etudiant//2
    return dichotomie_notes(donnees, rang)


def n_eme(donnees, rang):
    """Renvoie le nième étudiant en partant du bas

    Parameters:
        donnees (list): //
        rang (int):

    """
    note = dichotomie_notes(donnees, rang)
    compte, etudiants = donnees[note]
    return etudiants[rang - compte - 1]

def main():
    """main function

    """

    etudiants = [(0, "a"), (20, "b"), (5, "c")]
    donnees = conversion(etudiants)
    print(donnees)

main()
