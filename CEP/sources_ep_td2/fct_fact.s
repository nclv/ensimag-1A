/*
uint32_t fact(uint32_t n)
{
    if (n <= 1) {
        return 1;
    } else {
        return n * fact(n - 1);
    }
}
*/

/* Pour aller plus loin :
   remplacer la ligne du return par :

    uint64_t tmp = n*fact(n-1);
    if ((tmp >> 32) > 0)
        erreur_fact(n);
    return (uint32_t)tmp;

   On impose de plus le placement de tmp dans un registre temporaire
*/

    .text
    .globl fact
    /* uint32_t fact(uint32_t n) */
/* Contexte :  
    A remplir
*/
fact:
/* A compléter */
    ret

