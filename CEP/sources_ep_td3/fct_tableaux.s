/*
void tri_min(int32_t tab[], uint32_t taille)
{
    uint32_t i, j, ix_min;
    int32_t tmp;
    for (i = 0; i < taille - 1; i++) {
        for (ix_min = i, j = i + 1; j < taille; j++) {
            if (tab[j] < tab[ix_min]) {
                ix_min = j;
            }
        }
        tmp = tab[i];
        tab[i] = tab[ix_min];
        tab[ix_min] = tmp;
    }
}
*/
    .text
    .globl tri_min
/* void tri_min(int32_t tab[], uint32_t taille) */
/* Contexte : à définir
#   $$$ ------ Début de la partie corrigée ------
    Rien en pile
    * tab     : registre a0, paramètre de type (int32_t [])
    * taille  : registre a1, paramètre de type (uint32_t)
    * i       : registre t0, variable locale de type (uint32_t)
    * j       : registre t1, variable locale de type (uint32_t)
    * ix_min  : registre t2, variable locale de type (uint32_t)
    * tmp     : registre t3, variable locale de type (int32_t)
#   $$$ ------ Fin de la partie corrigée ------
*/
tri_min:
#   $$$ ------ Début de la partie corrigée ------
/*     for (i = 0;     */
    li   t0, 0
for1_opt:
/*     ; i < taille - 1; */
    addi t3, a1, -1      /* taille-1 dans t3 */
    sltu t3, t0, t3
    beqz t3, fin_for1_opt
/*         for (ix_min = i, j = i + 1;  */
    mv   t2, t0
    addi t1, t0, 1
for2_opt:
/*         ; j < taille;  */
    sltu t3, t1, a1
    beqz t3, fin_for2_opt
/*             if (tab[j] < tab[ix_min]) { */
    sll  t3, t1, 2
    add  t3, t3, a0
    lw   t3, (t3) /* tab[j] dans t3 */
    sll  t4, t2, 2
    add  t4, t4, a0 /* &tab[ix_min] dans t4 */
    lw   t5, (t4) /* tab[ix_min] dans t5 */
    slt  t6, t3, t5
    beqz t6, fin_if_opt
/*                 ix_min = j; */
    add  t2, t1, zero
 fin_if_opt:
/*        ; j++) {*/
    addi t1, t1, 1
    j    for2_opt
 fin_for2_opt:
/*         tmp = tab[i]; */
    sll  t6, t0, 2
    add  t6, t6, a0 /* &tab[i] dans t6 */
    lw   t3, (t6)
/*         tab[i] = tab[ix_min]; */
/* 5 prochaines instructions inutiles en code non-systématique */
    sll  t4, t2, 2
    add  t4, t4, a0 /* &tab[ix_min] dans t4 */
    lw   t5, (t4) /* tab[ix_min] dans t5 */
    sll  t6, t0, 2
    add  t6, t6, a0 /* &tab[i] dans t6 */
    sw   t5, (t6)
/*         tab[ix_min] = tmp; */
/* 2 prochaines instructions inutiles en code non-systématique */
    sll  t4, t2, 2
    add  t4, t4, a0 /* &tab[ix_min] dans t4 */
    sw   t3, (t4)
/*     }
    for ( ... ; i++) { */
    addi t0, t0, 1
    j    for1_opt
fin_for1_opt:
/* } */
#   $$$ ------ Fin de la partie corrigée ------
    ret
