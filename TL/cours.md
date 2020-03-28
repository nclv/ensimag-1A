## R et RE

L est dans R (est « récursif ») s'il existe un programme (une MT) qui **décide** L, c'est à dire qui s'arrête pour tout mot w en entrée et répond « oui » ou « non » selon que w est dans L ou non.

L est dans RE (est récursivement énumérable) s'il existe un programme (une MT) qui **accepte** L, c'est à dire qui :

 - (1) s'arrête en répondant « oui » pour tous les mots de L;
 - mais pour les mots qui ne sont pas dans L, soit (2) s'arrête en répondant « non », soit (3) ne termine pas (boucle).

On a évidemment `R ⊂ RE` (quand aucun mot n'entre dans le cas (3)). Le chapitre 8 montre qu'on n'a pas `R = RE` (et le chapitre 7 montre qu'il existe des langages ∉RE).

## Pseudo-code pour les raisonnements méta

Dans les raisonnements en théorie de la calculabilité, on est souvent améné à décrire à haut niveau comment on construit une certaine MT mais sans rentrer dans les détails (car ce serait fastidieux et pas forcément plus convaincant).

Alternativement, il est souvent aussi convaincant de donner les algorithmes en pseudo-code (en s'appuyant sur l'hypothèse de Church-Turing). On s'autorise ici à écrire des algorithmes dans un pseudo-langage procédural inspiré de Python. On adopte les définitions suivantes (cohérentes avec celles du CM):

 - une fonction f de ℕ dans ℕ est **calculable** ssi il existe une procédure (c-à-d "fonction" au sens de Python) appelée **calcule_f(n) qui termine ssi n est dans le domaine de f** et renvoie alors f(n) (donc si f est totale, calcule_f(n) termine ∀n.)
 - un langage L sur le vocabulaire Σ est **récursif** ssi il existe une procédure appelée **decide_L(w) -- avec w dans Σ* -- qui termine toujours, et retourne soit True si w ∈ L, soit False sinon.**
 - un langage L sur le vocabulaire Σ est **récursivement énumérable** ssi il existe une procédure appelée **accepte_L(w) -- avec  w dans Σ* -- qui termine ssi w est dans L (Cf. CM7, 5.1-Sol.1).**
 - on admet l'existence d'une procédure **termine_borné([m,w,k]) qui décide (donc en terminant toujours et en renvoyant True ou False)** si **la procédure/MT m** termine sur l'entrée w en au plus k étapes (k ∈ ℕ). Évidemment, termine_borné n'a d'intérêt que si m ne termine pas toujours...

---

Ici k est un "timeout" entier en étape de calculs ou en "vrai" temps d'exécution (par exemple des secondes), comme par exemple la commande timeout d'Unix.

Par définition, `termine_borné([m,w,k])==True` implique `termine_borné([m,w,k+1])==True`

### Exemple d'utilisation

Soit L un langage RE (donc pour lequel il existe une procédure `accepte_L`) tel que pour tout n, L contient _exactement 1_ mot de longueur n.
Pour montrer que L est récursif, je construis la procédure decide_L ci-dessous:

```
def decide_L(w):
  n = length(w)
  for k in ℕ: # énumération non-bornée
    for x in { v ∈ Σ* | length(v)==n }: # énumération finie
      if termine_borné([accepte_L, x, k]):
         return x==w
```

En effet, sous les hypothèses ci-dessus, soit u l'unique mot de même longueur que w qui appartient à L. Comme u appartient à L, il existe un k tel que termine_borné([accepte_L, u, k]) == True. Donc, on finit toujours par arriver dans le return de decide_L, et on y arrive quand x==u. Or, w appartient à L ssi w==u.


## Notes
La fonction de transition &delta; définit 3 choses INDÉPENDANTES, pour un **état q** et un **symbole X** dans la case du ruban pointée par la tête de lecture/écriture :

    p : le prochain état p ;
    Y : le symbole écrit dans la case où était X (dans une case il y a toujours un et un seul symbole);
    M : le « mouvement » de la tête de lecture/écriture.

Donc la machine peut très bien changer d'état et modifier la case courante tout en ne se « déplaçant » pas.

La tête ne bouge pas, mais on peut modifier la valeur que la case lue contient. Et on peut modifier l'état q indépendemment du mouvement aussi.

δ(q, X) = (q, Y , S) : On change X en Y, sans bouger et sans changer d'état. On passera l'étape suivante avec la fonction de transition δ(q, Y).

δ(q, X) = (p, X , S) : On change d'état sans bouger la tête ni changer la valeur. On passera à l'étape suivante avec la fonction de transition δ(p, X).
