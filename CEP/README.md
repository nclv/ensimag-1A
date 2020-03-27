# RISC-V


Par défaut, toutes les étiquettes (ou symboles) déclarées dans un programme assembleur sont privées et invisibles à l’extérieur du fichier. Or la fonction `pgcd_as` doit être visible pour pouvoir être appelée par le programme principal. C’est le but de la directive `.globl` qui rend l’étiquette `pgcd_as` publique.

Par convention, une fonction en assembleur RISCV renvoie sa valeur de retour dans le registre `a0`, c’est à dire `x10`.
Si on écrit une fonction qui ne renvoie rien (`void`), lafonction appelante ignorera le contenu de `a0`.

En fin de fonction, il faut rendre la main à la fonction appelante. Pour cela, il faut sauter à l’adresse de l’instruction suivant celle qui a appelé notre fonction. Par convention, cette adresse, usuellement appelée adresse de retour, est stockée dans le registre `ra` (`x1`).