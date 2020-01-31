Archive fournie par les enseignants pour TPs de TL2

TP1: cf. sujet tp1-pcalc.pdf
-------------------------------
  La version fournie ne sait traiter qu'une expression réduite à un
  entier d'un seul chiffre !

  Fichiers fournis:
  - lexer.py: analyseur lexical *à compléter*
  - test_lexer.py: pour valider votre implémentation de lexer.py
  - parser.py: machine à états des parseurs LL(1).
  - pcalc.py: calculette en syntaxe préfixe *à compléter*
  - test_parser.py: fonctions auxiliaires de tests.
  - test_pcalc.py: pour valider votre implémentation de pcalc.py

  A FAIRE dans l'ordre:
    - Compléter lexer.py (cf. question 5 du sujet).
      Vous pouvez le tester interactivement avec la commande ./lexer.py
      Vérifier que ./test_lexer.py s'exécute sans erreur.
    - Compléter pcalc.py (cf. question 6 du sujet).
      Vous pouvez tester la calculette interactivement avec la commande ./pcalc.py
      Vérifier que ./test_pcalc.py s'exécute sans erreur.
    - Modifier pcalc.py comme indiqué en question 7.

  PARTIE OPTIONNELLE s'il reste du temps:
    => section 1 du sujet tps-extension.pdf

TP2: cf. sujet tp2-calc.pdf
------------------------------

  Fichiers fournis:
  - lexer.py: analyseur lexical du TP1 *à étendre*
  - test_lexer.py: pour valider votre implémentation de lexer.py
  - parser.py: machine à états des parseurs LL(1).
  - calc.py: calculette en syntaxe préfixe *à compléter*
  - test_parser.py: fonctions auxiliaires de tests.
  - test_calc.py: pour valider votre implémentation de calc.py

  A FAIRE:
  - Étendre lexer.py pour ajouter les parenthèses.
    Vérifier que ./test_lexer.py continue de fonctionner.
    Ajouter des tests dans test_lexer.py pour vérifier que les parenthèses sont bien reconnues.
  - Compléter calc.py (cf. sujet tp2-calc.pdf)
    Vous pouvez tester la calculette interactivement avec la commande ./calc.py
  - Vérifier que ./test_calc.py s'exécute sans erreur.

  PARTIE OPTIONNELLE s'il reste du temps:
    => voir tps-extension.pdf
    => si vous allez jusqu'au bout, vérifiez que ./bigtest_calc.py fonctionne...
