    .text
/*
uint32_t x, y;
*/
/*

uint32_t mult_simple(void)
{
    res = 0;
    while (y != 0) {
        res = res + x;
        y--;
    }
    return res;
}
*/
    .globl mult_simple
mult_simple:
#  $$$ etd_strip_begin
/*
   Contexte: 
   res variable en memoire (reserver espace ici dans la zone data)
   x et y variables globales en memoire (deja reserve dans le fichier .c)
*/
    /* res = 0 */
    sw zero, res, t2
    /* while (y != 0) */
while:
    lw   t0, y
    beqz t0, fin_while
    /* res = res + x */
    lw   t0, x
    lw   t1, res
    add  t1, t1, t0
    sw   t1, res, t2
    /* y-- */
    lw   t0, y
    addi t0, t0, -1
    sw   t0, y, t2
    /* } */
    j    while
fin_while:
    /* return res; */
    lw   a0, res

#  $$$ etd_strip_end
    ret

/*
uint32_t mult_egypt(void)
{
    uint32_t res = 0;
    while (y != 0) {
        if (y % 2 == 1) {
            res = res + x;
        }
        x = x << 1 ;
        y = y >> 1;
    }
    return res;
}
*/
    .globl mult_egypt
mult_egypt:
/* Contexte : ??*/
#  $$$ etd_strip_begin
/*
   Contexte: 
   res variable locale dans le registre t0
   x et y variables globales en memoire
*/
    /* Attention, res est une variable locale que l'on mettra dans t0 */
    /* uint32_t res = 0; */
    mv   t0, zero 
    /* while (y != 0) */
while_e:
    lw   t1, y
    beqz t1, fin_while_e
    /* if (y % 2 == 1) */
    lw   t1, y    
    andi t1, t1, 1
    beqz t1, fin_if
    /* res = res + x */
    lw   t1, x
    add  t0, t0, t1
fin_if:
    /*  x = x << 1 ; */
    lw   t1, x
    slli  t1, t1, 1
    sw   t1, x, t2
    /* y = y >> 1 ; */
    lw   t1, y
    srli  t1, t1, 1
    sw   t1, y, t2
    /* } */
    j    while_e
fin_while_e:
    /* return res; */
    mv   a0, t0
#  $$$ etd_strip_end
    ret

/*
uint32_t mult_native(void)
{
    return x*y;
}
*/
    .globl mult_native
mult_native:
#  $$$ etd_strip_begin
/*
   Contexte: 
   x et y variables globales en memoire
*/
    /* return x * y */
    lw   t0, x
    lw   t1, y
    mul  a0, t0, t1
#  $$$ etd_strip_end
    ret


    .data
/* uint32_t res; */
#  $$$ etd_strip_begin
.comm res, 4
#  $$$ etd_strip_end
