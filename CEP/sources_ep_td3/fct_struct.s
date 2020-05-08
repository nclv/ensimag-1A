/*
void affichage(struct structure_t s)
{
    affiche(s.entier, s.ptr);
}
*/
    .text
    .globl affichage
/* void affichage(struct structure_t s) */
/* Contexte :
#  $$$ ------ Début de la partie corrigée ------
    Fonction non feuille : Besoin de sauvegarder ra uniquement, car s n'est
                           pas réutilisé après le retour de l'appel
    => PILE + 4
    s : registres a0 et a1, paramètre de type (struct structure_t) dont le
        champ entier de type (int32_t) est en a0 et le champ ptr de type (char *)
        est dans a1.

    s.entier           : registre a0 (champ de type int32_t)
    s.ptr              : registre a1 (champ de type char *)
    adresse de retour  : pile à sp+0 (registre ra initialement)
#  $$$ ------ Fin de la partie corrigée ------
*/
affichage:
#   $$$ ------ Début de la partie corrigée ------
    /* prologue */
    addi sp, sp, -4
    sw   ra, 0(sp)
    /* rien à faire, car l'ABI riscv utilise les registres dans l'ordre des membres
       de la structure pour les agrégats <= 64 bits.
       Si on voulait d'abord passer ptr et ensuite entier, il faudrait échanger les
       contenus de a0 et de a1 */
    /* affiche(s.entier, s.ptr); */
    jal  affiche
    /* epilogue */
    lw   ra, 0(sp)
    addi sp, sp, 4
#   $$$ ------ Fin de la partie corrigée ------
    ret

/*
void modification(int32_t entier, char *p, struct structure_t *s)
{
    s->entier = entier;
    s->ptr = p;
}
*/
    .globl modification
/* void modification(int32_t e, char *p, struct structure_t *ps) */
/* Contexte :
    Fonction feuille sans variables locales : pile inchangée
    e  : registre a0, argument de type (int32_t)
    p  : registre a1, argument de type (char *)
    ps : registre a2, argument de type (struct structure_t *)
*/
modification:
#   $$$ ------ Début de la partie corrigée ------
    /* ps->entier = e; */
    sw   a0, 0(a2)
    /* ps->ptr = p; */
    sw   a1, 4(a2)
    /* } */
#   $$$ ------ Fin de la partie corrigée ------
    ret
