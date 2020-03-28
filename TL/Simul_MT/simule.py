#!/usr/bin/env python3

def simule(nom_fichier, mot, trace, pas_a_pas):
    from analyse import lire_mt
    from ruban import Ruban
    from utils import image

    m = lire_mt(nom_fichier)
    for s in mot:
        assert s in m.sigma, "symbole pas dans Sigma : " + s
    r = Ruban(m.blanc, mot)
    q = m.init;
    nb_pas = 0
    max_len_etats = max([len(e) for e in m.etats])
    Configuration = "Configuration"
    Dec_Transition = 20
    Dec_trans = (len(Configuration) + Dec_Transition) * ' '
    try:
        if trace:
            print("Configuration" + Dec_Transition * ' ' +"Transition")
        while True:
            if trace:
                r.print_config(q, max_len_etats)
                if pas_a_pas:
                    input()
                else:
                    print()
            etat_symb = (q, r.symb())
            t = m.trans[q][r.symb()] # -> KeyError si indefini
            nb_pas += 1
            if trace:
                print(Dec_trans + "[" + str(nb_pas) + "]  " +
                      image((q, r.symb())) + "  ->  " + image(t))
            q = t[0]
            r.trans(t[1], t[2])
    except KeyError:
        if trace:
            print(Dec_trans + "pas de transition, execution terminee")
        return (q, q in m.finals, nb_pas, r)


if __name__ == "__main__":
    from utils import exec_arg
    exec_arg(simule, "le_mot")
