---
title: "Formulaire de réponse pour le test 2"
output: pdf_document
---

** **

##### Nicolas VINCENT G4



##### Question 1

* Calculer la probabilité de battre un record à l'épreuve $m$

###### Réponse :

Soit $m \in [1, n]$. On note $R_m = \max\limits_{(i<m)}X_i$ représentant le record des $m$ premiers tirages et $F$ la fonction de répartition de la loi des $(X_i)$.
Soit $x \in \mathrm{R}$, alors $F_R = P(R \leq x) = P(\max\limits_{(i<m)}X_i \leq x) =P\bigg(\bigcap\limits_{i=1}^{m-1}(X_i \leq t)\bigg)$.
Or les variables $X_i$ sont indépendantes donc
$$
\begin{aligned}
F_R = \prod_{i=1}^{m-1} P(X_i \leq t) = F^{m-1}(x)
\end{aligned}
$$
La probabilité de battre un record à l'épreuve $m$ est la probabilité que l'épreuve $m$ soit un record.

Les variables étant à densité, la probabilité que 2 variables soient égales est nulle (les valeurs sont toutes différentes). La probabilité que le dernier soit le plus grand est donc $\frac{1}{m}$ car les $X_i$ sont indépendantes.

$$
\begin{aligned}
P(\max\limits_{i<m}^{} X_i \leq X_m) &= \int_0^{+\infty} P(\max\limits_{i<m}^{} X_i \leq X_m | X_m = x) f_{X_m}(x) dx \\
&= \int_0^{+\infty} P(\max\limits_{i<m}^{} X_i \leq x) dF(x) \\
&= \int_0^{+\infty} F^{m-1}(x) dF(x) \\
&= \frac{1}{m} \bigg[ F^m(x) \bigg] _{0}^{+\infty} = \frac{1}{m} \\
\end{aligned}
$$
** **

##### Question 2

* Donner l'espérance de $N$ pour $n = 27$.

###### Réponse :

Soit $N$ le nombre de records battus après $n$ épreuves.
On note $Y_n$ la variable de Bernoulli indiquant si $n$ est un record.
$$ N = \sum_{i=1}^{n}Y_i = \sum_{m=1}^{n}\mathbb{1}_{\max\limits_{i<m}^{} X_i \leq X_m}$$ puis par linéarité de l'espérance, $$\rm E[N] = \rm E[\sum_{i=1}^{n}Y_i] = \sum_{i=1}^{n}E[Y_i] = \sum_{i=1}^{n}\frac{1}{i} \simeq log(n) + \gamma $$
Ou on aurait pu simplement faire $$ \rm E[N] = \sum_{m=1}^{n} P(\max\limits_{i<m}^{} X_i \leq X_m)$$, ce qui donne le même résultat.
Pour $n=27$,
$$\rm E[N] = \frac{312536252003}{80313433200} \simeq 3.89$$

** **

##### Question 3

* Calculer ${\rm E}[Y_n]$.

###### Réponse :

$$
\begin{aligned}
P(U_1 < U_2) &= \int_{\mathrm{R}} P(U_1 < U_2 | U_2 = x) f_{U_2}(x) dx \\
&= \int_{\mathrm{R}} P(U_1 < x) \mathbb{1}_{[0, 1]}(x)dx \\
&= \int_{0}^{1} x dx \\
&= \bigg[ \frac{x^2}{2} \bigg] _{0}^{1} = \frac{1}{2} \\
\end{aligned}
$$

Les $U_i$ sont indépendantes. Les $X_i$ sont des variables de Bernoulli. Donc $Var[X_i] = pq$ et $\rm E[X_i] = P(X_i = 1)$.

$$
\begin{aligned}
P(U_1 < U_2 < U_3) &= \int_{\mathrm{R}} P(U_1 < x)(1 - P(U_3 < x)) \mathbb{1}_{[0, 1]}(x)dx \\
&= \int_{0}^{1} (x - x^2) dx \\
&= \frac{1}{2} - \frac{1}{3} = \frac{1}{6} \\
\end{aligned}
$$

$$\rm E[Y_n] = \sum_{i=1}^{n-1} \rm E[X_i] = \sum_{i=1}^{n-1} \rm E[\mathrm{1}_{(U_i < U_{i+1})}] = \sum_{i=1}^{n-1} P(U_i < U_{i+1}) = \frac{1}{2^n}$$

** **

##### Question 4

* Calculer la valeur de la variance Var$[Y_3]$.

###### Réponse :

$$
\begin{aligned}
Var[X_1] &= \rm E[X_1^2] - (\rm E[X_1])^2 \\
&= P(U_1 < U_2)(1 - P(U_1 < U_2)) \\
&= \frac{1}{4}
\end{aligned}
$$
$Z = X_1X_2$ est une variable de Bernoulli.
$$
\begin{aligned}
Cov[X_1, X_2] &= \rm E[X_1X_2] - \rm E[X_1]\rm E[X_2] \\
&= P(X_1X_2 = 1) - P(U_1 < U_2)P(U_2 < U_3) \\
&= P(U_1 < U_2 < U_3) - \frac{1}{4} \\
&= -\frac{1}{12}
\end{aligned}
$$

$$Var[Y_3] = Var[X_1] + Var[X_2] = \frac{1}{2} $$

** **

##### Question 5

* Calculer Var$[Y_n]$ pour tout $n \geq 2$.

###### Réponse :

Soit $n \geq 2$. Les $X_i$ ne sont pas indépendantes donc
$${\rm Var}[Y_n]  = \sum_{i = 1}^{n-1} {\rm Var}[X_i] + 2 \sum_{i = 1}^{n-2} {\rm Cov}[X_i, X_{i+1}]$$

En effet, $$V(X+Y)=Cov(X+Y, X+Y)=Cov(X,X)+Cov(Y,Y)+2Cov(X,Y)=V(X)+V(Y)+2Cov(X,Y)$$ puis on obtient le résultat par combinaison linéaire.

$$Var[Y_n] = n\frac{1}{4} - 2(n-1)\frac{1}{12} = \frac{n+2}{12}$$ 

** **


##### Question 6

* Combien de tirages suffisent pour qu'avec une probabilité supérieure à 0.99, $A_{n-1}$ soit proche de la valeur 1/2 à $10^{-2}$ près.

###### Réponse :

** **


##### Question 7

* Déterminer la valeur de $c$.



###### Réponse :

** **


##### Question 8

* Déterminer la fonction de répartition de la variable $Y$. Donner sa valeur au point $t = 2/3$.

###### Réponse :

** **


##### Question 9


* Ecrire un algorithme de simulation d'un couple de densité $f(x,y)$.

###### Réponse :

** **

##### Question 10


* On pose $Z =  X Y$. Déterminer la densité de la loi de la variable $Z$.

###### Réponse :


** **
