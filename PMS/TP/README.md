https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_char_d%27assaut_allemand

Consulter le paragraphe **Analyse fréquentiste**

Remarques :
 - On remarque que, une fois observé, un numéro de série n'a aucune chance d'être à nouveau observé.
 - L'écart-type est approximativement égal a l'écart moyen entre deux observations, c'est-à-dire $N / k$. 

I know of three different answers to the German Tank Problem, all giving different results:

    Maximum Likelihood Estimation. Which value of N would make your observations most likely?
    Minimum Variance Unbiased Estimation. Which rule for calculating N would make you right on average (and have as small an error as possible)?

Here’s how they would differ in the German tank problem for the case of just a single observed tank, number M.

Maximum Likelihood Estimation: If there are N tanks and you observe one, then the probability of you observing tank number M is 0 if N<M, and 1/N if N≥M. This probability is maximized if N=M, so that’s what you should guess.

Despite being the hypothesis that best fits the data, the Maximum Likelihood Estimate is almost certainly too small: the true value of N can be bigger than M but cannot be less than M. We would say that using M as a guess for N is a biased estimate because on average M is smaller than N. Looking for an unbiased estimate would lead us to…

Minimum Variance Unbiased Estimation: Perhaps surprisingly, while guessing that N = M is almost always too small, guessing that N = 2M-1 is correct on average. If there were five tanks numbered 1 through 5, and each were shown to a different person and they all used the (2M-1) rule to estimate N, they’d make guesses of

    N=1 (for the person who saw tank #1)
    N=3 (for the person who saw tank #2)
    N=5 (for the person who saw tank #3)
    N=7 (for the person who saw tank #4)
    N=9 (for the person who saw tank #5)

The average guess for N is 5, the true value. This works no matter how many tanks there are! It turns out that guessing N = (2M-1) is the only guessing rule that gives N on average. (This is a fun short exercise!) For other problems, sometimes there is more than one way to make an “unbiased estimate,” and you try to choose a rule that would have the smallest error on average (the “minimum variance”).

On the other hand, it’s a little silly for the person who sees tank #1 to guess that there’s only 1 tank, when that is literally the only tank number that doesn’t rule out any possibilities.

Courtes étude du problème en R :
https://grangeblanche.com/2013/12/23/le-probleme-du-char-dassaut-allemand/

Calculs de la partie 1 (18.14.1) réponse Q4/Q5:
http://www.math.caltech.edu/~2016-17/2term/ma003/Notes/Lecture18.pdf

Lois conditionnelles partie 2:
https://www.wikiwand.com/en/German_tank_problem

Partie 2 Q2/Q3 + graphes :
http://www.gtmath.com/2018/06/parameter-estimation-part-2-german-tank.html
https://simonensemble.github.io/2019-11-15-german-tank-problem/

Un estimateur pour la partie 1 (Q5 débiaisé ??) + réponse Q4:
https://math.stackexchange.com/questions/747978/uniform-distribution-unbiased-estimator

Python code and graph for the estimators:
https://www.eadan.net/blog/german-tank-problem/

R code:
https://www.r-bloggers.com/on-the-german-tank-taxicab-problem/

Analyse en R très détaillée:
https://nathanielwoodward.com/posts/enemy-tank-problem/
