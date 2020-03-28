#!/usr/bin/env python3

def accepte(nom_fichier, mot, trace, pas_a_pas):
    from simule import simule

    (etat, est_final, nb_pas, r) = simule(nom_fichier, mot,
                                          trace, pas_a_pas)

    if est_final:
        print("etat final -> mot accepte (en", nb_pas, "pas)")
    else:
        print("etat non final -> mot non accepte (apres", nb_pas, "pas)")


if __name__ == "__main__":
    from utils import exec_arg
    exec_arg(accepte, "le_mot")
