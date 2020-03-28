// "plus 1" ; donnée codée en binaire.
// On autorise et on laisse des 0 en tête
// Algo : on va au bout (poids faible) puis on recule en "propageant"
// On termine en reculant pour être sur le début du résultat

& 0, 1

@ q0

$ f

q0 0 : qa 0 D      q0 1 : qa 1 D     // q0 B : bloqué (mot vide pas un entier)

qa 0 : qa 0 D      qa 1 : qa 1 D      qa B : qr B G

qr 1 : qr 0 G  // tant qu'on a des 1 on remplace par 0 (retenue propagée)
qr 0 : fr 1 G  // on a trouvé un 0 : remplacé par 1, "terminé"
qr B :  f 1 S  // il n'y avait que des 1 : on ajoute un 1 en tete

// en fr il faut encore reculer jusqu'au début
fr 0 : fr 0 G      fr 1 : fr 1 G      fr B : f B D
