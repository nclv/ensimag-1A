#include <stdio.h>
#include "cep_platform.h"

extern void attente_infinie();

void erreur()
{
   printf("Contexte de la boucle d'attente alteree par votre traitant.\n");
   attente_infinie();
}

int main(void)
{
   /* Autorisation globale des interruptions dans mstatus */
   __asm__("csrw mstatus, %0" :: "i"(MSTATUS_MIE));
   /* Prise en compte uniquement des interruptions "machine" externes dans mie */
   const uint32_t irq_ext = 1 << IRQ_M_EXT;
   __asm__("csrw mie, %0":: "r"(irq_ext));

   /* Configuration du PLIC pour autoriser l'irq 2 (sur laquelle sont reliés les boutons) */
   *(volatile uint32_t *)PLIC_ENABLE = 1 << PLIC_IRQ_2;
   *(volatile uint32_t *)PLIC_TARGET = 0;
   *(volatile uint32_t *)(PLIC_SOURCE + 4 * PLIC_IRQ_2) = 1;


   /* Configuration des boutons poussoirs en mode interruption */
   *(volatile uint32_t *)REG_PUSHBUTTON_CTL_ADDR = REG_PUSHBUTTON_MODE_INT;
   attente_infinie();
   return 0;
}
