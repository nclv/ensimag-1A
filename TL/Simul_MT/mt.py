#!/usr/bin/env python3

def seq_ens_trie(ens):
    return ", ".join(sorted(ens))

class MT:

    def __init__(self):
        self.etats = set()
        self.gamma = set()
        self.sigma = set()
        self.blanc = None
        self.init = None
        self.finals = set()
        self.trans = { } ## dict(key = etat) de dict(key=lu)

    '''
    Affiche les 7 constituants
    Les "ensembles" sont tries
    Les transitions sont triees par etat source et pour un etat source
    par symbole lu
    '''
    def afficher(self):
        from utils import image

        print ("etats : {", seq_ens_trie(self.etats), "}")
        print ("Gamma : {", seq_ens_trie(self.gamma), "}")
        print ("Sigma : {", seq_ens_trie(self.sigma), "}")
        print ("blanc :", self.blanc)
        print ("etat initial :", self.init)

        if  len(self.finals) == 0:
            print("PAS D'ETAT FINAL")
        elif len(self.finals) == 1:
            print("etat final :", list(self.finals)[0])
        else:
            print ("etats finals : {", seq_ens_trie(self.finals), "}")

        if len(self.trans) == 0:
            print("PAS DE TRANSITION")
            return
        print("transitions :")
        for (source, trans) in sorted(self.trans.items()):
            for (lu, triplet) in sorted(trans.items()):
                print ("  " + image ((source, lu)) + " -> " + image (triplet))


    '''
    Forme externe, dans le fichier nom_fichier
    Les "ensembles" sont tries
    Les transitions sont triees par etat source et pour un etat source
    par symbole lu
    '''
    def ecrire(self, nom_fichier):
        with open(nom_fichier, "w") as f:
            if self.blanc != 'B':   ## pas obligatoire
                print('#', self.blanc, file=f)
            print('&', seq_ens_trie(self.sigma), file=f)
            print('@', self.init, file=f)
            if self.finals:
                print('$', seq_ens_trie(self.finals), file=f)
            print(file=f)
            for (source, trans) in sorted(self.trans.items()):
                for (lu, (but, ecrit, mouv)) in sorted(trans.items()):
                    print (source, lu, ":", but, ecrit, mouv, file=f)

    '''
    Codage dans ZOU = {0, 1}, resultat dans nom_fichier
    Precondition : self est en forme normale :
                      - l'etat initial n'est pas final,
                      - un seul etat final
    '''
    def vers_ZOU(self, nom_fichier):
        assert self.init not in self.finals
        assert len(self.finals) == 1
        final = list(self.finals)[0]
        ## assert final not in self.trans

        def dico(ens, cle):

            ens_trie = sorted(ens, key=cle)

            def sequences_de_zeros():
                n = 1
                while True:
                    yield '0' * n
                    n += 1

            return dict(zip(ens_trie, sequences_de_zeros()))

        def dict_etats(): ## init : 1, final : 2, puis : 3, 4..., ordre lexico
            def cle(etat):
                if (etat == self.init):
                    return "1" + etat
                elif (etat == final):
                    return "2" + etat
                else:
                    return "3" + etat
            return dico(self.etats, cle)

        def dict_symbs(): ## blanc : 1, puis : 2, 3..., ordre lexico
            def cle(symb):
                if (symb == self.blanc):
                    return "1" + symb
                else:
                    return "2" + symb
            return dico(self.gamma, cle)

        with open(nom_fichier, "w") as f:
            d_etats = dict_etats()
            d_symbs = dict_symbs()
            d_mouvs = dict(zip(['G', 'D', 'S'], ['0', '00', '000']))
            for (source, trans) in sorted(self.trans.items()):
                for (lu, (but, ecrit, mouv)) in sorted(trans.items()):
                    '''
                    ## pas de fin de ligne
                    print(d_etats[source]  + '1' +
                          d_symbs[lu]    + '1' +
                          d_etats[but]   + '1' +
                          d_symbs[ecrit] + '1' +
                          d_mouvs[mouv]  + '1', end='', file=f)
                    '''
                    '''
                    ## fin de ligne apres chaque trans
                    '''
                    print(d_etats[source]  + '1' +
                          d_symbs[lu]    + '1' +
                          d_etats[but]   + '1' +
                          d_symbs[ecrit] + '1' +
                          d_mouvs[mouv]  + '1', file=f)

    '''
    Decodage depuis ZOU = {0, 1} dans un fichier
    Precondition : self est en forme normale :
                      - l'etat initial n'est pas final,
                      - un seul etat final
    '''
    def depuis_ZOU(self, nom_fichier):
        self.etats = set(["1", "2"])
        self.init = "1"
        self.finals = set(["2"])
        self.sigma = set(['0', '1'])
        self.blanc = 'B'
        self.gamma = self.sigma.copy()
        self.gamma.add(self.blanc)
        self.trans = { } ## dict(key = etat) de dict(key=lu)

        import string
        utilisables = list(string.printable)
        symbs = ['dummy', '0', '1', 'B']
        a_enlever = ['0', '1', 'B', ' ', '\t', '\r', '\n', '\x0b', '\x0c']
        for s in a_enlever:
            utilisables.remove(s)
        symbs.extend(utilisables)

        mouvs = ['dummy', 'G', 'D', 'S']

        def ZOU():
            with open(nom_fichier, "r") as zou:
                for ligne in zou:
                    for car in ligne:
                        if car == '\n':
                            continue
                        if not (car == '0' or car == '1'):
                            import sys
                            print("'0' ou '1' attendu", file = sys.stderr)
                            sys.exit(1)
                        yield car

        iter = ZOU()

        class Fini(Exception):
            pass

        class Fini_OK(Exception): ## soit que des transitions valides
                                  ## soit dans ZOU*, mais pas valide
            pass

        def lire_trans():
            def attendu(lu, ZOU):
                if lu != ZOU:
                    raise Fini_OK

            def lire_zeros():
                try:
                    lu = next(iter)
                except StopIteration:
                    raise Fini
                attendu(lu, '0')
                n = 1
                while True:
                    lu = next(iter)
                    if lu != '0': break
                    n += 1
                attendu(lu, '1')
                return n

            def lire_etat():
                etat = str(lire_zeros())
                self.etats.add(etat)
                return etat

            def lire_symb():
                symb = symbs[lire_zeros()]
                self.gamma.add(symb)
                return symb

            def lire_mouv():
                mouv = mouvs[lire_zeros()]
                return mouv

            try:
                try:
                    source = lire_etat()
                except Fini:
                    raise Fini_OK ## plus de transition
                lu = lire_symb()
                but = lire_etat()
                ecrit = lire_symb()
                mouv = lire_mouv()


                if source in self.trans:
                    assert (lu not in self.trans[source]),\
                            message("double definition de transition sur " +
                                    image((source, lu)))
                else:
                    self.trans[source] = { }
                self.trans[source][lu] = (but, ecrit, mouv)
            except Fini: ## dans ZOU*, mais pas valide -> pas de trans
                self.trans = { }
                raise Fini_OK

        def les_trans():
            try:
                while True:
                    lire_trans()
            except Fini_OK:
                pass

        les_trans()
