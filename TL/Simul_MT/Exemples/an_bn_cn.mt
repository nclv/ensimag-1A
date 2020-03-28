// MT reconnaissant { a^n.b^n.c^n }

& a, b, c  // Sigma
           // Noter que 'X' n'est pas dans Sigma
           // donc il ne peut pas y en avoir initialement...
@ q0    // etat initial
$ f     // etat final

// "Invariant" global sur le ruban : a^m.X^r.b^s.c^t

q0 B : f  B S  // C'est fini, soit dès le début (\epsilon OK), soit à la fin
q0 a : qa B D  // effacer le 'a' et avancer

qa a : qa a D  // avancer le long des 'a'...
qa X : qa X D  // ... et des 'X' (les 'b' précédemment effacés)
qa b : qb X D  // ... jusqu'à trouver obligatoirement un 'b', remplacé par 'X'

qb b : qb b D  // avancer le long des 'b'...
qb c : qc c D  // ... jusqu'à trouver obligatoirement un 'c'

qc c : qc c D  // avancer le long des 'c'...
qc B : qF B G  // ... jusqu'à trouver un 'B' et reculer d'une case pour...
qF c : qR B G  // ... effacer le dernier 'c'

qR a : qR a G  // reculer tant qu'on a des 'a'...
qR b : qR b G  // ... des 'b'...
qR c : qR c G  // ... des 'c'...
qR X : qR X G  // ... et des 'X'...
qR B : q0 B D  // ... jusqu'au 'B' et on recommence

// A la fin, si on n'a plus de 'a', il faut aller au bout des 'X' pour vérifier
// qu'il n'y a plus rien derrière !
q0 X : q0 X D

// Note : au premier "parcours" vers la droite on vérifie implicitement
//        qu'on a un mot de la forme a^n.b^p.c^q avec n, p, q > 0

// *** Exercice :
// Cas d'arrêt non accepteurs (pas final mais pas de transition) possibles
// Donner les langages (sur { a, b, c }) qui peuvent mener à ces situations
//
// q0 b
// q0 c
// qa B
// qa c
// qb a
// qb B
// qc a
// qc b

// *** Exercice :
// Cas d'arrêt non accepteurs (pas final mais pas de transition) impossibles
// Expliquer pourquoi ils sont impossibles (i.e. pourquoi on ne peut pas
// atteindre de configuration dans l'état donné avec le symbole courant donné)
//
// qb X
// qc X
// qF a
// qF b
// qF X
// qF B
