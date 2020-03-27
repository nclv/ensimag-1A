#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
// Ces deux variables globales sont publiques, de manière à pourvoir être
// utilisées dans le fichier assembleur fct_pgcd.s.
// L'utilisation de variables globales est généralement à proscrire.
// Leur présence dans cet exercice est uniquement à but pédagogique
uint32_t a = 5;
uint32_t b = 25;

// Déclaration de la fonction pgcd_as définie dans fct_pgcd.s
extern uint32_t pgcd_as(void);

// Définition de la fonction pgcd_c
static uint32_t pgcd_c(void)
{
   uint32_t i = a;
   uint32_t j = b;
   while (i != j) {
      if (i < j) {
         j = j - i;
      } else {
         i = i - j;
      }
   }
   return i;
}

int main(void)
{
   uint32_t res_c = pgcd_c();
   uint32_t res_as = pgcd_as();
   printf("PGCD calculé\n\ten C : %" PRIu32 "\n\ten assembleur: %" PRIu32 "\n", res_c, res_as);
   return 0;
}
