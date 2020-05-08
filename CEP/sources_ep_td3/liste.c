#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

struct cellule_t {
   int32_t val;
   struct cellule_t *suiv;
};

void inverse(struct cellule_t **l);

struct cellule_t *decoupe(struct cellule_t *l, struct cellule_t **l1, struct cellule_t **l2);

static struct cellule_t *cree_liste(int32_t tab[])
{
   struct cellule_t *liste = NULL;
   for (uint32_t i = 0; tab[i] != -1; i++) {
      struct cellule_t *cell = malloc(sizeof(struct cellule_t));
      if (cell == NULL) {
         printf("Erreur : malloc retourne NULL\n");
         exit(1);
      }
      cell->val = tab[i];
      cell->suiv = liste;
      liste = cell;
   }
   return liste;
}

static void affiche_liste(struct cellule_t *liste)
{
   while (liste != NULL) {
      printf("%" PRId32 " -> ", liste->val);
      liste = liste->suiv;
   }
   printf("FIN\n");
}

static void detruit_liste(struct cellule_t *liste)
{
   while (liste != NULL) {
      struct cellule_t *suiv = liste->suiv;
      free(liste);
      liste = suiv;
   }
}

static void test(int32_t tableau[])
{
   struct cellule_t *liste, *l1, *l2;
   printf("Tableau initial : ");
   for (uint32_t i = 0; tableau[i] != -1; i++) {
      printf("%" PRId32 " ", tableau[i]);
   }
   printf("\n");
   liste = cree_liste(tableau);
   printf("Liste initiale : ");
   affiche_liste(liste);
   printf("Liste inversee : ");
   inverse(&liste);
   affiche_liste(liste);
   liste = decoupe(liste, &l1, &l2);
   printf("Liste initiale apres le decoupage : ");
   affiche_liste(liste);
   printf("Liste des elements impairs : ");
   affiche_liste(l1);
   printf("Liste des elements pairs : ");
   affiche_liste(l2);
   detruit_liste(liste);
   detruit_liste(l1);
   detruit_liste(l2);
}

int main(void)
{
   const uint32_t taille_tab = 11;
   int32_t tableau[taille_tab];
   srandom(0xdeadbeef);
   printf("** Test d'un tableau quelconque **\n");
   for (uint32_t i = 0; i < taille_tab - 1; i++) {
      tableau[i] = random() % 10;
   }
   tableau[taille_tab - 1] = -1;
   test(tableau);
   printf("\n** Test d'un tableau avec seulement des elements pairs **\n");
   for (uint32_t i = 0; i < taille_tab - 1; i++) {
      tableau[i] = (random() % 10) & ~1;
   }
   tableau[taille_tab - 1] = -1;
   test(tableau);
   printf("\n** Test d'un tableau avec seulement des elements impairs **\n");
   for (uint32_t i = 0; i < taille_tab - 1; i++) {
      tableau[i] = (random() % 10) | 1;
   }
   tableau[taille_tab - 1] = -1;
   test(tableau);
   printf("\n** Test d'un tableau vide **\n");
   tableau[0] = -1;
   test(tableau);
   return 0;
}
