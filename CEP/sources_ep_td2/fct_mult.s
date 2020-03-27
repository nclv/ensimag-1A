/*
uint32_t mult(uint32_t x, uint32_t y);
{
    uint32_t res = 0;
    while (y != 0) {
        res = res + x;
        y--;
    }
    return res;
}
*/
    .text
    /* uint32_t mult(uint32_t x, uint32_t y); */
    .globl mult
/* Contexte Imposé :
   Fonction feuille: pas d'espace réservé dans la pile pour d'éventuels paramètres de fonction appelée [np=0 voir notation du cours],
   ni pour sauvegarder ra ni aucun registre [nr=0 voir notation du cours],
   on place la variable locale  dans la pile [nv=1 voir notation du cours] 
   x : a0
   y : a1
   res: à l'adresse sp+0
   => La fonction doit réserver dans la pile (np+nv+nr)*4 octets, ici 4 octets pour la variable locale res
   => Pile + 4 
*/

mult:
    /* on reserve la place nécessaire dans la pile */
    addi sp, sp, -4
    /* res = 0; */
    sw   zero, 0(sp) /* ici, 0(sp) n'est pas une étiquette mais un registre donc pas besoin d'un 3e argument pour le calcul de l'adresse (elle est déjà donnée: sp + 0) */
    /* while (y != 0) { */
while:
    beqz a1, fin_while
    /* res = res + x */
    lw   t0, 0(sp) /* bien mettre le 0(...), sinon sp est compris comme une étiquette */
    add  t0, t0, a0
    sw   t0, 0(sp)
    /* y-- */
    addi a1, a1, -1
    /* } */
    j while
fin_while:
    /* return res; */
    lw   a0, 0(sp)
    addi sp, sp, 4 /* on libère la pile */
    ret
/* On peut remarquer que le contexte imposé ici utilise la pile pour la variable locale alors que la fonction est une fonction feuille. Par la suite, on placera les variables locales en pile que si la fonction est non-feuille (contient un appel d'un sous-fonction) ou si le contexte donné l'impose. */
