# Partie 1

Une variable aléatoire $X$ est de loi ${U}_{\{1,\ldots,\theta\}}$ si elle est à valeurs dans $\{1, \ldots, \theta\}$ et que 
$$\Bbb{P}(X=k) = \frac{1}{\theta} \, \mathbb{1}_{\{1, \ldots, \theta\}}(k).$$

## 1. Calculer l'espérance et la variance de $X$. 

Les deux résultats sont connus. Calculons la fonction génératrice des moments de $X$.

$$M_X(t) = \Bbb{E}[e^{tX}] = \int e^{tx}\frac{1}{\theta} \, \mathbb{1}_{\{1, \ldots, \theta\}}(x)dx = \frac{1}{\theta}\int_1^\theta e^{tx}dx = \frac{1}{\theta}\bigg[\frac{1}{t}e^{tx}\bigg]_{x=1}^\theta = \frac{e^{t} - e^{\theta t}}{t(1 - \theta)}$$

On a alors $\Bbb{E}[X] = M_X'(0) = \frac{1 + \theta}{2}$ et $\Bbb{Var}(X) = \Bbb{E}[X^2] - \Bbb{E}[X]^2 = M_X''(0) - [M_X'(0)]^2 = \frac{(\theta - 1)^2}{12}$.

## 2. Calculer l'estimateur des moments $\tilde{\theta}_n$ de $\theta$. Montrer que cet estimateur est sans biais et calculer sa variance.

Pour tout $\theta$, $\Bbb{E}_{\theta}[X_1] = \frac{1 + \theta}{2}$. On peut donc prendre par exemple $\Phi(\theta) = \frac{1 + \theta}{2}$ (application bien injective) et $f = Id : \mathbb{R} \rightarrow \mathbb{R}$. L'estimateur obtenu par la méthode des moments est alors $\tilde{\theta}_n = 2\overline{X}_n - 1$.

Cet estimateur est sans biais et consistant.
En effet, pour tout $\theta \in \mathbb{R}$, $\Bbb{E}[\tilde{\theta}_n] = 2\Bbb{E}[\overline{X}_n] - 1 = 2\frac{\theta + 1}{2} - 1= \theta$ et l'application $x \rightarrow 2x - 1$ est continue.

$$\Bbb{Var}(\tilde{\theta}_n) = 4\Bbb{Var}(\overline{X}_n) = \frac{4n}{n^2}\Bbb{Var}(X_1) = \frac{4}{n}\frac{(\theta - 1)^2}{12} = \frac{(\theta - 1)^2}{3n}$$

Le problème avec cet estimateur est que sa valeur peut être inférieure au maximum de l'échantillon.

## 3. Calculer la fonction de répartition de $X$. Calculer la médiane de la loi de $X$ et en déduire un estimateur $\tilde{\theta}'_n$ de $\theta$ basé sur la médiane empirique.

La fonction de masse $f$ de $X$ vérifie $f(x) = \frac{1}{\theta}$ si $1 \leq x \leq \theta$ et $0$ sinon. La fonction de répartition $F$ de $X$ vérifie donc $F(k) = \frac{k}{\theta}$ si $1 \leq k \leq \theta$, $0$ si $k < 1$ et $1$ si $k > \theta$.

Notons $q_{\frac{1}{2}}$ la médiane de $X$. Elle vérifie $F(q_{\frac{1}{2}}) = \frac{1}{2}$. On a trivialement $q_{\frac{1}{2}} = \frac{1 + \theta}{2}$.

On rappelle l'expression de la médiane empirique : $\tilde{Q}_{n,\frac{1}{2}} = \frac{X_{\frac{n}{2}}^* + X_{\frac{n}{2} + 1}^*}{2}$ si $\frac{n}{2}$ est entier et $X_{\left\lfloor\frac{n}{2}\right\rfloor + 1}^*$ sinon.

On considère donc $\tilde{\theta}'_n = 2\tilde{Q}_{n,\frac{1}{2}} - 1$ basé sur la médiane empirique. Il est sans biais et consistant.

---

> On peut noter ici que les calculs de la fonction de répartition et de la médiane sont inutiles.
Nous sommes dans le cas d'une distribution symétrique (en effet, $f(x - \mu) = f(\mu - x)$). Ainsi qu'on prenne la moyenne ou la médiane comme estimateur, on estimera la même quantité car les deux paramètres sont identiques.

> Est-ce qu’on devrait utiliser la moyenne ou la médiane de l’échantillon pour estimer notre paramètre de position $\theta$ ? Lorsque plusieurs estimateurs estiment la même quantité et que leur biais est négligeable ou nul, le choix se fait généralement sur la base de la variance de l’estimateur, une mesure de précision : on va préférer un estimateur qui a une plus petite variance puisque ça veut dire qu’en moyenne la distance (au carré) entre l’estimateur et le paramètre est moindre. Celle-ci dépend toutefois de la distribution de laquelle proviennent les données - qui en pratique nous reste inconnue.

## 4. Soit $X_n^*$ le maximum des observations. Calculer la fonction de répartition de $X_n^*$ et les probabilités élémentaires $P(X_n^*=k)$, $\forall k \in \{1, \ldots, \theta\}$.

$\Bbb{P}(X_n^* \leq k) = \big(\frac{k}{\theta}\big)^n$ par indépendance des observations de même probabilité.
Si $k > \theta$ cette probabilité vaut 1.

L'évènement $(X_n^* = k)$ est le complémentaire de $(X_n^* < k) \cup (X_n^* > k)$.

Ainsi $\Bbb{P}(X_n^* = k) = 1 - \big(\big(\frac{k - 1}{\theta}\big)^n + \big(1 - \big(\frac{k}{\theta}\big)^n\big)\big) = \big(\frac{k}{\theta}\big)^n - \big(\frac{k - 1}{\theta}\big)^n$

## 5. Montrer que l'estimateur de maximum de vraisemblance de $\theta$ est $\hat{\theta}_n=X_n^*$. Montrer qu'il est biaisé mais qu'on ne peut pas le débiaiser facilement.

La fonction de masse de notre problème est $p_\theta(x) = \frac{1}{\theta}$ si $x \leq \theta$ et $0$ sinon.

Ainsi, l'estimateur du maximum de vraisemblance pour un échantillon de $n$ tanks issus d'un échantillon aléatoire de variables indépendantes vaut :

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
Si $n = 1$ et que le tank a le numéro de série $x$ alors $x$ est l'estimation du maximum de vraisemblance du nombre total de tanks.

On note ici que le support, représenté par les valeurs de $x$ donnant une fonction de masse positive, dépend de $\theta$. Pour le calcul de la borne de Cramér-Rao on suppose que le support n'en dépend pas.

---

$$
\begin{aligned}
    \Bbb{E}_{\theta}[\hat{\theta}_n] &= \sum_{k=1}^{\theta} k\bigg(\bigg(\frac{k}{\theta}\bigg)^n - \bigg(\frac{k - 1}{\theta}\bigg)^n\bigg) \\
    &= \theta^{-n}.\bigg(\theta^{n+1} - \sum_{k=1}^{\theta - 1} k^n \bigg) \\
    &= \theta - \sum_{k=1}^{\theta - 1} \bigg(\frac{k}{\theta}\bigg)^n \\
\end{aligned}
$$

Sans prendre la peine de finir le calcul, on voit que l'on obtiendra pas $\theta$. En effet, prenons une seule observation, alors $n = 1$ et $\Bbb{E}_{\theta}[\hat{\theta}_n] = \frac{\theta + 1}{2}$ ce qui donne un biais de $\frac{1 - \theta}{2}$.
Cet estimateur est difficile à débiaiser car la somme dépend de $\theta$.

Cependant, l'estimateur est consistant. $\Bbb{P}(X_n^* = k) \rightarrow 0$ lorsque $n \rightarrow \infty$ pour $k < \theta$. Donc $\Bbb{P}(X_n^* = n) \rightarrow 1$.
Cela n'a de sens ici que parce que l'on échantillonne avec remplacement. Avec un échantillonnement sans remplacement, nous manquerions de tanks.

---

On peut vérifier la consistance de cet estimateur par un calcul rapide
En effet, soit $\epsilon > 0$

$$
\begin{aligned}
    \Bbb{P}(|\hat{\theta}_n - \theta | \geq \epsilon) &= 1 - \Bbb{P}(\theta - \epsilon \leq \hat{\theta}_n \leq \theta + \epsilon) \\
    &= 1 - (F_{\hat{\theta}_n}(\theta + \epsilon) - F_{\hat{\theta}_n}(\theta - \epsilon)) \\
    &= \bigg(\frac{\theta - \epsilon}{\theta}\bigg)^n \\
\end{aligned}
$$
Or $1 - \frac{\epsilon}{\theta} < 1$ donc la série de terme général $\Bbb{P}(|\hat{\theta}_n - \theta | \geq \epsilon)$ converge et on a $\hat{\theta}_n \rightarrow \theta$ presque sûrement.

## 6. Expliquer comment construire le graphe de probabilités pour la loi uniforme discrète. En déduire un estimateur graphique $\theta_g$ de $\theta$.

Si $\theta$ est connu il est facile de tracer le graphe (voir Q7.) car toutes les entrées ont la probabilité $\frac{1}{\theta}$. On trace dans notre exemple le nuage de points $(x_i^*, \frac{i}{n}\theta)$ pour $i \in \{1, \ldots, n\}$. Si ces points sont approximativement alignés sur une droite de pente positive passant par l’origine, on pourra considérer que la loi uniforme discrète est un modèle probabiliste vraisemblable pour ces observations. L'inverse de la pente de la droite fournit alors une **estimation graphique $\theta_g$ de $\theta$**. Inversement, si ce n’est pas le cas, il est probable que les observations ne soient pas issues d’une loi uniforme discrète.

---

On peut en fait montrer que l'estimateur sans biais et de variance minimale de $\theta$ est :
$$\check{\theta}_n = \frac{{X_n^*}^{n+1} - (X_n^*-1)^{n+1}}{{X_n^*}^{n} - (X_n^*-1)^{n}}.$$

Dans la suite de cette première partie, on va comparer numériquement les 5 estimateurs $\tilde{\theta}_n, \tilde{\theta}'_n, \hat{\theta}_n$, $\theta_g$ et $\check{\theta}_n$ à l'aide de simulations en ${\tt R}$.

En ${\tt R}$, la simulation de la loi uniforme discrète se fait avec la commande ${\tt sample}$. ${\tt sample(1:20,10,replace=T)}$ tire 10 nombres au hasard entre 1 et 20 avec remise, tandis que ${\tt sample(1:20,10)}$ tire 10 nombres au hasard entre 1 et 20 sans remise.

## 7. Simuler un échantillon de taille $n=20$ d'une loi ${U}_{\{1,\ldots,\theta\}}$, avec $\theta=1000$. Tracer un histogramme et le graphe de probabilités pour la loi uniforme discrète. Calculez les 5 estimations de $\theta$. Commentez les résultats.

## 8. Simuler $m$ échantillons de taille $n$ d'une loi ${U}_{\{1,\ldots,\theta\}}$, avec $\theta=1000$. Pour chaque échantillon, calculer les valeurs des 5 estimations de $\theta$. On obtient ainsi des échantillons de $m$ valeurs de chacun des 5 estimateurs. Evaluer le biais et l'erreur quadratique moyenne de ces estimateurs. Faites varier $m$ et $n$. Qu'en concluez-vous ?

## 9. Déterminer un intervalle de confiance asymptotique de seuil $\alpha$ pour $\theta$, c'est-à-dire un intervalle aléatoire $I_n$ tel que $\lim_{n \rightarrow \infty} P(\theta \in I_n)=1-\alpha.$

Posons $P = \frac{X_n^*}{\theta}$ notre fonction pivot. En effet, on a bien $\Bbb{P}(P \leq k) = k^n$ (indépendant de $\theta$) par indépendance des tirages de même probabilité.

On remarque que $\Bbb{P}(P \leq \alpha^{\frac{1}{n}}) = \alpha$ et que $\Bbb{P}(P \leq 1) = 1$.
Ainsi,

$$ 1 - \alpha = \Bbb{P}(\alpha^{\frac{1}{n}} \leq P \leq 1) = \Bbb{P}(\alpha^{\frac{1}{n}} \leq \frac{X_n^*}{\theta} \leq 1) = \Bbb{P}(X_n^* \leq \theta \leq \frac{X_n^*}{\alpha^{\frac{1}{n}}})$$

Donc $I_n = \bigg[X_n^*, \frac{X_n^*}{\alpha^{\frac{1}{n}}}\bigg]$ est un intervalle de confiance asymptotique de seuil $\alpha$ pour $\theta$.

---

Pour trouver l'intervalle de confiance pour $\theta$ basé sur $n$ observations de valeur maximum $k$, on peut aussi résoudre les deux équations suivantes :

$$ \Bbb{P}(X_n^* \leq k) = \bigg(\frac{k}{\theta}\bigg)^n = \frac{\alpha}{2}$$
$$ \Bbb{P}(X_n^* \geq k) = 1 - \Bbb{P}(X_n^* \leq k - 1)  = 1 - \bigg(\frac{k - 1}{\theta}\bigg)^n = \frac{\alpha}{2}$$

On obtient donc $\theta_{+} = \frac{k}{(\frac{\alpha}{2})^\frac{1}{n}}$ et $\theta_{-} = \frac{k}{(1 - \frac{\alpha}{2})^\frac{1}{n}}$.

Puisque la distribution de l'échantillon est asymétrique, on préfère se ramener à l'intervalle précédemment calculé.

---

On obtient ainsi :

|  $n$  | Intervalle de confiance |
| :---: | :---------------------: |
|   1   |       $[k, 20k]$        |
|   2   |       $[k, 4.5k]$       |
|   5   |      $[k, 1.82k]$       |
|  10   |      $[k, 1.35k]$       |
|  20   |      $[k, 1.16k]$       |


## 10. Simuler $m$ échantillons de taille $n$ d'une loi ${U}_{\{1,\ldots,\theta\}}$. Calculer le pourcentage de fois où l'intervalle de confiance de seuil $\alpha$ pour $\theta$ contient la vraie valeur du paramètre $\theta$. Faire varier $n$, $m$ et $\alpha$, et conclure. 

# Partie 2

## 1.

La loi de $X_1$ n'a pas changé.
$$\Bbb{P}(X_1=x_1) = \frac{1}{\theta} \, \mathbb{1}_{\{1, \ldots, \theta\}}(x_1).$$

Prenons la première probabilité conditionnelle,
$$\Bbb{P}(X_2 = x_2 | X_1=x_1) = \frac{\Bbb{P}(X_2 = x_2, X_1 = x_1)}{\Bbb{P}(X_2 = x_2)}$$

Or le couple $(X_1, X_2)$ suit une loi uniforme sur $\{(x_1, x_2), x_1 \in \{1, \ldots, \theta\}, x_2 \in \{1, \ldots, \theta\}, x_1 \neq x_2 \}$ donc
$$\Bbb{P}(X_2 = x_2, X_1=x_1) = \frac{1}{\theta(\theta - 1)}, x_1 \in \{1, \ldots, \theta\}, x_2 \in \{1, \ldots, \theta\}, x_1 \neq x_2$$

Généralisons,
$$
\begin{aligned}
    \Bbb{P}(X_k = x_k | X_1=x_1, \ldots, X_{k-1} = x_{k-1}) &= \frac{\Bbb{P}(\bigcap_{j=1}^{k} (X_j = x_j))}{\Bbb{P}(\bigcap_{j=1}^{k - 1} (X_j = x_j)} \\
    &= \frac{\Bbb{P}(X_1=x_1).\Bbb{P}(X_2=x_2 | X_1=x_1).\Bbb{P}(X_3=x_3 | X_2=x_2, X_1=x_1) \ldots \Bbb{P}(X_k=x_k | \bigcap_{j=1}^{k-1} (X_j = x_j))}{\Bbb{P}(X_1=x_1).\Bbb{P}(X_2=x_2 | X_1=x_1).\Bbb{P}(X_3=x_3 | X_2=x_2, X_1=x_1) \ldots \Bbb{P}(X_{k-1}=x_{k-1} | \bigcap_{j=1}^{k-2} (X_j = x_j))} \\
    &= \frac{\theta}{\theta}\frac{(\theta - 1)}{(\theta - 1)}.\frac{(\theta - 2)}{(\theta - 2)} \ldots \frac{(\theta - k + 2)}{(\theta - k + 2)}\frac{1}{(\theta - k + 1)} \\
    &= \frac{1}{(\theta - k + 1)}
\end{aligned}
$$
Plus simplement la probabilité de tirer $x_k$ sachant que l'on a déjà fait $k - 1$ tirages sans remise dans un ensemble de $\theta$ éléments est $\frac{1}{(\theta - k + 1)}$ (avec bien sûr $x_k \leq \theta$). Mais quelques révisions calculatoires ne peuvent pas faire de mal...

$$
L(\theta, x_1, \ldots, x_n) = \left\{
    \begin{array}{ll}
        \frac{1}{\theta}.\frac{1}{(\theta - 1)} \ldots \frac{1}{(\theta - n + 1)} & \text{si } max_i (x_i) \leq \theta \\
        0 & \text{sinon.}
    \end{array}
\right.
$$

Cette fonction est aussi maximisée pour $\hat{\theta}_n = max_i (x_i) = X_n^*$.

---

Calculons la variance de notre estimateur des moments.
$$\Bbb{Var}(\tilde{\theta}_n) = 4\Bbb{Var}(\overline{X}_n) = 4\sum_{i=1}^n \frac{1}{n^2}\Bbb{Var}(X_i) = \frac{4}{n}\frac{(\theta - n)(\theta - 1)}{12} = \frac{(\theta - n)(\theta - 1)}{3n}$$


## 2.

Reformulons l'évènement recherché. On recherche en fait un probabilité conditionnelle.
La probabilité que le numéro de série maximum observé soit égal à $k$ quand le nombre de tanks est connu égal à $\theta$ et que le nombre de tanks observés est égal à $n$.
On cherche donc à répondre à la question : quelle est la probabilité qu'un nombre de série $k$ soit le maximum observé dans un échantillon de $n$ tanks lorsqu'il y en a $\theta$ au total ?

La probabilité d'obtenir un échantillon de maximum $k$ est le nombre de façons de choisir un échantillon ayant un maximum $k$ divisé par le nombre d'échantillons.
On a $k - 1$ parmi $n - 1$ ensembles distincts de $n$ numéros de série où le numéro de série maximal est $k$. 

Ainsi, pour choisir un échantillon de maximum $k$, il faut choisir l'observation correspondant à $k$ ainsi que $n - 1$ autres observations de l'ensemble $\{1, \ldots k - 1\}$ de $k - 1$ parmi $n - 1$ façons. Donc

$$\Bbb{P}(X_n^* = k) = \frac{\left(_{n-1}^{k-1} \right)}{\left(_{n}^{\theta} \right)}$$

Notez qu'il faut $k$ telle que $n \leq k \leq \theta$ puisque le numéro de série maximum ne peut pas être supérieur au nombre total de tanks ou inférieur au nombre de tanks capturés.

On peut maintenant calculer la fonction de répartition de $X_n^*$ et tracer la distribution.
En effet, c'est l'intégrale de $\Bbb{P}(X_n^* = k)$ par rapport à la variable $k$. Ainsi,

$$\Bbb{P}(X_n^* \leq k) = \frac{\left(_{n}^{k} \right)}{\left(_{n}^{\theta} \right)}$$

---

$$
\begin{aligned}
    \Bbb{E}[X_n^*] &= \sum_{k=n}^{\theta}{k \frac{{k-1}\choose{n-1}}{{\theta}\choose{n}}} \\  
    &= \frac{1}{(n-1)!{\theta \choose n}} \sum_{k=n}^{\theta}{\frac{k!}{(k-n)!}} \\ 
    &= \frac{n!}{(n-1)!{\theta \choose n}} \sum_{k=n}^{\theta}{k \choose n} \\ 
    &= n \frac{{\theta+1}\choose{n+1}}{\theta \choose n} \\ 
    &= \frac{n}{n+1}(\theta+1) 
\end{aligned}
$$

La valeur obtenue n'est égale à $\theta$ seulement quand $n = \theta$. $X_n^*$ est donc un estimateur biaisé de $\theta$.

On en déduit que $\hat{\theta}_n^{(1)}=\frac{n+1}{n}X_n^*-1$ est un estimateur sans biais de $\theta$.

---

La variance de l'estimateur $\hat{\theta}_n^{(1)}$ est $\frac{1}{n}\frac{(\theta - n)(\theta  - 1)}{n + 2}$ après calculs.

> On a $\Bbb{Var}(\hat{\theta}_n^{(1)}) = \frac{(n + 1)^2}{n^2}\Bbb{Var}(X_n^*)$. Le calcul de $\Bbb{E}[(X_n^*)^2]$ est ce qui pose problème.

---

On aurait pu construire cet estimateur à partir de celui proposé à la question suivante.
On remplace l'écart $(x_1^* - 1)$ par la moyenne des écarts de notre échantillon. On obtient ainsi un écart moyen

$$
\begin{aligned}
    E_{moy} &= \frac{1}{n}((x_1^* - 1) + (x_2^* - x_1^* - 1) + (x_3^* - x_2^* - 1) + \ldots + (x_n^* - x_{n - 1}^* - 1)) \\
    &= \frac{1}{n}(x_n^* - n) \\
    &= \frac{x_n^*}{n} - 1
\end{aligned}
$$

On retrouve bien l'estimateur $\hat{\theta}_n^{(1)} = X_n^* + E_{moy} = X_n^* + \frac{X_n^*}{n} - 1$.

# 3.

Comment avons nous construit cet estimateur ? On estime que le nombre de tanks avec un numéro de série inférieur au minimum de l'échantillon (ils n'ont pas été observés) est environ égal au nombre de tanks avec un numéro de série supérieur au maximum de l'échantillon.
Cela nous donne $\hat{\theta}_n^{(2)} = X_n^* + (X_1^* - 1)$.

---

La variance de l'estimateur $\hat{\theta}_n^{(2)} = X_n^* + X_1^* - 1$ est $\frac{2}{n + 1}\frac{(\theta - n)(\theta  - 1)}{n + 2}$ après calculs.

