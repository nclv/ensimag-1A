// {wcw, w \in {a, b}*}

& a, b, c // Sigma

@ q0 // etat initial
$ f  // etat final

                 q0 c : qf c D
                 qf X : qf X D
                 qf B : f B S

q0 a : qa B D                 q0 b : qb B D
qa a : qa a D                 qb a : qb a D
qa b : qa b D                 qb b : qb b D
qa c : qac c D                qb c : qbc c D
qac X : qac X D               qbc X : qbc X D
qac a : q2 X G                qbc b : q2 X G

                 q2 a : q2 a G
                 q2 b : q2 b G
                 q2 c : q2 c G
                 q2 X : q2 X G
                 q2 B : q0 B D
