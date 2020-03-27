#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

// Déclaration de la fonction pgcd_as définie dans fct_pgcd.s
extern uint32_t pgcd(uint32_t a, uint32_t b);

int main()
{
   uint32_t res_as = pgcd(5, 25);
   printf("PGCD(5,25) calculé en assembleur: %" PRIu32 "\n", res_as);
   return 0;
}
