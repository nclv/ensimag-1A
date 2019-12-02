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
$$ N = \sum_{i=1}^{n}Y_i = \sum_{i=1}^{n}\mathbb{1}_{\max\limits_{i<m}^{} X_i \leq X_m}$$ puis par linéarité de l'espérance, $$E[N] = E[\sum_{i=1}^{n}Y_i] = \sum_{i=1}^{n}E[Y_i] = \sum_{i=1}^{n}\frac{1}{i} \simeq log(n) + \gamma $$
Ou on aurait pu simplement faire $$ E[N] = \sum_{i=1}^{n} P(\max\limits_{i<m}^{} X_i \leq X_m)$$, ce qui donne le même résultat.
Pour $n=27$,
$$E[N] = \frac{312536252003}{80313433200} \simeq 3.89$$

** **

##### Question 3

* Calculer ${\rm E}[Y_n]$.


###### Réponse :

** **

##### Question 4

* Calculer la valeur de la variance Var$[Y_3]$.

###### Réponse :

** **

##### Question 5

* Calculer Var$[Y_n]$ pour tout $n \geq 2$.

###### Réponse :

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
