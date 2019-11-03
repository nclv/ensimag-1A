# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
On fait une analyse de texte pour dessiner le graphe des mots suivants.
Permet l'utilisation de dictionnaires et une imbrication de structures.
On se sert des donnees pour generer des phrases aleatoires.
"""


import sys
from re import finditer
from random import choice, choices
from os import system


def mots(nom_fichier):
    """
    renvoie un iterateur sur tous les mots du fichier.
    elimine au passage tout ce qui n'est pas une lettre.
    """
    with open(nom_fichier, "r") as fichier:
        for ligne in fichier:
            for mot in finditer("[a-zA-Z]+", ligne):
                yield mot.group(0)


def couples(iterateur):
    """
    renvoie un iterateur sur tous les couples d'elements successifs
    de l'iterateur donne.
    """
    valeur_precedente = next(iterateur)
    for valeur in iterateur:
        yield valeur_precedente, valeur
        valeur_precedente = valeur


def compte_mots_suivants(nom_fichier):
    """
    renvoie un dict associant a chaque mot m1 du fichier
    un dict associant a chaque mot m2 suivant m1 dans le fichier
    le nombre de fois ou m2 apparait apres m1.
    """
    suivants = dict()

    for mot_precedent, mot in couples(mots(nom_fichier)):
        key_already_exist = (
            mot_precedent in suivants.keys() and mot in suivants[mot_precedent].keys()
        )
        if key_already_exist:
            suivants[mot_precedent][mot] += 1
        else:
            suivants.setdefault(mot_precedent, {})[mot] = 1
    print(suivants)
    return suivants


def affiche_graphe(suivants):
    """
    affiche le graphe dans le terminal.
    attention : petits textes seulement.
    """
    with open("test.dot", "w") as fichier_dot:
        fichier_dot.write("digraph g {\n")
        for mot1, dictionnaire in suivants.items():
            for mot2, value in dictionnaire.items():
                fichier_dot.write(f"{mot1} -> {mot2} [ label={value} ];\n")
        fichier_dot.write("}\n")

    system("dot -Tpng test.dot -o test.png")
    system("display test.png")


def analyse_texte():
    """
    analyse le fichier donne en argument et dessine le graphe
    des mots suivants.
    """
    if len(sys.argv) != 2:
        print("utilisation :", sys.argv[0], "fichier_texte")
        sys.exit(1)
    suivants = compte_mots_suivants(sys.argv[1])
    # affiche_graphe(suivants)
    # une petite phrase aleatoire.
    mot_depart = choice(list(suivants.keys()))
    phrase = [mot_depart]
    for _ in range(10):
        # print("phrase", phrase)
        phrase.append(suivant_aleatoire(phrase[-1], suivants))
    print(" ".join(phrase))


def suivant_aleatoire(mot, suivants):
    """
    tire aleatoirement (uniformement en fonction des frequences)
    un suivant du mot donne.
    si le mot donne n'a pas de suivant, retourne un mot aleatoire.
    """
    result = None
    # print(mot)
    weights, mots = [], []
    somme = sum(list(suivants[mot].values()))
    for mot, value in suivants[mot].items():
        weights.append(value / somme)
        mots.append(mot)
    # print(somme, mots, weights)
    result = mots[0] if len(mots) == 1 else choices(mots, weights=weights)[0]
    return result


if __name__ == "__main__":
    analyse_texte()
