    .text
/*
bool est_present(uint32_t val, struct noeud_t *abr)
{
   if (abr == NULL) {
       return false;
   } else if (val == abr->val) {
       return true;
   } else if (val < abr->val) {
       return est_present(val, abr->fg);
   } else {
       return est_present(val, abr->fd);
   }
}

*/
    .globl est_present
est_present:
/* Contexte : à définir */
#   $$$ ------ Début de la partie corrigée ------
/* Contexte :
fonction non feuille :
  * pas de variable locale
  * les arguments sont utilisés avant les appels de fonctions, jamais après,
    inutile donc de les sauvegarder
  * besoin de sauvegarder ra

    adresse de retour  : pile à sp+0 (registre ra initialement)
 */
    addi sp, sp, -4      # place pour l'adresse de retour
    sw   ra, 0(sp)       # stocke adresse de retour
/* Il n'est pas nécessaire de sauvegarder les arguments, car la fonction termine
 * aussitôt après l'appel sans les réutiliser */

/*
   if (abr == NULL) {
*/
    beqz a1, ep_faux     # arbre vide si abr==0
/*
   } else if (val == abr->val) {
*/
    lw   t0, 0(a1)       # abr->val : 1er champ de la structure
                         # donc à adresse de la structure + 0
    beq  a0, t0, ep_vrai # test valeur trouvée
/*
   } else if (val < abr->val) {
*/
    lw   t0, 0(a1)       # abr->val : 1er champ de la structure
    slt  t1, a0, t0      # val < abr->val dans v1
    beqz t1, ep_plus_gd  # test v1==0

ep_plus_pt:              # donc val est plus petit
/*
       return est_present(val, abr->fg);
*/
    mv   a0, a0          # trad systématique:
                         # chargement du premier argument dans a0
    lw   a1, 4(a1)       # 2ème argument dans a1
                         # récupère abr->fg : 2eme elt de la structure
    jal  est_present     # appel récursif
    j    ep_retour       # retour d'appel récursif : a0 contient le résultat

ep_plus_gd:
/*
   else {
       return est_present(val, abr->fd);
*/
    mv    a0, a0         # trad systématique:
                         # chargement du premier argument dans a0
    lw    a1, 8(a1)      # 2ème argument dans a1
                         # récupère abr->fd : 3eme elt de la structure
    jal   est_present    # appel récursif
    j     ep_retour      # retour d'appel récursif : a0 contient le résultat
ep_vrai:
/*
       return true;
*/
    li    a0, 1          # valeur de retour vrai
    j     ep_retour      # saut à la fin de la fonction

ep_faux:
/*
       return false;
*/
    li    a0, 0          # valeur de retour faux

ep_retour:
    lw   ra, 0(sp)       # récupère l'adresse de retour
    addi sp, sp,  4      # symétrique au prologue
#   $$$ ------ Fin de la partie corrigée ------
    ret

/*
void abr_vers_tab(struct noeud_t *abr)
{
    if (abr != NULL) {
        abr_vers_tab(abr->fg);
        *ptr = abr->val;
        ptr++;
        struct noeud_t *fd = abr->fd;
        free(abr);
        abr_vers_tab(fd);
    }
}
*/
    .globl abr_vers_tab
abr_vers_tab:
/* Contexte :
#   $$$ ------ Début de la partie corrigée ------
  * fonction non feuille :
  * 1 variable locale devant être stockée en pile (fd),
  * besoin de sauver a0, pouvant (étant en fait) modifié par l'appel
  * besoin de sauvegarder ra
  => réservation de 3 mots sur la pile

    ra   : pile à sp+8
    fd   : pile à sp+4
    abr  : pile à sp+0 (registre a0 initialement)

#   $$$ ------ Fin de la partie corrigée ------
 */
#   $$$ ------ Début de la partie corrigée ------
    addi sp, sp, -3*4    # adresse de retour + 1 argument + 1 registre
    sw   ra, 2*4(sp)     # stocke adresse de retour
/*
    if (abr != NULL) {
*/
    beqz a0, avt_retour   # test arbre vide
/*
        abr_vers_tab(abr->fg);
*/
    sw   a0, 0*4(sp)     # sauve le pointeur de nœud courant dans la pile
    lw   a0, 1*4(a0)    # récupère abr->fg, 2ème champ, comme argument
    jal  abr_vers_tab     # et appelle la fonction récursivement
    lw   a0, 0*4(sp)     # récupération du pointeur de nœud courant
/*
        *ptr = abr->val;
*/
    lw   t0, ptr          # charge le contenu de la variable globale ptr
    lw   t1, 0(a0)       # charge la valeur associée au nœud (abr->val)
    sw   t1, 0(t0)       # *ptr prend la valeur
/*
        ptr++;
*/
    lw   t0, ptr          # charge le contenu de la variable globale ptr
    addi t0, t0, 4       # incrémente (4!) l'adresse contenue dans t0
    sw   t0, ptr, t1          #  et modifie ptr
/*
        struct noeud_t *fd = abr->fd;
*/
    lw   t0, 2*4(a0)     # récupère abr->fd, 3ème champ
    sw   t0, 1*4(sp)     # et l'enregistre dans l'emplacement
                            # pour fd prévu dans la pile
                            # pas dans registre car appel de free
                            # avant son utilisation
/*
        free(abr);
*/
    mv   a0, a0          # trad sytématique : argument de free
    jal  free              # a0 pointe sur le nœud courant
/*
        abr_vers_tab(fd);
*/
    lw    a0, 1*4(sp)     # récupère fd comme argument
    jal   abr_vers_tab      # et appelle la fonction récursivement
                            # sauvegarde du noeud courant non nécessaire
                            # car plus d'utilisation avant la fin du programme
avt_retour:
    lw   ra, 2*4(sp)     # récupère l'adresse de retour
    addi sp, sp,  3*4    # symétrique au prologue
#   $$$ ------ Fin de la partie corrigée ------
    ret

#   $$$ ------ Début de la partie corrigée ------
    .data
    .globl ptr
# uint32_t *ptr;
.lcomm ptr, 4
#   $$$ ------ Fin de la partie corrigée ------
