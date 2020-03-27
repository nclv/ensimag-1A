#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

uint32_t fact(uint32_t);

void erreur_fact(uint32_t n)
{
   printf("Fact(%" PRIu32 ") ne tient pas sur 32 bits !\n", n);
   // la fonction exit arrete proprement le programme
   exit(1);
}

int main()
{
   char tampon[16];
   printf("Entrez l'entier non signé à utiliser en entrée de fact \n");
   fgets(tampon, 16, stdin);
   uint32_t n = strtoul(tampon, NULL, 0);
   printf("Fact(%" PRIu32 ") = %" PRIu32 "\n", n, fact(n));
   return 0;
}
