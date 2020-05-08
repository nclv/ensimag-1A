#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
#include "cep_platform.h"

#define TICK_ALARM 10000000

extern struct compteur {
   uint32_t tics;            /* valeur actuelle du compteur */
   void     (*sens)(void);   /* pointeur de fonction de type void funcname(void) donnant le sens de comptage */
} *param;                    /* variable globale de type pointeur sur struct compteur */

extern void reveil(uint32_t delta_t); /* À écrire en assembleur */

void incremente(void)
{
   param->tics++;
}

void decremente(void)
{
   param->tics--;
}

void bulle(void)
{
}

#if 0
/* version C du traitant, qui sera utilisée en pratique à la place de l'assembleur dans cep_exp.S */
void mon_vecteur(uintptr_t mcause)
{
   if (mcause & 0x80000000) {
      printf("Traitant d'interruption");
      if ((mcause & 0xf) == IRQ_M_TMR) { /* timer : changer la date acquitte l'interruption */
         printf("\ttimer : Appel n° %" PRIu32 "\n", param->tics);
         set_alarm(TICK_ALARM);
         param->sens();
      } else {                           /* Ce ne peut être que l'interruption externe */
         printf("\tbtns  : Appel n° %" PRIu32 "\n", param->tics);
         volatile uint32_t btns, xxxx;
         btns = *(volatile uint32_t *)REG_BTNS_ADDR;
         if (btns & 0x1)
            param->tics = 0;
         else if (btns & 0x2)
            param->sens = incremente;
         else if (btns & 0x4)
            param->sens = decremente;
         else
            param->sens = bulle;

         xxxx = *(volatile uint32_t *)PLIC_IRQ_CLAIM;
         *(volatile uint32_t *)PLIC_IRQ_CLAIM = xxxx;
      }
   } else {
      printf("Exception non gérée, bonjour chez vous !\n");
      exit(1);
   }
}
#endif

void mon_vecteur_horloge(void)
{
   printf("Traitant d'interruption\ttimer : Appel n° %" PRIu32 "\n", param->tics);
   reveil(TICK_ALARM);
   param->sens();
}

int main(void)
{
   /* Autorisation globale des interruptions dans mstatus */
   __asm__("csrw mstatus, %0" :: "i"(MSTATUS_MIE));
   /* Prise en compte uniquement des interruptions "machine" externes et du timer "machine" dans mie */
   const uint32_t irq = (1 << IRQ_M_EXT) | (1 << IRQ_M_TMR);
   __asm__("csrw mie, %0":: "r"(irq));

   /* Configuration du PLIC pour autoriser l'irq 2 (sur laquelle sont reliés les boutons) */
   *(volatile uint32_t *)PLIC_ENABLE = 1 << PLIC_IRQ_2;
   *(volatile uint32_t *)PLIC_TARGET = 0;
   *(volatile uint32_t *)(PLIC_SOURCE + 4 * PLIC_IRQ_2) = 1;

   /* Configuration des boutons poussoirs en mode interruption */
   *(volatile uint32_t *)REG_PUSHBUTTON_CTL_ADDR = REG_PUSHBUTTON_MODE_INT;

   struct compteur inst = {.tics = 0,.sens = incremente};
   param = &inst;

   /* Démarrage du timer */
   reveil(TICK_ALARM);

   while (param->tics <= 100);
   return 0;
}
