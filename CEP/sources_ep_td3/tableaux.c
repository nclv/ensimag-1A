#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <inttypes.h>

#define TAILLE_MAX 150

void tri_min(int32_t tab[], uint32_t taille);

void afficher_tab(int32_t tab[], uint32_t taille)
{
   for (uint32_t i = 0; i < taille; i++) {
      printf("%" PRId32 " ", tab[i]);
   }
   printf("\n");
}

int comp(const void *a, const void *b)
{
   return *(int32_t *) a - *(int32_t *) b;
}

int main(void)
{
   uint32_t taille;
   char tampon[16];
   do {
      printf("Entrez la taille du tableau voulue (< TAILLE_MAX)\n");
      fgets(tampon, 16, stdin);
      taille = strtoul(tampon, NULL, 0);
   } while (taille > TAILLE_MAX);

   int32_t *tab = (int32_t *)malloc(taille * sizeof(int32_t));
   if (tab == NULL) {
      printf("Erreur, allocation de tab impossible !\n");
      exit(1);
   }

   srandom(666); /* Diabolique, n'est-il pas ? */

   for (uint32_t i = 0; i < taille; i++) {
      tab[i] = (random() % 666) - 333;
   }

   if (taille < 20) {
      printf("Tableau initial : ");
      afficher_tab(tab, taille);
   }
   /*Réservation de tableau pour le tri de référence et le tri optimisé */
   int32_t *ref = malloc(taille * sizeof(int32_t));
   if (ref == NULL) {
      printf("Erreur, allocation de ref impossible !\n");
      exit(1);
   }
   memcpy(ref, tab, sizeof(int32_t) * taille);

   /* Tri de référence */
   qsort(ref, taille, sizeof(int32_t), comp);

   /* Tri avec la version systématique */
   tri_min(tab, taille);
   if (taille < 20) {
      printf("Tableau trie par recherche du minimum : ");
      afficher_tab(tab, taille);
   }
   if (memcmp(ref, tab, sizeof(int32_t)* taille) == 0) {
      printf("Tri par recherche du minimum conforme\n");
   } else {
      printf("Erreur : le tri par recherche du minimum n'est pas correct !\n");
      exit(1);
   }
   return 0;
}
