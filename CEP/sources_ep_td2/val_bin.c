#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <inttypes.h>

/* Ce code n'est *pas* un exemple à suivre, il ne sert qu'à illuster
   le passage de plus de 8 paramètres à une fonction ! */

uint8_t val_binaire(uint8_t, uint8_t, uint8_t, uint8_t,
                    uint8_t, uint8_t, uint8_t, uint8_t,
                    uint8_t, uint8_t, uint8_t, uint8_t,
                    uint8_t, uint8_t, uint8_t, uint8_t);

uint8_t chiffre(char c)
{
   if (c == '0') {
      return 0;
   } else if (c == '1') {
      return 1;
   } else {
      printf("Erreur : %c n'est pas un chiffre binaire\n", c);
      exit(1);
   }
}

char titi[17];

void stringify(uint8_t s[16])
{
   for (int i = 0; i < 16; i++)
      titi[i] = '0' + s[i];
   titi[16] = 0;
}

int main(void)
{
   uint8_t toto[16] = {1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0};
   uint16_t val = val_binaire( toto[0],  toto[1],  toto[2],  toto[3],
                              toto[4],  toto[5],  toto[6],  toto[7],
                              toto[8],  toto[9], toto[10], toto[11],
                             toto[12], toto[13], toto[14], toto[15]);
   stringify(toto);
   printf("Valeur du nombre binaire %s = %" PRIx16 "\n", titi, val);
   return 0;
}
