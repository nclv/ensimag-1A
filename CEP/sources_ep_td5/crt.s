.section .text.init,"ax",@progbits
.equ   STACK_SIZE,   1024
.globl _start

_start:
    # adresse du vecteur/traitant d'interruption
    la   t0, mon_vecteur
    csrw mtvec, t0

    # réservation d'une (petite) zone de mémoire pour la pile
    la   sp, stacks + STACK_SIZE

    # lance la bibliothèque minimaliste et appelle main
    j    libfemto_start_main

    .bss
    .align 4
    .global stacks
stacks:
    .skip STACK_SIZE
