# RISC-V


Par défaut, toutes les étiquettes (ou symboles) déclarées dans un programme assembleur sont privées et invisibles à l’extérieur du fichier. Or la fonction `pgcd_as` doit être visible pour pouvoir être appelée par le programme principal. C’est le but de la directive `.globl` qui rend l’étiquette `pgcd_as` publique.

Par convention, une fonction en assembleur RISCV renvoie sa valeur de retour dans le registre `a0`, c’est à dire `x10`.
Si on écrit une fonction qui ne renvoie rien (`void`), lafonction appelante ignorera le contenu de `a0`.

En fin de fonction, il faut rendre la main à la fonction appelante. Pour cela, il faut sauter à l’adresse de l’instruction suivant celle qui a appelé notre fonction. Par convention, cette adresse, usuellement appelée adresse de retour, est stockée dans le registre `ra` (`x1`).

## Notes de TP

 - gdb effectue la pseudo-instruction `lw` en 1 pas (alors qu’elle fait 2 instructions)
 - `res` , variable globale, mot mémoire à réserver et manipuler avec `sw` et `lw`
 - on écrit les variables globales du fichier dans `.data` avec la directive `.comm name, size` si elle n'est pas initialisée (permet d'allouer du stockage dans la section `.data`, `size` en bytes ou octets ie. **8 bits**)
 - `lw` loads a word from memory into a register
 - `sw` saves a word from a register into RAM : `sw t1, valeur, t2` , où `t1` est le registre dont la valeur sera mise en mémoire à l’adresse désignée par `valeur` et `t2` un registre utilisé pour construire l’adresse désignée par `valeur`
 - Quand il s’agit de zones mémoires à manipuler sur **8 bits** utilisez les instructions de transfert de mémoire adaptées **sb** et **lbu**



## Assembleur

|          C           |                         Assembly                          |                                   Commentaire                                    |
| :------------------: | :-------------------------------------------------------: | :------------------------------------------------------------------------------: |
| `int i = a` <br> `int i = 1` |            `lw t0, a` <br> `addi t0, zero, 1` <br> `li tO, 1`            | Variable `i` locale |
| `res = 0` <br> `uint32_t x` |`sw zero, res, t2` <br> INUTILE | Variable `res` en mémoire (`t2` registre temporaire, qui sera écrasé) <br> Variable `x` globale en memoire (déjà réservée dans le fichier .c)|
| `res = res + t0` |**`lw t1, res`** <br> `add t1, t1, t0` <br> **`sw t1, res, t2`** | Encapsulation d'une opération sur `res` en mémoire |
|  `while (t0 != t1)`  |                    `beq  t0, t1, fin `                    |                          On saute à `fin` si `t0 == t1`                          |
|    `if (t0 < t1)`    |                     `sltu t2, t0, t1` (`slti`)                    |                   On stocke le résultat de `t0 < t1` (`<=`) dans `t2`                   |
|                      |                      `beqz t2, else`                      |                          On saute à `else` si `t2 == 0`                          |
|                      |                        `j fin_if`                         |             Après les opérations dans la branche `(t0 < t1)` du `if`             |
|                      |                         `j while`                         |               Dans `fin_if` près les opérations après le `if else`               |
|                      | **`mv a0, t0`** <br> `add a0, t0, zero` <br> `addi a0, t0, 0` <br> **`lw a0, res`** (`res` en mémoire)|                        `a0` contient la valeur de retour                         |
|                      |                    **`ret`** <br> `jr ra`                     | L'adresse de retour dans la fonction appelante est stockée dans le registre `ra` |
| `t1 % 2 == 1`| `andi t1, t1, 1` | on test si le premier chiffre est à 1 et non à 0 |

## GDB

`quit` pour quitter gdb.

`qemu-system-riscv32 -machine cep -nographic -kernel filename` dans un terminal et `riscv32-unknown-elf-gdb filename` dans un autre pour suivre l'exécution via un gdb connecté à l'émulateur.

gdb vous indique après chaque commande d’exécution la prochaine instruction (C ou asm) qu’il va exécuter dans votre programme et son numéro de ligne 

 - `break main` ajoute un point d'arrêt au début du programme (qemu a déjà posé un point d'arrêt sur le fichier `.as`)
 - `print a` (`p a`) pour un affichage immédiat et `display res_c` (ou `res_as`) pour un affichage persistant après chaque commande gdb (`display {a,b,c}` pour un display multiple)
 - `next` pour continuer l'exécution pas à pas
 - `list` permet de voir les environs du code exécuté
 - `step` permet de continuer à la prochaine instruction dans une fonction
 - `stepi` avance d'une seule vrai instruction