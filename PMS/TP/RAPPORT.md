# Partie 1

Une variable aléatoire $X$ est de loi ${U}_{\{1,\ldots,\theta\}}$ si elle est à valeurs dans $\{1, \ldots, \theta\}$ et que 
$$P(X=k) = \frac{1}{\theta} \, \mathbb{1}_{\{1, \ldots, \theta\}}(k).$$

## 1. Calculer l'espérance et la variance de $X$. 

Les deux résultats sont connus. Calculons la fonction génératrice des moments de $X$.

$$M_X(t) = E[e^{tX}] = \int e^{tx}\frac{1}{\theta} \, \mathbb{1}_{\{1, \ldots, \theta\}}(x)dx = \frac{1}{\theta}\int_1^\theta e^{tx}dx = \frac{1}{\theta}\bigg[\frac{1}{t}e^{tx}\bigg]_{x=1}^\theta = \frac{e^{t} - e^{\theta t}}{t(1 - \theta)}$$

On a alors $E[X] = M_X'(0) = \frac{1 + \theta}{2}$ et $Var(X) = E[X^2] - E[X]^2 = M_X''(0) - [M_X'(0)]^2 = \frac{(\theta - 1)^2}{12}$.

## 2. Calculer l'estimateur des moments $\tilde{\theta}_n$ de $\theta$. Montrer que cet estimateur est sans biais et calculer sa variance.

Pour tout $\theta$, $E_{\theta}[X_1] = \frac{1 + \theta}{2}$. On peut donc prendre par exemple $\Phi(\theta) = \frac{1 + \theta}{2}$ (application bien injective) et $f = Id : \mathbb{R} \rightarrow \mathbb{R}$. L'estimateur obtenu par la méthode des moments est alors $\tilde{\theta}_n = 2\overline{X}_n - 1$.

Cet estimateur est sans biais et consistant.
En effet, pour tout $\theta \in \mathbb{R}$, $E[\tilde{\theta}_n] = 2E[\overline{X}_n] - 1 = 2\frac{\theta + 1}{2} - 1= \theta$ et l'application $x \rightarrow 2x - 1$ est continue.

$$Var(\tilde{\theta}_n) = 4Var(\overline{X}_n) = \frac{4n}{n^2}Var(X_1) = \frac{4}{n}\frac{(\theta - 1)^2}{12} = \frac{(\theta - 1)^2}{3n}$$

## 3. Calculer la fonction de répartition de $X$. Calculer la médiane de la loi de $X$ et en déduire un estimateur $\tilde{\theta}'_n$ de $\theta$ basé sur la médiane empirique.

La densité $f$ de $X$ vérifie $f(x) = \frac{1}{\theta - 1}$ si $1 \leq x \leq \theta$ et $0$ sinon. La fonction de répartition $F$ de $X$ vérifie donc $F(x) = \frac{x - 1}{\theta - 1}$ si $1 \leq x \leq \theta$, $0$ si $x < 1$ et $1$ si $x > \theta$.

Notons $q_{\frac{1}{2}}$ la médiane de $X$. Elle vérifie $F(q_{\frac{1}{2}}) = \frac{1}{2}$. On a trivialement $q_{\frac{1}{2}} = \frac{1 + \theta}{2}$.

On rappelle l'expression de la médiane empirique : $\tilde{Q}_{n,\frac{1}{2}} = \frac{X_{\frac{n}{2}}^* + X_{\frac{n}{2} + 1}^*}{2}$ si $\frac{n}{2}$ est entier et $X_{\left\lfloor\frac{n}{2}\right\rfloor + 1}^*$ sinon.

On considère donc $\tilde{\theta}'_n = 2\tilde{Q}_{n,\frac{1}{2}} - 1$ basé sur la médiane empirique. Il est sans biais et consistant.

---

> On peut noter ici que les calculs de la fonction de répartition et de la médiane sont inutiles.
Nous sommes dans le cas d'une distribution symétrique (en effet, $f(x - \mu) = f(\mu - x)$). Ainsi qu'on prenne la moyenne ou la médiane comme estimateur, on estimera la même quantité car les deux paramètres sont identiques.

> Est-ce qu’on devrait utiliserla moyenne ou la médiane de l’échantillon pour estimer notre paramètre de position $\theta$ ? Lorsque plusieurs estimateurs estiment la même quantité et que leur biais est négligeable ou nul, le choix se fait généralement sur la base de la variance de l’estimateur, une mesure de précision : on va préférer un estimateur qui a une plus petite variance puisque ça veut dire qu’en moyenne la distance (au carré) entre l’estimateur et le paramètre est moindre. Celle-ci dépend toutefois de la distribution de laquelle proviennent les données - qui en pratique nous reste inconnue.

## 4. Soit $X_n^*$ le maximum des observations. Calculer la fonction de répartition de $X_n^*$ et les probabilités élémentaires $P(X_n^*=k)$, $\forall k \in \{1, \ldots, \theta\}$.

$P(X_n^* \leq k) = \big(\frac{k}{\theta}\big)^n$ par indépendance des observations.

L'évènement $(X_n^* = k)$ est le complémentaire de $(X_n^* < k) \cup (X_n^* > k)$.

Ainsi $P(X_n^* = k) = 1 - \big(\big(\frac{k - 1}{\theta}\big)^n + \big(1 - \big(\frac{k}{\theta}\big)^n\big)\big) = \big(\frac{k}{\theta}\big)^n - \big(\frac{k - 1}{\theta}\big)^n$

## 5. Montrer que l'estimateur de maximum de vraisemblance de $\theta$ est $\hat{\theta}_n=X_n^*$. Montrer qu'il est biaisé mais qu'on ne peut pas le débiaiser facilement.

La fonction de masse de notre problème est $p_\theta(x) = \frac{1}{\theta}$ si $x \leq \theta$ et $0$ sinon.

Ainsi, l'estimateur du maximum de vraisemblance pour un échantillon de $n$ tanks issus d'un échantillon aléatoire indépendant vaut :

$$
L(\theta, x_1, \ldots, x_n) = \left\{
    \begin{array}{ll}
        \frac{1}{\theta^n} & \text{si } max_i (x_i) \leq \theta \\
        0 & \text{sinon.}
    \end{array}
\right.
$$

Cette fonction est maximisée pour $\hat{\theta}_n = max_i (x_i) = X_n^*$.

---
Si $n = 1$ et que le tank à le numéro de série $x$ alors $x$ est l'estimation du maximum de vraisemblance du nombre total de tanks.

On note ici que le support, représenté par les valeurs de $x$ donnant une fonction de masse positive, dépend de $\theta$. Pour le calcul de la borne de Cramér-Rao on suppose que le support n'en dépend pas.

---

$$E_{\theta}[\hat{\theta}_n] = \sum_{k=1}^{\theta} k\bigg(\bigg(\frac{k}{\theta}\bigg)^n - \bigg(\frac{k - 1}{\theta}\bigg)^n\bigg)$$

Sans prendre la peine de finir le calcul, on voit que l'on obtiendra pas $\theta$. En effet, prenons une seule observation, alors $n = 1$ et $E_{\theta}[\hat{\theta}_n] = \frac{\theta + 1}{2}$ ce qui donne un biais de $\frac{1 - \theta}{2}$.

Cependant, l'estimateur est consistant. $P(X_n^* = k) \rightarrow 0$ lorsque $n \rightarrow \infty$ pour $k < \theta$. Donc $P(X_n^* = n) \rightarrow 1$.
Cela n'a de sens ici que parce que l'on échantillonne avec remplacement. Avec un échantillonnement sans remplacement, nous manquerions de tanks.

## 6. Expliquer comment construire le graphe de probabilités pour la loi uniforme discrète. En déduire un estimateur graphique $\theta_g$ de $\theta$.

---

On peut en fait montrer que l'estimateur sans biais et de variance minimale de $\theta$ est :
$$\check{\theta}_n = \frac{{X_n^*}^{n+1} - (X_n^*-1)^{n+1}}{{X_n^*}^{n} - (X_n^*-1)^{n}}.$$

Dans la suite de cette première partie, on va comparer numériquement les 5 estimateurs $\tilde{\theta}_n, \tilde{\theta}'_n, \hat{\theta}_n$, $\theta_g$ et $\check{\theta}_n$ à l'aide de simulations en ${\tt R}$.

En ${\tt R}$, la simulation de la loi uniforme discrète se fait avec la commande ${\tt sample}$. ${\tt sample(1:20,10,replace=T)}$ tire 10 nombres au hasard entre 1 et 20 avec remise, tandis que ${\tt sample(1:20,10)}$ tire 10 nombres au hasard entre 1 et 20 sans remise.

## 7. Simuler un échantillon de taille $n=20$ d'une loi ${U}_{\{1,\ldots,\theta\}}$, avec $\theta=1000$. Tracer un histogramme et le graphe de probabilités pour la loi uniforme discrète. Calculez les 5 estimations de $\theta$. Commentez les résultats.

## 8. Simuler $m$ échantillons de taille $n$ d'une loi ${U}_{\{1,\ldots,\theta\}}$, avec $\theta=1000$. Pour chaque échantillon, calculer les valeurs des 5 estimations de $\theta$. On obtient ainsi des échantillons de $m$ valeurs de chacun des 5 estimateurs. Evaluer le biais et l'erreur quadratique moyenne de ces estimateurs. Faites varier $m$ et $n$. Qu'en concluez-vous ?

## 9. Déterminer un intervalle de confiance asymptotique de seuil $\alpha$ pour $\theta$, c'est-à-dire un intervalle aléatoire $I_n$ tel que $\lim_{n \rightarrow \infty} P(\theta \in I_n)=1-\alpha.$

## 10. Simuler $m$ échantillons de taille $n$ d'une loi ${U}_{\{1,\ldots,\theta\}}$. Calculer le pourcentage de fois où l'intervalle de confiance de seuil $\alpha$ pour $\theta$ contient la vraie valeur du paramètre $\theta$. Faire varier $n$, $m$ et $\alpha$, et conclure. 