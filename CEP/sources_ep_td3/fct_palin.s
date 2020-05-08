/*
bool palin(const char *ch)
{
    uint32_t inf, sup;
    inf = 0;
    sup = strlen(ch) - 1;
    while (inf < sup && ch[inf] == ch[sup]) {
        inf++;
        sup--;
    }
    return inf >= sup;
}
*/
    .text
    .globl palin
    /* bool palin(char *ch) */
/* Contexte : À remplir */
#  $$$ ------ Début de la partie corrigée ------
/* Fonction non feuille (sauvergarde de ra + 2 variables locales + le paramètre)
   => pile + 16
    ra   : pile à sp+12
    ch   : pile à sp+8
    sup  : pile à sp+4
    inf  : pile à sp+0
 */
#  $$$ ------ Fin de la partie corrigée ------
palin:
#  $$$ ------ Début de la partie corrigée ------
    /* prologue */
    addi sp, sp, -16
    sw   ra, 12(sp)
    /* inf = 0; */
    sw   zero, 0(sp)
    /* sup = strlen(ch) - 1; */
    sw   a0, 8(sp) /* sauvegarde ch, strlen pouvant le modifier */
    jal  strlen
    addi t0, a0, -1
    sw   t0, 4(sp)
    lw   a0, 8(sp) /* restauration ch */
while:
    /* while (inf < sup) && (ch[inf] == ch[sup]); */
    lw   t0, 0(sp)
    lw   t1, 4(sp)
    slt  t2, t0, t1 /* première condition dans t2 */
    beqz t2, fin_while
    add  t0, t0, a0
    lbu  t0, (t0)
    add  t1, t1, a0
    lbu  t1, (t1)
    bne  t0, t1, fin_while
    /*     inf++ */
    lw   t0, 0(sp)
    addi t0, t0, 1
    sw   t0, 0(sp)
    /*     sup-- */
    lw   t0, 4(sp)
    addi t0, t0, -1
    sw   t0, 4(sp)
    /* } */
    j    while
fin_while:
    /*  return inf >= sup */
    lw   t0, 0(sp)
    lw   t1, 4(sp)
    slt  t2, t0, t1 /* test inf < sup */
    xori a0, t2, 1  /* Inverse le bit 0 */
    /* épilogue */
    lw   ra, 12(sp)
    addi sp, sp, 16
#  $$$ ------ Fin de la partie corrigée ------
    ret
