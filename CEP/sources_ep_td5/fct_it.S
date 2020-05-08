#include "cep_platform.h"
.text
/*
uint8_t blink;
void mon_vecteur(void)
{
    - Sauvegarde en pile des registres utilisés dans le traitant
    - lecture des boutons poussoirs pour faire baisser l'interruption externe
    - lecture du registre claim acquitter l'interruption au niveau du contrôleur
    - blink = ~blink
    - ecriture de blink sur les LED (adresse 0x30000000)
    - Restauration des registres sauvegardés
    - Retour de traitant (instruction mret)
}
*/
.globl mon_vecteur

mon_vecteur:
    /* sauvegarde en pile des registres utilisés dans le traitant */
    addi sp, sp, -12
    sw   t0, 0(sp)
    sw   t1, 4(sp)
    sw   t2, 8(sp)
    /* lecture des boutons poussoirs pour acquitter l'interruption niveau périphérique */
    li   t1, REG_PINS_ADDR
    lw   t2, 0(t1)
    /* blink = ~blink; */
    la   t1, blink
    lbu  t0, (t1)
    xori t0, t0, 0xF
    sb   t0, (t1)

    /* écriture de blink sur les LED

       Les deux premières instructions qui suivent sont une version optimisée de
            li   t1, REG_LEDS_ADDR
            sb   t0, 0(t1)
       En effet, (%hi( ) et %lo( ) sont des macros qui sélectionnent des parties
       de la constante REG_LEDS_ADDR. On peut donc faire l'écriture en 2
       instructions plutôt que 3.
       C'est ainsi qu'est traduite la pseudo-instruction
            sb   t0, REG_LEDS_ADDR, t1
    */
    lui  t1, %hi(REG_LEDS_ADDR)
    sb   t0, %lo(REG_LEDS_ADDR)(t1)
    /* restauration des registres sauvegardés */
    lw   t0, 0(sp)
    lw   t1, 4(sp)
    lw   t2, 8(sp)
    addi sp, sp, 12
    /* retour vers l'instruction interrompue (mret) */
    mret

/* fonction d'attente fournie permettant de lever certaines erreurs */
.globl attente_infinie
attente_infinie:
    mv   t0, zero
    mv   t1, zero
    mv   t2, zero
boucle:
    bne  t0, t2, erreur
    addi t0,t0,1
    bne  t1, t2, erreur
    addi t1,t1,1
    bne  t0, t1, erreur
    addi t2,t2,1
    j    boucle

.data
/* uint8_t blink; */
.lcomm blink, 1
