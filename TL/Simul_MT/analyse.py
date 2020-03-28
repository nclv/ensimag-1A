#!/usr/bin/env python3

import sys
from mt import MT
from utils import image

def lire_mt(nom_fichier):

    def les_cars(nom_fichier):
        with open(nom_fichier, "r") as fichier:
            for ligne in fichier:
                for car in ligne:
                    yield car

    cars = les_cars(nom_fichier)
    car = None
    lig, col = 1, 0

    def avancer():
        nonlocal car, lig, col
        car = next(cars)  ## StopIteration en fin de fichier
        if car == '\n':
            lig += 1
            col = 0
        else:
            col += 1

    class FiniOK(Exception):
        pass

    class Mot():
        def __init__(self):
            self.m = ""
    le_mot = Mot()

    def message(m):
        return "l." + str(lig) + " c." + str(col) + " : " + m

    mt = MT()

    def is_sep():
        return car == ' ' or car == '\t' or car == '\n'

    def is_comm():
        return car == '/'

    def is_sep_comm():
        return is_sep() or is_comm()

    def pass_seps():
        while is_sep():
            avancer()

    def verif_seps():
        assert is_sep(), message("separateur attendu")
        avancer()
        pass_seps()

    def verif_sep_comm():
        if (is_comm()):
            avancer()
            assert car == '/', message("commentaire attendu")
            avancer()
            while car != '\n':
                avancer()
        avancer()

    def pass_seps_comms():
        while is_sep_comm():
            verif_sep_comm()

    def verif_seps_comms():
        assert is_sep_comm(), message("separateur ou commentaire attendu")
        verif_sep_comm()
        pass_seps_comms()

    def lire_symb():
        assert not is_sep(), message("symbole attendu")
        le_mot.m = car
        avancer()

    def lire_sigma():
        lire_symb()
        symb = le_mot.m
        assert symb != mt.blanc, message("blanc (" + mt.blanc +
               ") interdit dans Sigma")
        assert symb not in mt.sigma, message("symbole (" + symb +
               ") deux fois dans Sigma")
        mt.sigma.add(symb)
        mt.gamma.add(symb)

    def is_mouv():
        return car == 'G' or car == 'D' or car == 'S'

    def lire_mouv():
        assert is_mouv(), message("mouvement (G, D, S) attendu")
        le_mot.m = car
        avancer()

    def lire_etat():
        assert car.isalnum(), message("nom d'etat attendu")
        le_mot.m = car
        try:
            avancer()
            while car.isalnum():
                le_mot.m += car
                avancer()
        finally:
            mt.etats.add(le_mot.m)

    def verif(att):
        assert car == att, message(att + " attendu")
        avancer()


    def etats_finals_eventuels():
        if (car != '$'): # pas d'etat final
            return

        avancer() # passer '$'

        pass_seps_comms()

        while True:
            try:
                lire_etat()
                pass_seps_comms()
            except StopIteration:
                raise FiniOK
            finally:
                final = le_mot.m
                assert final not in mt.finals,\
                       message("double definition d'etat final (" +
                               final + ")")
                mt.finals.add(final)

            if (car != ','):
                return

            avancer() # passer ','
            pass_seps_comms()

    try:
        avancer()

        # ['#' symb]
        # -> blanc eventuel (symb, 'B' par defaut)
        pass_seps_comms()
        if (car == '#'):
            avancer()
            verif_seps()
            lire_symb()
            mt.blanc = le_mot.m
        else:
            mt.blanc = 'B'
        mt.gamma.add(mt.blanc)

        # '&' symb (',' symb)*
        # -> symboles de Sigma, obligatoire
        pass_seps_comms()
        verif('&')
        verif_seps()
        while True:
            lire_sigma()
            pass_seps_comms()
            if (car != ','): break
            avancer()
            pass_seps_comms()

        # '@' etat
        # -> etat initial, obligatoire
        verif('@')
        pass_seps()
        try:
            lire_etat()
            pass_seps_comms()
        except StopIteration:
            raise FiniOK
        finally:
            mt.init = le_mot.m

        # ['$' etats_finals]
        # -> etats finals, eventuellement aucun
        etats_finals_eventuels()

        ### Ici on est sorti OK si fini (pas de transition [1])

        # (transition)*
        # -> transitions, eventuellement aucune
        #                       EN FAIT AU MOINS UNE, VOIR [1]

        while True:
            ### Ici il FAUT une transition

            # source lu : but ecrit mouv
            #    <=> delta(source, but) = (but, ecrit, mouv)

            lire_etat()
            source = le_mot.m
            verif_seps()

            lire_symb()
            lu = le_mot.m
            mt.gamma.add(lu)
            pass_seps()

            verif(':')

            if source in mt.trans:
                assert (lu not in mt.trans[source]),\
                        message("double definition de transition sur " +
                                image((source, lu)))
            else:
                mt.trans[source] = { }

            pass_seps_comms()

            lire_etat()
            but = le_mot.m
            verif_seps()

            lire_symb()
            ecrit = le_mot.m
            mt.gamma.add(ecrit)
            verif_seps()

            try:
                lire_mouv()
                verif_seps_comms()
            except StopIteration:
                raise FiniOK       ### Seule facon de sortir OK de la boucle
            finally:
                mouv = le_mot.m
                mt.trans[source][lu] = (but, ecrit, mouv)

    except FiniOK:
        return mt

    except StopIteration:
        print("ERREUR : " + "fin de fichier inattendue", file = sys.stderr)
        sys.exit(1)

    except AssertionError as err:
        print("ERREUR : " + err.args[0], file = sys.stderr)
        sys.exit(1)


def main(fich_source, trace):
    mt = lire_mt(fich_source)
    if trace:
        mt.afficher()

def usage():
    print("usage :", sys.argv[0], "fichier_MT", "[ A ]",
          file = sys.stderr)
    print("        A pour afficher les composants de la MT",
          file = sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    if not (2 <= len(sys.argv) <= 3):
        usage()
    if len(sys.argv) == 2:
        main(sys.argv[1], False)
    elif sys.argv[2] == 'A':
        main(sys.argv[1], True)
    else:
        usage()
