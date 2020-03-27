#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

extern uint32_t mult_simple(void);
extern uint32_t mult_egypt(void);
extern uint32_t mult_native(void);
static uint32_t mult_c(void);

uint32_t x, y;

typedef struct {
   uint32_t(*func) ();
   char *id;
} my_mult;

enum mult_poly {
   c,
   simple,
   egypt,
   native,
   mult_nb
};

static my_mult mults[mult_nb] = {
   {mult_c, "Res. attendu"},
   {mult_simple, "Mult. simple"},
   {mult_egypt, "Mult. egypt."},
   {mult_native, "Mult. native"}
};

static uint32_t mult_c(void)
{
   return x * y;
}

static void test(uint32_t xi, uint32_t yi)
{
   printf("Multiplication de %" PRIu32 " par %" PRIu32 ":\n", xi, yi);
   for (uint8_t i = 0; i < mult_nb; i++) {
      x = xi;
      y = yi;
      printf("%s : %" PRIu32 "\n", mults[i].id, mults[i].func());
   }
   printf("\n");
}

/* Adresse contenant une horloge temps-réel (rtc) */
#define CLINT_TIMER   0x0200bff8
static uint64_t maintenant(void)
{
   return *(volatile uint64_t *) CLINT_TIMER;
}

static void test_perf(uint32_t cpt, my_mult * mult)
{
   uint32_t prod;
   uint64_t temps = maintenant();
   for (uint32_t i = 0; i < cpt; i++) {
      x = 2;
      y = (1u << 29) - 1;
      prod = mult->func();
   }
   temps = maintenant() - temps;
   printf("%s : %" PRIu32 " (temps d'execution : %u nanosecondes pour %" PRIu32 " iteration%s) \n",
          mult->id, prod, (unsigned) temps, cpt, cpt > 1 ? "s" : "");
}

static uint32_t acq(const char *nb)
{
   /* On réserve 16 caractères pour les saisies de chaines.
    * Même si on pourrait descendre à 11, car un nombre de 32bits
    * tient même sur 10 symboles décimaux + \0 */
   char tampon[16];

   printf("Multiplication non-signée : Entrez le %s opérande\n", nb);
   fgets(tampon, 16, stdin);
   return strtoul(tampon, NULL, 0);
}

int main(void)
{
   printf("Test interactif\n");
   uint32_t xi, yi;
   xi = acq("premier");
   yi = acq("deuxième");
   test(xi, yi);

   printf("Tests supplémentaires\n");
   test(5, 16);
   test(20, 54);

   printf("Test de performance sur la multiplication de 2 par 2^29-1\n");
   test_perf(1, mults);
   test_perf(1, mults + 1);
   test_perf(10000000, mults + 2);
   test_perf(10000000, mults + 3);
   return 0;
}
