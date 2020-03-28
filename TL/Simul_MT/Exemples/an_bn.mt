// { a^n b^n | n >= 0 }

& a, b  // Sigma
@ q0    // etat initial
$ f     // etat final

q0 B : f  B S  // mot vide : fini OK
q0 a : q1 B D  // effacer le a et avancer
q1 a : q1 a D  // avancer...
q1 b : q2 b D  // ... jusqu'a avoir trouve un b
q2 b : q2 b D  // continuer jusqu'a...
q2 B : q3 B G  // ... avoir trouve un B puis reculer
q3 b : q4 B G  // effacer le b et reculer
q4 a : q4 a G  // ... jusqu'a...
q4 b : q4 b G  // ... trouver un...
q4 B : q0 B D  // ... B et on recommence
