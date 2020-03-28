#!/usr/bin/env python3

class Cellule:
    def __init__(self, symb, prec = None, suiv = None):
        self.symb, self.prec, self.suiv = symb, prec, suiv

class Ruban:
    def __init__(self, blanc, mot_init = ""):
        self.blanc = blanc
        self.debut = self.fin = self.tete = Cellule(blanc)
        for symb in mot_init:
            assert symb != blanc, blanc + "(blanc) interdit en init de ruban"
            self.fin.suiv = Cellule(symb, self.fin, None)
            self.fin = self.fin.suiv
        if self.debut.suiv:
            self.tete = self.debut.suiv

    def trans(self, Y, M):
        self.tete.symb = Y
        if M == 'G':
            if self.tete is self.debut:
                self.debut = Cellule(self.blanc, None, self.debut)
                self.tete.prec = self.debut
            self.tete = self.tete.prec
        elif M == 'D':
            if self.tete is self.fin:
                self.fin = Cellule(self.blanc, self.fin, None)
                self.tete.suiv = self.fin
            self.tete = self.tete.suiv

    def symb(self):
        return self.tete.symb

    '''
    utilitaires d'affichage
    '''

    def print_contenu_depuis(self, cell):
        cour = cell
        while cour:
            print(cour.symb, end='')
            cour = cour.suiv
        print()

    def print_contenu(self):
        self.print_contenu_depuis(self.debut)

    def print_depuis_tete(self):
        cour = self.tete
        while cour and cour.symb != self.blanc:
            print(cour.symb, end='')
            cour = cour.suiv
        print()

    def print_config(self, q, mle):
        cour = self.debut
        while cour is not self.tete and cour.symb == self.blanc:
            cour = cour.suiv

        diff_l = mle - len(q)
        print('[' + ' ' * (diff_l // 2), q, ' ' * ((diff_l + 1) // 2) + ']-',
              end = '')
        tmp = cour
        if tmp.symb != self.blanc:
            print('-', end = '')
        while tmp is not self.tete:
            print('-', end = '')
            tmp = tmp.suiv
        print('v')

        dec_ruban = mle + 1
        print(' ' * dec_ruban, "...", end = '')

        if cour.symb != self.blanc:
            print(self.blanc, end='')

        while cour is not self.tete:
            print(cour.symb, end='')
            cour = cour.suiv
        print(cour.symb, end='')
        dern = self.fin
        while dern is not cour and dern.symb == self.blanc:
            dern = dern.prec
        while cour is not dern:
            cour = cour.suiv
            print(cour.symb, end = '')
        if cour.symb != self.blanc:
            print(self.blanc, end='')
        print("...", end='')

    '''
    nettoyage pour fonction :
        'efface' tout ce qui est a gauche de la tete de lecture
        et tout ce qui est a partir du premier B au-dela de la tete
        autrement dit : le 'resultat' est entre la tete de lecture
        et le premier B (exclu)
    '''
    def nettoyer(self):
        cour = self.debut
        while cour is not self.tete:
            cour.symb = self.blanc
            cour = cour.suiv
        while cour is not self.fin and cour.symb != self.blanc :
            cour = cour.suiv
        while cour is not self.fin:
            cour = cour.suiv
            cour.symb = self.blanc
