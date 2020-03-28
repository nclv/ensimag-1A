// "moins" unaire :
// (1) 0 M y = 0
// (2) x+1 M 0 = x+1
// (3) x+1 M y+1 = x M y

& 1, M  // Sigma ; entree sous la forme 1*M1* : xMy

@ q0    // etat initial

$ f     // un seul etat final

q0 M : f1 B D  // (1)
f1 1 : f1 B D
f1 B : f B S   // il n'y a plus que des B -> 0

q0 1 : q1 1 D  // (2) ou (3) on effacera ce 1 au retour si (3)
q1 1 : q1 1 D
q1 M : q2 M D

q2 B : f2 B G  // (2), il faut effacer le M (puis revenir au debut)
f2 M : f2 B G  // on est sur de commencer par celui-ci et de ne plus l'avoir
f2 1 : f2 1 G
f2 B : f B D

q2 1 : q3 1 D  // (3)
q3 1 : q3 1 D
q3 B : q4 B G
q4 1 : q5 B G  // on efface 1 en fin de y
q5 1 : q5 1 G
q5 M : q6 M G
q6 1 : q6 1 G
q6 B : q7 B D
q7 1 : q0 B D  // on efface le premier 1 de x, et on recommence
