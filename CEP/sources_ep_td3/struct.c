#include <stdio.h>
#include <inttypes.h>

struct structure_t {
   int32_t entier;
   char *ptr;
};

extern void affichage(struct structure_t);
extern void modification(uint32_t, char *, struct structure_t *);

extern struct rect_t double_rect(struct rect_t);

void affiche(uint32_t entier, char *ptr)
{
   printf("entier = %" PRId32 ", ptr = 0x%" PRIX32 "\n", entier, (uint32_t) ptr);
}

int main(void)
{
   struct structure_t s = {-1, (char *)0xBADC0FFE};
   affichage(s);
   modification(5, (char *) 0xDEADC0DE, &s);
   affichage(s);
   return 0;
}
