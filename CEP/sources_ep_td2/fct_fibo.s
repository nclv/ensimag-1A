/*
uint32_t fibo(uint32_t n);
{
    uint32_t fibo_temp;
    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
	fibo_temp = fibo(n - 1);
        return fibo_temp + fibo(n - 2);
    }
}
*/
    .text
    /* uint32_t fibo(uint32_t n) */
    .globl fibo
/* Contexte :
   Fonction non feuille => besoin de sauvegarder :
   - la place pour les paramètres des fonctions appelées si supérieur à 8 [notation np du cours, np=0]
   - la variable locale fibo_temp [notation nv du cours, nv=1]
   - le registre ra et le paramètre que l'on doit retrouver au retour [notation nr du cours, nr=2]

   => La fonction doit réserver dans la pile (np+nv+nr)*4 octets
   => Pile + 12

Conventions utilisées
    adresse de retour : ra ou pile sp+8
    n : registre a0 ou pile à sp+4
    fibo_temp : à l'adresse sp+0
    PILE:
    sp+0 : place pour la variable locale fibo_temp 
    sp+4 : place pour permettre à la fonction de sauvegarder son registre a0, paramètre n
    sp+8 : place de l'adresse de retour (ra) dans la pile
*/

fibo:
    /* on reserve la place nécessaire dans la pile */
    addi sp, sp, -12
    /* on y sauvegarde l'adresse de retour */
    sw   ra, 8(sp)
    /* Et le paramètre n */
    sw   a0, 4(sp)
    /* if (n == 0) */
    bnez a0, elsif
    /* return 0; */
    j    fin
elsif:
    /* else if (n == 1) */
    li   t0, 1
    bne  a0, t0, else
    /* return 1; */
    j    fin
else:
    /* fibo_temp = fibo(n - 1)
       on place n-1 dans a0
    */
    addi a0, a0, -1
    jal  fibo
    /* stocke la valeur retournée dans fibo_temp */
    sw   a0, 0(sp)

    /* restauration du parametre n initial (a0 pu être modifié dans la fonction appelée)*/
    lw   a0, 4(sp)
    /* on appelle maintenant fibo(n - 2) */
    addi a0, a0, -2
    jal  fibo
    /* et on calcule la somme finale en mettant fibo_temp dans t0 */
    lw   t0, 0(sp)
    add  a0, a0, t0
fin:
    lw   ra, 8(sp)  /* on recharge ra avec l'adresse de retour de la pile */
    addi sp, sp, 12 /* on libère la pile */
    ret
