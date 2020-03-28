# Exercice 1, language L1

Pour reconnaître les mots de la forme `w.c.w`, on itère le processus:

 - «mémoriser» puis «effacer» la première lettre (a ou b) du w à gauche du c
 - «vérifier» qu'il existe une première lettre identique sur le mot à droite du c et «effacer» cette lettre.

En pratique:

 - «mémoriser»/«vérifier» se fait en introduisant des états différents selon qu’on a rencontré un a ou un b en partie gauche (on "duplique" l'automate en le spécialisant sur le traitement d'une lettre).
 - «l'effacement» de la première de lettre de gauche peut se faire de manière standard avec le symbole B (blanc): car on est en train d'effacer une lettre à une extrémité du mot écrit sur le ruban.
 - par contre, «l'effacement» de la première de lettre de droite ne peut pas se faire avec le symbole B (blanc). En effet, on effacerait alors une lettre potentiellement au milieu du mot écrit sur le ruban. A la prochain itération, on ne saurait plus trouver correctement la fin du mot. Il faut donc introduire un symbole spécial X qui sert à représenter les lettres «effacées» en partie droite.

A la fin du processus, **on vérifie qu'il ne reste pas de lettre (a ou b) à droite du c**.

En résumé: étant donné une configuration initiale q0.u où q0 est l'état initial et u est un mot de {a,b,c}* écrit à droite de q0 et bordé de B de chaque côté, on fait une boucle qui reconnaît en fait les configurations $\{ B.q_0.w.c.v.w.B \;|\; w \in \{a,b\}^* \wedge v \in \{X\}^* \}$


On peut s'inspirer sur l'exemple du langage du cours $\{ an.bn | n ∈ ℕ \}$ pour écrire la boucle (qui fait l'effacement des lettres).

# Exercice 1, language L2

L'approche est la même que pour le langage L1, mais **le problème essentiel est de déterminer le milieu du mot qui n'est plus marqué par "c"**. Pour cela, une idée possible est de remplacer les a,b du début du mot par de nouveaux symboles, disons par exemple, A,B et ceux de la fin du mot par d'autres symboles, disons A',B'. Ainsi on passe de (par exemple) abbabb à ABBA'B'B'

Cela est réalisé en **remplaçant d'abord le premier caractère a ou b par la lettre A ou B associée, puis en allant à la fin du mot pour remplacer le dernier caractère a ou b par A' ou B'.**

On passe de donc de:
abbabb
à
AbbabB'
puis
ABbaB'B'
etc.

Notez que cela permet également de s'assurer que le mot est bien de longueur paire: si à un moment on ne trouve pas de caractère a,b à la fin du mot c'est que le mot était de longueur impaire.

Ensuite il faut procéder comme pour L1, sauf que le passage du début à la fin du mot est marqué par le passage des lettres A,B à A',B' et non plus par un c.

Il y a d'autres idées possibles: par exemple compter le nombre de lettres et l'écrire (par ex en unaire) sur le ruban, puis faire une division par deux.

# Exercice 2

La transformation d'un AFD en MT est simple: il suffit de remplacer les transitions `(q,a) -> q'`, par des transitions `(q,a) -> (q',a,D)`, c'est à dire que les transitions recopient simplement les caractères lus et déplacent la tête de lecture toujours vers la droite. 

Il y a cependant une subtilité liée au critère d'acceptation. A la différence des automates, **dans les MT, l'acceptation n'est pas décidée lorsqu'on arrive sur le dernier caractère du mot**. Il faut donc, lorsqu'on arrive sur un état final, **vérifier qu'on est bien à la fin du mot** (i.e. que le caractère suivant est un blanc) avant d'accepter le mot.

Avec les notations de l'énoncé, on a :

```
Q' = Q ∪ {f}  (f nouvel état)
Γ = V ∪ {B}  (B nouveau symbole, le blanc)
F' = {f}
δ'(q, X) = (p, X, D) <--> δ(q, X) = p
δ'(q, B) = (f, B, S)   ∀ q ∈ F
```

# Exercice 3

On suppose que l'entrée est codée sous la forme `1^n # 1^m`. Le `#` sert à séparer les deux opérandes, qui sont codés en unaire. L'objectif est de retourner `1^{x M y}` (i.e. après exécution de la MT, le ruban doit contenir ce mot, avec de préférence la tête de lecture au début).

Par exemple:

11111#111 ---> 11 (= 1^{5-3})

11#111 ---> mot vide (= 1^0)

On peut partir d'une **définition inductive** de la fonction M:
1) 0 M m = 0
2) (n+1) M 0 = (n+1)
3) (n+1) M (m+1) = n M m

On peut donc procéder ainsi:
 - si premier caractère est # (cas de base numéro 1), alors on efface tout le mot (on retourne un mot vide).
 - si le premier caractère est 1, alors on doit aller à la fin du mot, avec deux cas possibles:
    - soit il n'y a plus de 1 après le # (cas de base numéro 2). Alors il suffit simplement d'effacer le #.
    - soit il y a un 1 après le # (cas inductif). Alors il faut effacer un 1 à la fin du mot, et aussi retourner au début et effacer le premier "1" (i.e. on enlève un "1" de chaque coté du #). On recommence ensuite toute l'opération (retour à l'état initial).

Noter que dans la solution fournie :
1) le '#' de l'indication est un 'M'
2) la MT rejette les mots (sur `{1, M}`) qui ne sont pas dans le format attendu. Par exemple le mot vide est rejeté car `δ(q0, B)` n'est pas défini, les mots commençant par MM sont rejetés car `δ(f1, M)` n'est pas défini...

# Exercice 4

$f : ℕ → ℕ$ bijective --> $f$ et $f^{-1}$ sont totales (leur domaine est donc ℕ).

Pour montrer que l'inverse de f est calculable, il faut écrire une procédure `calcule_inv_f` à partir de `calcule_f`. 
Ensuite, il faut justifier que cette procédure calcule ce qu'il faut (en particulier qu'elle termine toujours).

Pour savoir ce que vaut $f^{-1}$(42), si je peux savoir ce que vaut f(n) pour n'importe quel n (et je le peux, car j'ai `calcule_f`), alors je dois bien pouvoir, par une méthode simple mais systématique, trouver l'unique k tel que f(k) = 42...

```
def  Nat(): ## générateur de ℕ, voir autres discussions...
    n = 0
    while True:
        yield n
        n += 1

def calcule_inv_f(n):
    for k in Nat(): ## k parcourt ℕ (dans l'ordre)
        if calcule_f(k) == n: ## Youpi, on a trouvé l'unique antécédant de n
            return k
```

Le reste de l'exo doit s'interpréter en fonction de la solution ci-dessus : si f est surjective mais pas injective, alors on trouve le **plus petit x** tel que f(x) = n ; si f est injective, alors `calcule_inv_f` peut ne pas terminer ; $f^{-1}$ reste partielle calculable (par `calcule_inv_f`) et son domaine est l'image de f...

# Exercice 5

## 5.1
Pour l'union et l'intersection, en pseudo-code : si on a

```
def decide_A(w):...  ## Σ* → Bool
def decide_B(w):...  ## Σ* → Bool
```

il faut écrire

```
def decide_A_Union_B(w):
    return decide_A(w) or decide_B(w)

def decide_A_inter_B(w):
    return decide_A(w) and decide_B(w)
```

Pour le complémentaire, c'est le premier théorème de la diapo 22.

## 5.2

Pour l'union et l'intersection, en pseudo-code : si on a

```
def accepte_A(w):...
## Σ* → True ssi w ∈ A, ne termine pas sinon
def accepte_B(w):...
## Σ* → True ssi w ∈ A, ne termine pas sinon
```

Quand on a fait 5.1 on comprend pourquoi c'est encore ici facile pour **l'intersection** : pour être dans A ∩ B il faut de toutes façons être dans A, donc on peut appeler accepte_A : si elle ne termine pas alors on ne termine pas, mais c'est OK (on n'est pas dans A), et si elle termine il suffit d'appeler accepte_B. On peut donc écrire la même chose que pour 5.1, en remplaçant les « decide_...» par « accepte_... ».

Pour l'union c'est plus compliqué : si on n'est pas dans A on est peut-être dans B. On ne peut donc pas appeler accepte_A et attendre... Mais on peut **lancer les deux « en parallèle simulé » avec `termine_borné`**... D'où :

```
def accepte_A_Union_B(w):
    for k in Nat():
        if termine_borné([accepte_A, w, k])  or \ ## on est dans A
           termine_borné([accepte_B, w, k]):      ## on est dans B
            return True
    ## on sort (en renvoyant True) ssi on est dans A ou dans B
    ## sinon on ne sort jamais de la boucle, donc on boucle...

def accepte_A_Inter_B(w):
    return accepte_A(w) and accepte_B(w)
```

## 5.3
Si on a `accepte_L` et `accepte_comp_L` (pour le complémentaire) alors on peut écrire :

```
def decide_L(w):
    for k in ℕ: # énumération non-bornée
       if termine_borné([accepte_L, w, k]):  ## w ∈ L
         return True
       elif termine_borné([accepte_comp_L, w, k]):  ## w ∉ L
          return False
```

On sortira forcément au bout d'un certain nombre de tours par **une et une seule** des lignes avec un ##.

L'idée avec le pseudo-code « simple » présenté ici est de **« simuler le parallélisme »** (de façon extrêmement inefficace en termes de temps d'exécution, mais ce n'est pas la question).

Ici par exemple : `decide_L` exécute
 - étape de `accepte_L(w)` et éventuellement 0 étape de `accepte_comp_L(w)` ;
 - étape de `accepte_L(w)` (en repartant du début) et éventuellement 1 étape de `accepte_comp_L(w)` (en repartant du début) ;
 - étapes de `accepte_L(w)` (en repartant du début) et éventuellement 2 étapes de `accepte_comp_L(w)` (en repartant du début) ;
 - ...

et ceci jusqu'à ce qu'une des deux procédures `accepte_L` ou `accepte_comp_L` termine (en k étapes). Or on sait qu'un et une seule des deux termine (accepte_L si w ∈ L, accepte_comp_L sinon), d'où le résultat...

# Exercice 6

On fait une preuve par **l'absurde**.

Supposons L un langage de programmation qui ne permet de programmer que des **fonctions totales calculables**, mais **complet**, au sens où toute fonction totale calculable de ℕ dans ℕ y est représentable par (au moins) un programme.

 - Montrer que L est en bijection avec ℕ (comme L est au plus dénombrable, il suffit de montrer qu'il contient une infinité de programmes).
 - À tout entier n∈ℕ on peut donc associer le programme (de L) pn, qui calcule une fonction fn. La preuve consiste ensuite à construire une fonction g de ℕ dans ℕ, totale calculable, donc calculable par (au moins) un programme pm de L (et donc g = fm).
 - Il faut s'arranger pour obtenir une contradiction du type g(m)≠g(m).

L'idée est de construire un g paradoxal, basé sur un **procédé diagonal à la Cantor**.

---

Autrement dit (ayant montré le point 1), on applique le raisonnement suivant...

Soit g la fonction définie par $g(n)=E(fn(n))$ où E est ici une expression que l'on va préciser plus tard...

On montre que **g est totale calculable** de ℕ dans ℕ : il suffit pour cela que **E soit elle-même totale calculable** et que **L soit récursif**...

On en déduit que g est donc calculable par un certain pm de L et que donc g = fm.

Par définition de g, on a g(m)=E(fm(m)).

Par définition de m, on a g(m)=fm(m).

Pour trouver la contradiction finale, il suffit de **trouver une expression E(k) calculable dans ℕ (pour tout k∈ ℕ) tel que E(k)≠k**...

Le schéma ci-dessus avec le E donne une méthode pour trouver des preuves par procédé diagonal.

---

Outre son évident intérêt pédagogique, cet exercice démontre une propriété fondamentale des **langages de programmation** :

Si l'on veut pouvoir écrire tous les programmes qui terminent toujours (i.e. : si on veut pouvoir programmer toutes les fonctions totales calculables), alors on a besoin d'un langage de programmation dans lequel **on doit pouvoir écrire des programmes qui bouclent** (qui ne terminent pas) **sur certaines** de leurs entrées (ces programmes calculant alors des fonctions partielles).

Remarquons qu'un programme (Python p.ex.) qui lève une exception quand son entrée n'est pas dans le domaine de la fonction qu'il calcule (ne satisfait pas les préconditions...) est un programme qui en fait termine toujours. Il calcule donc une fonction totale (l'ensemble B des résultats devenant B ⊎ Exception («union disjointe»).)

Du coup, il existe des programmes Python dans lesquels il est impossible d'ajouter du code (et pas forcément au tout début du programme, style assert...) pour vérifier que l'entrée satisfait les préconditions (est dans le domaine de la fonction calculée...) En fait, ce sont ceux dont **le domaine de la fonction calculée est récursivement énumérable** (par définition car la fonction est calculable) mais non récursif !
