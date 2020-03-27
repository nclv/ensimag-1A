#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

uint32_t age(uint32_t);

int main(void)
{
   printf("usage: annee_naissance\n");
   uint16_t annee = 1999;
   printf("Vous avez donc %" PRIu32 " ans !\n", age(annee));
   return 0;
}
