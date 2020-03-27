/*
uint8_t res8;
uint32_t res;

uint32_t somme(void)
{
    uint32_t i;
    uint32_t res = 0;
    for (i = 1; i <= 10; i++) {
        res = res + i;
    }
    return res;
}

uint32_t sommeMem(void)
{
    uint32_t i;
    for (i = 1; i <= 10; i++) {
        res = res + i;
    }
    return res;
}

uint8_t somme8(void)
{
    uint8_t i;
    res8 = 0;
    for (i = 1; i <= 24; i++) {
        res8 = res8 + i;
    }
    return res8;
}
*/
    .text
    .globl somme
somme:
/*  Contexte : à préciser */
#  $$$ etd_strip_begin
/* i : variable locale dans le registre t0 */
/* res : variable locale dans le registre t1 */
    /* res = 0; */
    addi t1, zero, 0
    /* for (i = 1; */
    addi t0, zero,  1
for:
    /* i <= 10; */
    slti t2, t0, 11
    beqz t2, fin_for
    /* res = res + i; */
    add  t1, t1, t0
    /* i++) */
    addi t0, t0, 1
    /* } */
    j    for
fin_for:
    /* return res; */
    mv   a0, t1
    ret
#  $$$ etd_strip_end


    .globl sommeMem
sommeMem:
/*  Contexte : à préciser */
#  $$$ etd_strip_begin
/* Contexte :
   i : variable locale dans le registre t0 
   res : variable en mémoire, reserver dans zone .data 
*/
/* attention, à la différence du mips ou at ($1) était 
   implicitement utilisé pour les calculs intermédiaires
   dans les macros, il faut avec le riscv explicitement
   indiquer un registre temporaire, qui sera écrasé:
   visible ici dans les stores */
    /* res = 0; */
    sw   zero, res, t2
    /* for (i = 1; */
    li   t0, 1
formem:
    /* i <= 11; */
    slti t1, t0, 11
    beqz t1, fin_formem
    /* res = res + i; */
    lw   t1, res
    add  t1, t1, t0
    sw   t1, res, t2
    /* i++) */
    addi t0, t0, 1
    /* } */
    j    formem
fin_formem:
    /* return res; */
    lw   a0, res
    ret
#  $$$ etd_strip_end


    .globl somme8
somme8:
/*  Contexte : à préciser */
#  $$$ etd_strip_begin
/* Contexte :
   i : variable locale dans le registre t0 
   res8 : variable en mémoire, reserver dans zone .data 
   Attention : on reserve ici un seul octet
*/
    /* res8 = 0; */
    sb   zero, res8, t2
    /* for (i = 1; */
    li   t0, 1
for8:
    /* i <= 24; */
    slti t1, t0, 25
    beqz t1, fin_for8
    /* res8 = res8 + i; */
    lbu  t1, res8
    add  t1, t1, t0
    sb   t1, res8, t2
    /* i++) */
    addi t0, t0, 1
    /* } */
    j    for8
fin_for8:
    /* return res8; */
    lbu  a0, res8
    ret
#  $$$ etd_strip_end

    .data
/* uint32_t res;
 la variable globale res étant définie dans ce fichier, il est nécessaire de
 la définir dans la section .data du programme assembleur : par exemple, avec 
 la directive .comm vu qu'elle n'est pas initialisée (idem pour res8)
*/

#  $$$ etd_strip_begin
.comm res, 4
.comm res8,1
#  $$$ etd_strip_end
