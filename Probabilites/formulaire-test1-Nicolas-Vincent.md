---
title: "Formulaire de réponse pour le test 1"
author: VINCENT Nicolas
output: html_document
---

** **

##### Prénom Nom Groupe



##### Question 1

* Déterminer l'espérance du nombre de candidats réussissant l'examen.

###### Réponse :

On répète $n = 240$ épreuves de Bernoulli indépendants de même probabilité de succès $p = (1 - q)^{10}$ avec $q = 0.02$. C'est donc une loi Binomiale $B(n, p)$.

On en déduit que l'espérance du nombre de candidats réussissant l'examen est $np = 240(0.98)^{10} \simeq 196$.

** **

##### Question 2

* Calculer les probabilités P($N = i$), pour tout $i$ de 1 à 4.  

###### Réponse :

$$ \begin{aligned}\forall i \in \{1, ..., 4\}, \quad P(N = i) &= P(N_2 = i | N_1 \leq N_2) \\
&= \frac{P(N_2 = i , N_1 \leq N_2)}{P(N_1 \leq N_2))} \\
&= \frac{i}{10}
\end{aligned}
$$

** **

##### Question 3

* Calculer la probabilité de l'événement $G$ sachant que le candidat change de porte. Calculer la probabilité de l'événement $G$ sachant que le candidat conserve son choix initial.

###### Réponse :

Supposons que je choisisse la porte 3 – le raisonnement est identique dans les deux autres cas.
On note $T_1$ (resp. $T_2$ et $T_3$) la bonne porte est la porte 1 (resp. 2 et 3) et $O_1$ (resp. $O_2$ et $O_3$) le présentateur ouvre la porte 1 (resp. 2 et 3).
Soit C: "le joueur change de porte"

Supposons alors que l’animateur ouvre la porte 1 – le raisonnement est le même s’il ouvre la porte 2.
$$
\begin{aligned}
P(G | C) = P(T_2|O_1) &= \frac{P(O_1|T_2)P(T_2)}{P(O_1|T_1)P(T_1) + P(O_1|T_2)P(T_2) + P(O_1|T_3)P(T_3)}\\
&= \frac{1.\frac{1}{3}}{0.\frac{1}{3} + 1.\frac{1}{3} + \frac{1}{2}.\frac{1}{3}} \\
&= \frac{2}{3}
\end{aligned}
$$

** **

##### Question 4

* Le candidat opte a priori pour une stratégie aléatoire. Il change de porte avec la probabilité $p = 1/3$. Puis il joue et gagne le jeu. Quelle est la probabilité que le candidat ait changé de porte ?   

###### Réponse :

$$
\begin{aligned}
P(C|G) &= \frac{P(G|C)P(C)}{P(G)} \\
&= \frac{P(G|C)P(C)}{P(G|C)P(C) + P(G|\bar{C})P(\bar{C})} \\
&= \frac{\frac{2}{3}\frac{1}{3}}{\frac{2}{3}\frac{1}{3} + \frac{1}{3}\frac{2}{3}} \\
&= \frac{1}{2}
\end{aligned}
$$

** **

##### Question 5

* Calculer la valeur médiane de la variable $X$.  

###### Réponse :

La médiane de $X$ est la valeur $m$ telle que $P(X \leq m) = \frac{1}{2}$.
Or
$$
\begin{aligned}
P(X \leq m) &= \frac{1}{2}P(X \leq m | N = 1) + \frac{1}{3}P(X \leq m | N = 2) + \frac{1}{6}P(X \leq m | N = 3) \\
&= \frac{1}{2}P(U \leq m) + \frac{1}{3}P(2U \leq m) + \frac{1}{6}P(3U \leq m) \\
&= \frac{1}{2}m + \frac{1}{3}\frac{m}{2} + \frac{1}{6}\frac{m}{3} \\
\end{aligned}
$$
Ainsi $m = \frac{9}{13}$.

** **


##### Question 6

* Calculer la probabilité de l'événement $(Z_N > 1)$  

###### Réponse :

$$\begin{aligned}
\forall t > 0, \forall n \geq 1\quad
P(Z_n > t) &= P(min_{i \in \{1, ..., n\}} (X_i) > t) \\
&= P\bigg(\bigcap\limits_{i=1}^{n}(X_i > t)\bigg) \\
&= \prod_{i=1}^{n} P(X > t) \quad \text{par indépendance des $X_i$ de même loi $X$} \\
&= e^{-n\mu t}
\end{aligned}
$$
Par convention, on pose $Z_0=0$. Soit $N$ une variable de loi de Poisson de paramètre $λ=1$ indépendante des $(X_i)$.
$$\begin{aligned}
P(Z_N > 1) &= \sum_{k=1}^\infty P(Z_k > 1, N = k) \\
&= \sum_{k=1}^\infty P(Z_k > 1)P(N = k) \quad \text{car $N$ est indépendante des $(X_i)$}\\
&= \sum_{k=1}^\infty e^{-k\mu}\frac{e^{-1}1^k}{k!} \\
&= \frac{e^{e^{-\mu}} - 1}{e}
\end{aligned}
$$

** **


##### Question 7

* Déterminer la loi de la variable $Z$. Donner son espérance.


###### Réponse :

On note $E_i$ : "échec au $i^{ème}$ essai".
Ainsi
$$
\begin{aligned}
P(\text{"atteindre la cible au premier ou second tir"}) = 1 - P(E_1 \cap E_2) = 1 - P(E_1)P(E_2) = 1 - q^2 \quad \text{par indépendance.}
\end{aligned}
$$
Donc $Z \hookrightarrow B(n, 1 - q^2) = B(20, \frac{9}{10})$ et $E(Z) = n(1 - q^2) = 18$.
** **


##### Question 8

* Déterminer la loi de la variable $Y = Z - X$. Donner son espérance.

###### Réponse :

Y est le nombre de joueurs atteignant la cible uniquement au second tir.
$$
\begin{aligned}
P(\text{"atteindre la cible uniquement au second tir"}) = P(E_1 \cap S_2) = (E_1)P(S_2) = pq \quad \text{par indépendance.}
\end{aligned}
$$
Donc $Y \hookrightarrow B(n, pq) = B(20, \frac{2}{9})$ et $E(Y) = npq = \frac{40}{9}$.

On a $(Y | X = k) \hookrightarrow B(n - k, p)$ (nombre de réussites possible parmi n-k)
On en déduit la probabilité demandée.
$$ P(Y = l | X = k) = \binom{n - k}{l}p^l(1 - p)^{n - l}$$

$$ E(Y | X = k) = (n - k)p $$

** **


##### Question 9

* Donner une relation simple liant ${\rm E}[XY]$ à l'espérance d'une fonction simple de $X$ et la valeur de cette espérance (une ligne).

###### Réponse :

$$
\begin{aligned}
E[XY] &= \sum_{k=1}^n \sum_{l=1}^n k.lP(Y = l , X = k) \\
&= \sum_{k=1}^n kP(X = k) \sum_{l=1}^n lP(Y = l | X = k) \\
&= \sum_{k=1}^n kP(X = k) \sum_{l=1}^n l\binom{n - k}{l}p^l(1 - p)^{n - l} \\
&= \sum_{k=1}^n kP(X = k)E(Y | X = k) \\
&= \sum_{k=1}^n k\binom{n}{k}p^k(1-p)^{n-k}(n - k)p \\
&= n(n - 1)p^2q
\end{aligned}
$$

** **

##### Question 10

* Calculer la variance de la variable aléatoire $Z$. En déduire la covariance du couple $(X,Y)$ et retrouver le résultat précédent (une ligne).

###### Réponse :

$V(Z) = nq^2(1 - q^2)$ (loi Binomiale)

$$
\begin{aligned}
cov(X, Y) &= E(XY) - E(X)E(Y) = \frac{1}{2}(Var(Z) - Var(X) - Var(Y)) \\
&= \frac{1}{2}\bigg(nq^2(1 - q^2) - npq(1 - pq) - npq\bigg) \\
&= ... \\
&= -np²q \quad \text{plus X est grand plus Y risque d'être petit}
\end{aligned}
$$
On retrouve
$E(XY) = n(n-1)p²q$.

** **
