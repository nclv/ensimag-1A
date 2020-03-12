#include <stdint.h>

#ifndef _ALIBABA_H_
#define _ALIBABA_H_

typedef struct _cellule cellule;
typedef struct _ldc ldc;

extern void ldc_init(ldc *pl);

// insere la valeur n en fin de la liste pointee par l
// circulaire donc équivalent à ajouter en tete
extern void ldc_insere_fin(ldc *pl, uint32_t n);

// affiche le contenu de la liste l
extern void ldc_affiche(ldc l);

// retourne le nombre d'elements contenus dans l
extern uint32_t ldc_taille(ldc l);

// supprime l'element e de la liste pointee par pl.
// precondition: *pl non vide, e non null, e dans *pl
extern void ldc_supprime(ldc *pl, uint32_t e);

// vide la liste pointee par l, et libere la memoire.
// En sortie, *l == NULL
extern void ldc_libere(ldc *l);
extern void cellule_libere(cellule *c);

#endif
