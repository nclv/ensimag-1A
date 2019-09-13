---
title: "Formulaire de réponse pour le test 0 -- TD-1"
author: VINCENT Nicolas
output: pdf_document
---

** **


#### Problème 1



##### Question 1

* Déterminer la probabilité de l'événement $(N_E > k)$, pour tout $k \geq 1$. Quelle est la loi de $N_E$ ?

###### Réponse :

$\qquad$On s'intéresse au premier succès dans une suite d'épreuves de Bernoulli de même paramètre $p = \frac{1}{6}$.
L'évènement $(N_E > k)$ équivaut à dire que chacune des $k$ premières épreuves est un échec. Ainsi:
$$ \forall k \in \mathrm{N}, \quad P(N_E > k)= (1-p)^k = \bigg(\frac {5}{6}\bigg)^k$$

> On peut démontrer directement ce résulat par le calcul ou bien raisonner avec le complémentaire.

$\qquad$On aura reconnu une **loi géométrique** de paramètre $\frac{1}{6}$.

##### Question 2

* Calculer la probabilité de l'événement $(N > k)$, pour tout $k \geq 1$. Quelle est la loi de $N$ ?

###### Réponse :

On constate que $N = min(N_E, N_R)$ en adaptant les notations d'Eva à Ralph, où les variables aléatoire $N_E$ et $N_R$ suivent respectivement deux lois géométriques de paramètre $p=\frac{1}{6}$ et $q=\frac{1}{7}$. Ainsi:
$$\forall k \in \mathrm{N}^* , \quad (N > k) = (N_E > k) \cap(N_R > k)$$
On a donc par indépendance des lancers:

$$  P(N > k) = P(N_E > k)P(N_R > k) = (1-p)^k(1-q)^k = \bigg(\frac{5}{7}\bigg)^k $$

et la variable aléatoire $N$ suit une **loi géométrique** de paramètre $1 - (1-p)(1-q) = \frac{2}{7}$.

##### Question 3

* Quelle est la probabilité pour que Eva gagne ?

###### Réponse :

L'évènement "Eva gagne" s'écrit $(N_E < N_R)$.

$$ \begin{align}P(N_E < N_R) &= P\bigg(\bigcup\limits_{n=1}^{\infty}(N_E = n, N_R > n)\bigg) \\
&= \sum_{n=1}^\infty P(N_E = n, N_R > n) \\
&= \sum_{n=1}^\infty P(N_E = n)P(N_R > n) \\
&= \sum_{n=1}^\infty p(1-p)^{n-1}(1-q)^n \\
&= \frac{p}{1-p}\sum_{n=1}^\infty ((1-p)(1-q))^n \\
&= \frac{p(1-q)}{1-(1-p)(1-q)} \\
&= \frac{1}{2} \\
\end{align}$$

##### Question 4

* Quelle est la probabilité de match nul ?


###### Réponse :

Il y a match nul lorsque $N_E = N_R$
$$ \begin{align}P(N_E = N_R) &= P\bigg(\bigcup\limits_{n=1}^{\infty}(N_E = n, N_R = n)\bigg) \\
&= \sum_{n=1}^\infty P(N_E = n, N_R = n) \\
&= \sum_{n=1}^\infty P(N_E = n)P(N_R = n) \\
&= \sum_{n=1}^\infty p(1-p)^{n-1}q(1-q)^{n-1} \\
&= pq\sum_{n=0}^\infty ((1-p)(1-q))^n \\
&= \frac{pq}{1-(1-p)(1-q)} \\
&= \frac{1}{12} \\
\end{align}$$

##### Question 5

* Calculer la probabilité que la partie a duré moins de 3 manches sachant qu'Eva a gagné.


###### Réponse :

On utilise la définition d'une probabilité conditionnelle:
$$ \begin{align}
P(N<3|N_E<N_R) &= \frac{P((N<3)\cap(N_E<N_R))}{P(N_E<N_R)} \\
&= \frac{P((N_E<3)\cap(N_R<3)\cap(N_E<N_R))}{P(N_E<N_R)} \\
&= \frac{P((N_E=1)\cap(N_R<2)}{P(N_E<N_R)} \\
&= \frac{1}{14}
\end{align}
$$

** **

#### Problème 2



##### Question 1

*  Calculer la probabilité que la variable aléatoire $W$ soit inférieure ou égale à $1/3$.

###### Réponse :

$$\begin{align}
P\bigg(W\leqslant\frac{1}{3}\bigg) &= P\bigg(W\leqslant\frac{1}{3}|U<\frac{1}{4}\bigg)P\bigg(U<\frac{1}{4}\bigg)+P\bigg(W\leqslant\frac{1}{3}|U\geqslant\frac{1}{4}\bigg)(1-P\bigg(U<\frac{1}{4}\bigg)) \\
&=P\bigg(V\leqslant\frac{1}{3}\bigg)P\bigg(U<\frac{1}{4}\bigg)+P\bigg(V\leqslant\frac{1}{9}\bigg)(1-P\bigg(U<\frac{1}{4}\bigg)) \\
&= \frac{1}{3}\frac{1}{4} + \frac{1}{9}\bigg(1 - \frac{1}{4}\bigg) \\
&= \frac{1}{6}

\end{align}
$$

##### Question 2

*  Calculer l'espérance de la variable aléatoire $W^2$.

###### Réponse :

Nous allons utiliser le théorème de transfert et la linéarité de l'intégrale.

$$
\begin{align}
E(W^2) &= \int_{0}^{1}t^2P(W=t)dt \\
&= \frac{1}{4}\int_{0}^{1}t^2P(V=t)dt + \frac{3}{4}\int_{0}^{1}t^2P(V=t^2)dt \\
&= \frac{1}{4}\int_{0}^{1}t^3dt + \frac{3}{4}\int_{0}^{1}t^4dt \\
&= \frac{1}{16} + \frac{3}{20} \\
&= \frac{17}{80}

\end{align}
$$


** **

#### Problème 3


##### Question 1

*  Calculer l'espérance de la variable aléatoire $Z$.

###### Réponse :

La linéarité de l'espérance nous permet d'écrire:
$$ E(Z) = E(X) + E(Y)$$

On connaît l'espérance de la loi $X$, uniforme sur l'intervalle $[0, 1]$ $(\frac{1+0}{2} = \frac{1}{2})$. Pour calculer celle de $Y$, il faut utiliser un théorème de calcul d'espérance par conditionnement.

$$ \begin{align}
E(Y) &= \sum_{n \in \mathrm{N}} E(Y|X = n)P(X = n) \\
&= \int_{\mathrm{R}} E(Y|X = x)f_X(x)dx \\
&= \int_{0}^{1} E(Y|X = x)dx \\
&= \int_{0}^{1} \frac{x}{2}dx \\
&= \frac{1}{4}
\end{align}
$$

Ainsi:
$$ E(Z) = \frac{3}{4}$$
