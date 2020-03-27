#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

extern uint32_t somme(void);
extern uint32_t sommeMem(void);
extern uint8_t somme8(void);

int main(void)
{
   printf("Somme(1 .. 10)  = %" PRIu32 "\n", somme());
   printf("SommeMem(1 .. 10)  = %" PRIu32 "\n", sommeMem());
   printf("Somme8(1 .. 24)  = %" PRIu8 "\n", somme8());
   return 0;
}
