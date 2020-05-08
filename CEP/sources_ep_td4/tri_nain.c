#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <inttypes.h>

#define TAILLE 10000
#define STR_M(s) #s
#define STR(s) STR_M(s)
#define OPTIM (defined OPT) || (defined SUPEROPT)

int32_t tab[TAILLE];
int32_t ref[TAILLE];

void tri_nain(int32_t[], uint32_t);

void tri_nain_opt(int32_t[], uint32_t);

void tri_nain_superopt(int32_t[], uint32_t);

static void afficher_tab(int32_t tab[], uint32_t taille)
{
   for (uint32_t i = 0; i < taille; i++) {
      printf("%" PRId32 " ", tab[i]);
   }
   printf("\n");
}

static void init_tabs(int32_t tab[], int32_t ref[], uint32_t taille)
{
   for (uint32_t i = 0; i < taille; i++) {
      tab[i] = (random() % 19) - 9;
   }
   memcpy(ref, tab, sizeof(int32_t) * taille);
}

int comp(const void *a, const void *b)
{
   return (int)(*(int32_t *)a - *(int32_t *)b);
}

/* Adresse contenant une horloge temps-réel (rtc) */
#define CLINT_TIMER   0x0200bff8
static uint64_t maintenant(void)
{
   return *(volatile uint64_t *)CLINT_TIMER;
}


int main(void)
{
   printf("Test sur un tableau de petite taille (10)\n");
   uint32_t taille = 10;

   srandom(0xbaffe);
   init_tabs(tab, ref, taille);

   printf("Tableau initial : ");
   afficher_tab(tab, taille);

   qsort(ref, taille, sizeof(int32_t), comp);
#ifndef OPT
   tri_nain(tab, taille);
#else
   tri_nain_opt(tab, taille);
#endif
   printf("Tableau trie par le nain : ");
   afficher_tab(tab, taille);

   if (memcmp(ref, tab, sizeof(int32_t) * taille) != 0) {
      printf("Erreur : le nain a mal trie un tableau (sale bete !)\n");
      exit(EXIT_FAILURE);
   }

   printf("Test de performance sur un tableau de grande taille (" STR(TAILLE) ")\n");
   uint64_t qt, dt, odt, sdt; /* qsort time, dwarf sort time, optimized dt */

   taille = TAILLE;
   init_tabs(tab, ref, taille);
   dt = maintenant();
   tri_nain(tab, taille);
   dt = maintenant() - dt;
#if OPTIM
   memcpy(tab, ref, sizeof(int32_t) * taille);
   odt = maintenant();
   tri_nain_opt(tab, taille);
   odt = maintenant() - odt;
#endif
#ifdef SUPEROPT
   memcpy(tab, ref, sizeof(int32_t) * taille);
   sdt = maintenant();
   tri_nain_superopt(tab, taille);
   sdt = maintenant() - sdt;
#endif
   qt = maintenant();
   qsort(ref, taille, sizeof(int32_t), comp);
   qt = maintenant() - qt;
   if (memcmp(ref, tab, sizeof(int32_t) * taille) != 0) {
      printf("Erreur : le nain a mal trie un tableau (sale bete !)\n");
      exit(EXIT_FAILURE);
   }
   printf("Tri de reference :               %" PRIu32 " nsec.\n", (uint32_t)qt);
   printf("Tri par le nain :               %" PRIu32 " nsec.\n", (uint32_t)dt);
#if OPTIM
   printf("Tri par le nain optimisé:       %" PRIu32 " nsec.\n", (uint32_t)odt);
#endif
#ifdef SUPEROPT
   printf("Tri par le nain super-optimisé: %" PRIu32 " nsec.\n", (uint32_t)sdt);
#endif
   return EXIT_SUCCESS;
}
