FPGA (field-programmable gate array, réseau de portes programmables in situ)

Un bloc logique est de manière générale constitué d'une table de correspondance (LUT ou Look-Up-Table) et d'une bascule (Flip-Flop en anglais). La LUT sert à implémenter des équations logiques ayant généralement 4 à 6 entrées et une sortie. Elle peut toutefois être considérée comme une petite mémoire, un multiplexeur ou un registre à décalage. Le registre permet de mémoriser un état (machine séquentielle) ou de synchroniser un signal (pipeline).

A LUT, which stands for LookUp Table, in general terms is basically a table that determines what the output is for any given input(s). In the context of combinational logic, it is the truth table. This truth table effectively defines how your combinatorial logic behaves.

L'outil de synthèse cherche les éléments matériels à configurer sur le FPGA pour qu'il se comporte comme l'on attend.
Cela prend du temps de tester toutes les possibilités de circuits valides.
Il renvoie ensuite la meilleure, ici deux LUT3.


`entity` défini les entrées et sorties
Le `component` de l'`architecture structurelle` crèe une nouvelle "boîte" dans celle de l'`entity` créée. Avec `port map` on relie ensuite les fils.


Reset synchrone: action du reset seulement sur front montant de la clock.
