#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

// Déclaration de la fonction mult définie dans fct_mult.s
extern uint32_t mult(uint32_t a, uint32_t x);
// Déclaration de la fonction affine définie dans fct_affine.s
extern uint32_t affine(uint32_t a, uint32_t b, uint32_t x);

uint32_t affine_c(uint32_t a, uint32_t b, uint32_t x)
{
   return mult(x, a) + b;
}

int main()
{
   uint32_t res_as = affine(2, 3, 4);
   printf("affine(2,3,4) calculé en assembleur: %" PRIu32 " et en C: %" PRIu32 "\n", res_as, affine_c(2, 3, 4));
   return 0;
}
