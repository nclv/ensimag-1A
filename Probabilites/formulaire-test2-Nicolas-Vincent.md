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

$$\rm E[Y_n] = \sum_{i=1}^{n-1} \rm E[X_i] = \sum_{i=1}^{n-1} \rm E[\mathrm{1}_{(U_i < U_{i+1})}] = \sum_{i=1}^{n-1} P(U_i < U_{i+1}) = \frac{n-1}{2}$$

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

$$Var[Y_n] = (n - 1)\frac{1}{4} - 2(n-2)\frac{1}{12} = \frac{n+1}{12}$$

** **


##### Question 6

* Combien de tirages suffisent pour qu'avec une probabilité supérieure à 0.99, $A_{n-1}$ soit proche de la valeur 1/2 à $10^{-2}$ près.

###### Réponse :

On utilise l'inégalité de Bienaymé-Tchebychev. On cherche
$$
\begin{aligned}
P\left(\left|A_{n-1}-\frac{1}{2}\right |\geq 10^{-2} \right)\leq\frac {n+1}{12(n-1)^2(10^{-2})^2} \leq 0.01
\end{aligned}
$$
Soit $n \geq 83337$.

** **

##### Question 7

* Déterminer la valeur de $c$.

###### Réponse :

$$
\begin{aligned}
\int_{\mathbb{R}}\int_{\mathbb{R}}f(x, y)dxdy = \int_0^1\int_0^y cxy^2dxdy = 1 \implies c = 10
\end{aligned}
$$

** **


##### Question 8

* Déterminer la fonction de répartition de la variable $Y$. Donner sa valeur au point $t = 2/3$.

###### Réponse :

$$\forall y \in R, \quad f_Y(y) = \int_{x \in \mathrm{R}} f(x, y)dx = \int_{x=0}^{x=y} 10xy^2dx = 5y^4\mathrm{1}_{]0,1[}(y)$$ et $$F_Y(y) = F_{(X,Y)}(\infty, y) = \int_{-\infty}^y f_Y(t)dt  = 5\int_{-\infty}^y t^4\mathrm{1}_{]0,1[}(t)dt=
\left\{
    \begin{array}{ll}
        0 & \text{si } y \leq 0 \\
        y^5 & \text{si } 0 < y < 1 \\
        1 & \text{sinon.}
    \end{array}
\right.$$

$$F_Y\bigg(\frac{2}{3}\bigg) = \frac{32}{243}$$

** **

##### Question 9


* Ecrire un algorithme de simulation d'un couple de densité $f(x,y)$.

###### Réponse :

On cherchera à simuler tout d’abord $Y$ selon la loi marginale de densite $f_Y$. Ensuite, sachant $Y = y$, on cherchera à simuler la loi conditionnelle de densité $f^{Y = y}_X$.

$$\forall x \in R, \quad f^{Y = y}_X(x) = \frac{f(x,y)}{\int_{t \in \mathrm{R}} f(t, y)dt} = \frac{10xy^2\mathrm{1}_{D}(x,y)}{5y^4\mathrm{1}_{]0,1[}(y)} = \frac{2x}{y^2}\mathrm{1}_{]0, y[}(x)$$

Ce qui donne par la méthode d'inversion :
$Y := \bigg(\frac{ALEA}{5}\bigg)^{\frac{1}{4}}$
$X := Y\bigg(\frac{ALEA}{2}\bigg)^{\frac{1}{2}}$

** **

##### Question 10


* On pose $Z =  X Y$. Déterminer la densité de la loi de la variable $Z$.

###### Réponse :

Pour $ 0 < z < 1$, et $Y > 0$, la condition $XY \leq z$ équivant à $X \leq \frac{z}{Y}$.
$$P(XY \leq z) = \int_0^1 \int_0^{z/y}10xy^2dxdy = \int_0^1 5z^2 dy = 5z^2$$
Donc, $f_Z(z) = 10z$.
(le résultat est faux mais je n'ai pas trouvé mon erreur...)


** **
