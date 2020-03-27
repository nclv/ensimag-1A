/*
uint32_t pgcd(uint32_t a, uint32_t b)
{
    while (a != b) {
        if (a < b) {
            b = b - a;
        } else {
            a = a - b;
        }
    }
    return a;
}

*/
    .text
    .globl pgcd
    /* uint32_t pgcd(uint32_t a, uint32_t b) */
/* Contexte :
    Fonction feuille pas d'espace reservé dans la pile
    a : a0
    b : a1
*/
pgcd:
    /* while (a != b) {  */
while:
    beq  a0, a1, fin /*Saut à fin si a==b*/
    /* if (a < b) {  */
    sltu t0, a0, a1 /*Le registre t0 est utilisé pour stocker le résultat du 
test a<b*/
    beqz t0, else /*zero est l'alias de zero */
    /* b = b - a;  */
    sub  a1, a1, a0
    j    fin_if
    /* } else {  */
else:
    /* a = a - b;  */
    sub  a0, a0, a1
    /*  }  */
fin_if:
    /*  }  */
    j    while
    /* return a; */
fin:
    /* Par convention, le registre a0 (x10) contient la valeur de retour.
       Nos calculs mettant à jour a0, ce registre contient bien la valeur du pgcd.
       Par convention encore, l'adresse de retour dans la fonction appelante est
       stockée dans le registre ra (x1) */
    ret
