// {ww, w \in {a, b}*}

& a, b // sigma
@ q0   // etat initial
$ f    // etat final

                     q0 B : f B S // mot vide : OK et fini


q0 a : q1 X D                             q0 b : q1 Y D
             q1 a : q1 a D    q1 b : q1 b D

             q1 Z : q2 Z G    q1 T : q2 T G   q1 B : q2 B G         

q2 a : q3 Z G                             q2 b : q3 T G
             q3 a : q3 a G  q3 b : q3 b G

    q3 X : q0 X D     q3 Y : q0 Y D

// ici on est en XYY[q0]ZTT par exemple, on recule au debut

q0 Z : q4 Z G    q0 T : q4 T G
q4 X : q4 X G    q4 Y : q4 Y G
q4 B : q5 B D

// ici on est en [q5]XYYZTT p.ex., en tous cas autant (>0) de X|Y que de Z|T
// du coup on fait un peu comme pour wcw ('# pour 'cocher' la partie droite)

q5 X : qZ B D                   q5 Y : qT B D
qZ X : qZ X D                   qT X : qT X D
qZ Y : qZ Y D                   qT Y : qT Y D
qZ # : qZ # D                   qT # : qT # D
qZ Z : q6 # G                   qT T : q6 # G

q6 # : q6 # G     q6 X : q6 X G     q6 Y : q6 Y G
                  q6 B : q5 B D

// Il reste a verifier qu'on n'a que plus que des #
q5 # : q5 # D
q5 B : g B G

// On peut remarquer qu'a la fin le ruban contient |w| (en unaire avec #)
// Ici on revient au debut

g # : g # G
g B : f B D
