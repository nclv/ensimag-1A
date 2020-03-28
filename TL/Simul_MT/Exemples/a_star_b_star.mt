// a*b* = { a^n b^p | n, p >= 0 }

& a, b // Sigma

@ q0   // etat initial

$ f    // etat final

q0 a : q0 a D  // avancer tant que 'a'
q0 B : f B S   // on a trouve blanc : fin du mot, OK
q0 b : q1 b D  // apres un 'b' : 'a' interdit

q1 b : q1 b D  // avancer tant que 'b'
q1 B : f B S   // terminer OK en fin de mot
