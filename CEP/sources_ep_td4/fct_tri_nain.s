/*
void tri_nain(int32_t tab[], uint32_t taille)
{
    uint32_t i = 0;
    while(i < taille - 1) {
        if (tab[i] > tab[i+1]) {
            int32_t tmp = tab[i];
            tab[i] = tab[i+1];
            tab[i + 1] = tmp;
            if (i > 0) {
                i = i - 1;
            }
        } else {
            i = i + 1;
        }
    }
}
*/
    .text
/*  void tri_nain(int32_t tab[], uint32_t taille) */
    .globl tri_nain
tri_nain:
/* Contexte : à définir */
#   $$$ ------ Début de la partie corrigée ------
/* Fonction feuille : pas de modification de pile
    tab     : registre a0 (int32_t *)
    taille  : registre a1 (uint32_t)
    i       : registre t0 (uint32_t)
    tmp     : registre t1 (int32_t)
*/
/*  i = 0; */
    mv   t0, zero
/*  while(i < taille - 1) { */
while:
    addi t2, a1, -1
    sltu t2, t0, t2
    beqz t2, fin_while
/*    if (tab[i] > tab[i+1]) { */
    slli t2, t0, 2
    add  t2, a0, t2
    lw   t3, 0(t2) /* tab[i] */
    lw   t4, 4(t2) /* tab[i+1] */
    slt  t5, t4,t3
    beqz t5, else
/*      tmp = tab[i]; */
    slli t2, t0, 2
    add  t2, a0, t2
    lw   t1, 0(t2)
/*      tab[i] = tab[i+1]; */
    slli t2, t0, 2
    add  t2, a0, t2
    lw   t3, 4(t2)
    sw   t3, 0(t2)
/*      tab[i + 1] = tmp; */
    slli  t2, t0, 2
    add  t2, a0, t2
    sw   t1, 4(t2)
/*      if (i > 0)*/
    blez t0, fin_if2
/*        i = i - 1; */
    addi t0, t0, -1
/*      } */
fin_if2:
    j    fin_if1
/*    } else { */
else:
/*      i = i + 1; */
    addi t0, t0, 1
/*    } */
fin_if1:
    j    while
fin_while:
#   $$$ ------ Fin de la partie corrigée ------
    ret

    .text
    .globl tri_nain_opt
/* Version du tri optimisée sans respecter la contrainte de la traduction
 * systématique */
tri_nain_opt:
/* Contexte :
complétez le contexte précédent en indiquant les registres qui contiendront des
variables temporaires. */
#   $$$ ------ Début de la partie corrigée ------
/*
    tab[i] ou tmp  : registre t1
    taille - 1     : registre t2
    &tab[i]        : registre t3
    tab[i+1]       : registre t4
*/
    mv   t0, zero
    addi t2, a1, -1
/*  while(i < taille - 1) */
while_opt:
    sltu t5, t0, t2
    beqz t5, fin_while_opt
/*    if (tab[i] > tab[i+1]) */
    slli t5, t0, 2
    add  t3, a0, t5
    lw   t1, 0(t3)
    lw   t4, 4(t3)
    slt  t5,t4,t1
    beqz t5, else_opt
/*      tmp = tab[i]; */
/*      tab[i] = tab[i+1]; */
    sw   t4, 0(t3)
/*      tab[i + 1] = tmp; */
    sw   t1, 4(t3)
/*      if (i > 0) { */
    blez t0, while_opt
/*        i = i - 1; */
    addi t0, t0, -1
    j    while_opt
else_opt:
/*      i = i + 1; */
    addi t0, t0, 1
    j    while_opt
fin_while_opt:
#   $$$ ------ Fin de la partie corrigée ------
    ret

    .text
    .globl tri_nain_superopt
/* Version encore plus optimisée sans rien respecter
   (tout se perd ma bonne dame !).

Optimisations effectuées:
  - A compléter
#   $$$ ------ Début de la partie corrigée ------
  - Factoriser les sauts à la suite (fin_if1 et fin_if2 disparaissent)
  - Se passer de i et ne garder que tab+4*i en modifiant les tests
            i < taille - 1  <=>  tab+4*i < tab + 4*(taille - 1)
            i > 0           <=>  tab + (4*i) > tab
    et en faisant les incréments/décréments de i sur tab+4*i (par pas de 4)
  - Comme le nain ne se déplace que d'une case à la fois, à chaque passage dans
    la boucle, une seule valeur doit être lue en mémoire, l'autre l'ayant été à
    l'itération précédente.

Pour tirer partie de cette dernière remarque, on peut vouloir mettre à jour
les registres contenant tab[i] et tab[i+1] au moment où l'on modifie la valeur
de i. Cependant, ce faisant on effectue les lectures avant le test i < taille-1
donc on peut lire une case de trop (en l'occurrence tab[taille]).
Pour éviter cela, on peut
1) Faire une rotation de boucle pour mettre les lectures en fin de boucle,
   donc mettre la comparaison tab[i] > tab[i+1] en début de boucle, sans oublier
   de remettre hors de la boucle la partie manquante de la première itération :
            while:                            A;
            A;          est équivalent à      while:
            B;                                B;
            j while                           A;
                                              j while
   où A et B sont des blocs d'instructions arbitraires.
2) Faire remonter le test i < taille - 1 et les lectures mémoire dans les
   branches où l'on modifie i.
3) Remplacer l'une des deux lectures mémoire par un mv.

D'autres optimisations deviennent possibles après avoir transformé ainsi notre
programme :
  - Inutile de tester i < taille - 1 si on vient de faire i = i - 1.
  - Dans le cas d'un échange de tab[i] et tab[i+1], pour maintenir le contexte,
    il faudrait échanger t1 et t4. Mais à cause du i = i - 1 qui suit,
    on doit aussi faire mv t4, t1. Au final rien ne change pour t4. De plus,
    comme on charge t1 depuis la mémoire juste parès, inutile de le faire pour
    t1 non plus !

Au final, notez que l'on a ici accéléré notre programme au prix d'un nombre
d'instructions plus grand.
#   $$$ ------ Fin de la partie corrigée ------
*/
tri_nain_superopt:
/* Contexte :
complétez le contexte précédent en indiquant les registres qui contiendront des
variables temporaires.  */
#   $$$ ------ Début de la partie corrigée ------
/*
    tab+i             : registre t0
    tab[i] ou tmp     : registre t1
    tab + taille - 1  : registre t2
    tab[i+1]          : registre t4
*/
    mv   t0, a0 /* calcul de tab + 4*i */
    addi t2, a1, -1 /* calcul de tab + 4*(taille - 1) */
    slli t5, t2, 2
    add  t2, a0, t5
    /* si taille <= 1 (c.-à-d. tab + 4*(taille - 1)) < tab + 4*i, on termine */
    sltu t5, t0, t2 
    beqz t5, fin_while_superopt
	/* sinon, on établit le contexte */
    lw   t1, 0(t0)
    lw   t4, 4(t0)
while_superopt:
/*    if (tab[i] > tab[i+1]) { */
    slt  t5,t4,t1
    beqz t5, else_superopt
    /* échange de tab[i] et de tab[i+1] en mémoire */
    sw   t4, 0(t0)
    sw   t1, 4(t0)
/*      if (i > 0) { */
    beq  t0, a0, swap_superopt /* i = 0, mais pour retablir le contexte, */
                               /*        il faut encore échanger t1 et t4 */
/*        i = i - 1; */
    addi t0, t0, -4
    /* pas besoin de tester i < taille - 1, c'est vrai */
	/* pas besoin de faire mv t4, t1 car on ne les a pas encore échangés */
    lw   t1, 0(t0)
    j    while_superopt
else_superopt:
/*      i = i + 1; */
    addi t0, t0, 4
/*    while(i < taille - 1) { */
    sltu t5, t0, t2
    beqz t5, fin_while_superopt
    mv   t1, t4
    lw   t4, 4(t0)
    j    while_superopt
swap_superopt: /* échange de t1 et t4 (tab[i] et tab[i+1]) sans 3e registre */
	xor  t1, t1, t4
	xor  t4, t1, t4
	xor  t1, t1, t4
    j    while_superopt
fin_while_superopt:
#   $$$ ------ Fin de la partie corrigée ------
    ret
