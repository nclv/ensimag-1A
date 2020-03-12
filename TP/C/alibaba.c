#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <assert.h>

#include "alibaba.h"


// Liste doublement chaînée circulaire


struct _cellule {
    uint32_t val;
    struct _cellule *suiv;
    struct _cellule *prec;
};

/*
    Notre liste aura deux points d'entrée un en tête de liste l'autre en fin de liste.
    Pour éviter de traîner deux pointeurs, nous les mettrons dans une structure.
    Ceci aura pour avantage de n'avoir qu'une seule variable à traiter par liste.
*/
struct _ldc {
    uint32_t taille;
    cellule *tete;
    cellule *queue;
};

// initialiser les pointeurs d'entrée à NULL, obligatoire avant toute utilisation de la liste
void ldc_init(ldc *l) {
    l->tete = NULL;
    l->queue = NULL;
    l->taille = 0;
}

// insere la valeur n en fin (ou début car ciruclaire) de la liste pointee par l
void ldc_insere_fin(ldc *l, uint32_t n) {
    cellule *queue = (cellule *)malloc(sizeof(cellule));
    assert(queue != NULL);
    queue->val = n;
    if (l->queue) {
        queue->suiv = l->tete;
        queue->prec = l->queue;
        l->queue->suiv = queue;
    } else {
        queue->suiv = queue;
        queue->prec = queue;
        l->tete = queue;
    }
    l->queue = queue;
    ++(l->taille);
}

// affiche le contenu de la liste l
void ldc_affiche(ldc l) {
    cellule *tete = l.tete;
    uint32_t taille = ldc_taille(l);
    printf("Taille : %i \n", taille);
    while (taille != 0) {
        printf("%i -> ", tete->val);
        tete = tete->suiv;
        --taille;
    }
    printf("\n");
}

// retourne le nombre d'elements contenus dans l
uint32_t ldc_taille(ldc l) {
    return l.taille;
};

// supprime l'element e de la liste pointee par pl.
// precondition: *pl non vide, e non null, e dans *pl
void ldc_supprime(ldc *l, uint32_t e) {
    uint32_t taille = ldc_taille(*l);
    cellule *avant_recherchee = l->tete;
    assert(taille != 0);

    while (avant_recherchee->suiv != NULL && taille != 0 && avant_recherchee->suiv->val != e) {
        avant_recherchee = avant_recherchee->suiv;
        --taille;
    }

    if (avant_recherchee->suiv != NULL) {
        // on a trouve la cellule recherchée dans la liste
        cellule *recherchee = avant_recherchee->suiv;
        avant_recherchee->suiv = recherchee->suiv;
        recherchee->suiv->prec = avant_recherchee;
        if (recherchee == l->tete) {
            l->tete = recherchee->suiv;
        }
        if (recherchee == l->queue) {
            l->queue = avant_recherchee;
        }
        free(recherchee);
        --(l->taille);
    }

}

// vide la liste pointee par l, et libere la memoire.
// En sortie, l == NULL
void ldc_libere(ldc *l) {
    cellule *tete = l->tete;
    cellule_libere(tete);
    l = NULL;
    assert(l == NULL);
}

void cellule_libere(cellule *c) {
    if (c != NULL) {
        cellule_libere(c->suiv);
        free(c);
    }
}

int main(void) {

#ifdef TESTS
    ldc liste;

    ldc_init(&liste);
    ldc_affiche(liste);
    ldc_insere_fin(&liste, 1);
    ldc_affiche(liste);
    ldc_supprime(&liste, 1);
    ldc_affiche(liste);
    ldc_insere_fin(&liste, 2);
    ldc_affiche(liste);
    ldc_insere_fin(&liste, 3);
    ldc_insere_fin(&liste, 4);
    ldc_insere_fin(&liste, 5);
    ldc_affiche(liste);
    ldc_supprime(&liste, 3);
    ldc_affiche(liste);
    ldc_supprime(&liste, 5);
    ldc_affiche(liste);
    ldc_supprime(&liste, 2);
    ldc_affiche(liste);
    ldc_libere(&liste);
#else
    ldc voleurs;
    ldc_init(&voleurs);

    for (uint32_t i = 1; i <= 41; i++) {
        ldc_insere_fin(&voleurs, i);
    }
    ldc_affiche(voleurs);

    ldc perdants;
    ldc_init(&perdants);
    uint32_t arbitre = 3;

    while (ldc_taille(voleurs) > 2) {
        ldc_supprime(&voleurs, arbitre);
        ldc_insere_fin(&perdants, arbitre);
        arbitre += 3;
        arbitre %= 41;
    }
    ldc_affiche(voleurs);
    ldc_affiche(perdants);

#endif

    return EXIT_SUCCESS;
}
