#include "cep_platform.h"
.text
.globl reveil
/* void reveil(uint32_t delta_t); */
reveil:
/* A completer */
    ret

.globl gestion_interruptions
gestion_interruptions:
    addi sp, sp, -4 # Juste ra à sauver
    sw   ra, 0(sp)
    andi t0, a0, 0xf
    li   t1, IRQ_M_TMR  # Interruption d'horloge
    bne  t0, t1, interruption_externe
    jal  mon_vecteur_horloge
    j    retour
interruption_externe:
    /* À compléter : gestion des boutons poussoirs */
retour:
    lw   ra, 0(sp)
    addi sp, sp, 4
    ret

    .data
    .globl param
/* struct compt *param; */
param: .long 0x0
