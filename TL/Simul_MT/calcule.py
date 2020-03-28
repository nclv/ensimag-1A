#!/usr/bin/env python3

def calcule(nom_fichier, donnee, trace, pas_a_pas):
    from simule import simule

    (etat, est_final, nb_pas, r) = simule(nom_fichier, donnee,
                                          trace, pas_a_pas)

    if est_final:
        print("etat final       -> dans le domaine (en", nb_pas, "pas)")
        r.nettoyer()
        print("résultat (entre la tête et le premier blanc) :")
        r.print_depuis_tete()
        print()
    else:
        print("etat non final   -> hors du domaine (apres", nb_pas, "pas)")


if __name__ == "__main__":
    from utils import exec_arg
    exec_arg(calcule, "la_donnee")
