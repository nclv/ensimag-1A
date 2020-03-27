#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

extern uint32_t mult(uint32_t, uint32_t);

static uint32_t acq(const char *nb)
{
   char tampon[16];
   printf("Multiplication non-signée : Entrez le %s opérande\n", nb);
   fgets(tampon, 16, stdin);
   return strtoul(tampon, NULL, 0);
}

int main(void)
{
   uint32_t a, b;
   a = acq("premier");
   b = acq("deuxième");
   printf("%" PRIu32 " x %" PRIu32 " = %" PRIu32 "\n", a, b, mult(a, b));
   return 0;
}
