
#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

uint32_t fibo(uint32_t);

int main()
{
   char tampon[16];
   printf("Entrez l'entier non signé à utiliser en entrée de fibo \n");
   fgets(tampon, 16, stdin);
   uint32_t n = strtoul(tampon, NULL, 0);
   printf("Fibo(%" PRIu32 ") = %" PRIu32 "\n", n, fibo(n));
   return 0;
}
