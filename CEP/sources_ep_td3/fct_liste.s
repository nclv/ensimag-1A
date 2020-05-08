/*
void inverse(struct cellule_t **l)
{
   struct cellule_t *res, *suiv;
   res = NULL;
   while (*l != NULL) {
       suiv = (*l)->suiv;
       (*l)->suiv = res;
       res = *l;
       *l = suiv;
   }
   *l = res;
}
*/
    .text
    .globl inverse

/* void inverse(struct cellule_t **l) */
/* Contexte : A définir */
#  $$$ ------ Début de la partie corrigée ------
/* Fonction feuille : rien à changer sur la pile
    l     : registre a0, paramètre de type (struct cellule_t **)
    res   : registre t0, variable locale de type (struct cellule_t *)
    suiv  : registre t1, variable locale de type (struct cellule_t *)
*/
#  $$$ ------ Fin de la partie corrigée ------
inverse:
#  $$$ ------ Début de la partie corrigée ------
/*    res = NULL; */
    li   t0, 0
/*    while (*l != NULL) { */
while1:
    lw   t2, (a0)
    beqz t2, fin_while1
/*        suiv = (*l)->suiv; */
    lw   t2, (a0) /* *l dans t2 */
    lw   t1, 4(t2) /* (**l).suiv dans t1 suiv correspond à un décalage de 4 */
/*        (*l)->suiv = res; */
    lw   t2, (a0) /* *l dans t2 */
    sw   t0, 4(t2)
/*        res = *l; */
    lw   t0, (a0)
/*        *l = suiv; */
    sw   t1, (a0)
/*    } */
    j    while1
fin_while1:
/*    *l = res; */
    sw   t0, (a0)
/* } */
#  $$$ ------ Fin de la partie corrigée ------
    ret

/*
struct cellule_t *decoupe(struct cellule_t *l, struct cellule_t **l1, struct cellule_t **l2)
{
    struct cellule_t fictif1, fictif2;
    *l1 = &fictif1;
    *l2 = &fictif2;
    while (l != NULL) {
        if (l->val % 2 == 1) {
            (*l1)->suiv = l;
            *l1 = l;
        } else {
            (*l2)->suiv = l;
            *l2 = l;
        }
        l = l->suiv;
    }
    (*l1)->suiv = NULL;
    (*l2)->suiv = NULL;
    *l1 = fictif1.suiv;
    *l2 = fictif2.suiv;
    return l;
}
*/
    .globl decoupe
/* Contexte :
Fonction feuille : A priori pile inchangée, mais besoin de l'adresse des
variables locales => implantation des variables locales en pile.
Besoin de 2*2 mots de 32 bits dans la pile (PILE+16)
-> fictif1 à sp+0, fictif2 à sp+8
   (2 mots mémoire chacun : un pour le champ val, un pour le champ suiv)

  l             : registre a0, paramètre de type (struct cellule_t *)
  l1            : registre a1, paramètre de type (struct cellule_t **)
  l2            : registre a2, paramètre de type (struct cellule_t **)
  fictif2.suiv  : pile à sp+12 (champ de type cellule_t *)
  fictif2.val   : pile à sp+8  (champ de type int32_t)
  fictif1.suiv  : pile à sp+4  (champ de type cellule_t *)
  fictif1.val   : pile à sp+0  (champ de type int32_t)
*/
decoupe:
#   $$$ ------ Début de la partie corrigée ------
    addi sp, sp, -16
/*     *l1 = &fictif1; */
    sw   sp, (a1)
/*     *l2 = &fictif2; */
    addi t0, sp, 8
    sw   t0, (a2)
/*     while (l != NULL) {*/
while:
    beqz a0, fin
/*         if (l->val % 2 == 1) { */
    lw   t0, (a0)
    andi t0, t0, 1
    beqz t0, else
/*             (*l1)->suiv = l; */
    lw   t0, (a1) /* *l1 dans t0 */
    sw   a0, 4(t0)
/*             *l1 = l; */
    sw   a0, (a1)
/*         } else { */
    j    fin_if
else:
/*             (*l2)->suiv = l; */
    lw   t0, (a2) /* *l2 dans t0 */
    sw   a0, 4(t0)
/*             *l2 = l; */
    sw   a0, (a2)
/*         } */
fin_if:
/*         l = l->suiv; */
    lw   a0, 4(a0)
/*     } */
    j    while
fin:
/*     (*l1)->suiv = NULL; */
    lw   t0, (a1) /* *l1 dans t0 */
    sw   zero, 4(t0)
/*     (*l2)->suiv = NULL; */
    lw   t0, (a2)
    sw   zero, 4(t0)
/*     *l1 = fictif1.suiv; */
    lw   t0, 4(sp)
    sw   t0, (a1)
/*     *l2 = fictif2.suiv; */
    lw   t0, 12(sp)
    sw   t0, (a2)
/*     return l; */
    addi sp, sp, 16
#   $$$ ------ Fin de la partie corrigée ------
    ret
