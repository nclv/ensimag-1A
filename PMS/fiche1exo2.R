# Principes et Méthodes Statistiques
# Fiche 1 - Exercice 2

# Création du vecteur des données.
tremb<-c(0.516, 0.887, 0.783, 0.613, 0.697, 0.459, 0.724, 0.755, 0.867, 0.893, 0.835, 0.718, 0.851, 0.386, 0.855)

# Lecture des données.
tremb
tremb[2]

# Taille du vecteur.
n<-length(tremb)
n

# Données ordonnées.
trembord<-sort(tremb)
trembord

# Histogramme avec le paramétrage par défaut de R.
hist(tremb)

# Histogramme à classes de même largeur suivant les 
# règles du cours.
# La règle de Sturges donne k = 5 classes.
# Calcul des bornes inférieure et supérieure.
a0<-trembord[1]-0.025*(trembord[n]-trembord[1])
a5<-trembord[n]+0.025*(trembord[n]-trembord[1])
a0
a5

# Largeur des classes
h<-(a5-a0)/5
h

# Bornes des classes : on partage [a0,a5] en 5 intervalles
# de largeur h.
bornes<-seq(a0,a5,h)
bornes

# Histogramme corespondant.
hist(tremb, prob=T, breaks=bornes)

# Même chose en couleur avec des limites aux axes.
hist(tremb, prob=T, breaks=bornes,col="blue", xlim=c(0,1), ylim=c(0,4))

# Pour avoir 2 figures dans la même fenêtre, sur une ligne et 2 colonnes.
par(mfcol=c(1,2))
hist(tremb)
hist(tremb, prob=T, breaks=bornes,col="red")

# Même chose avec 2 lignes et une colonne.
par(mfcol=c(2,1))
hist(tremb)
hist(tremb, prob=T, breaks=bornes,col="green")

# Retour à une seule figure par fenêtre.
par(mfcol=c(1,1))

# Histogramme à classes de même effectif 
b<-c(3,6,9,12)
bornes<-c(a0,(trembord[b]+trembord[b+1])/2,a5)
histtremb<-hist(tremb, prob=T, breaks=bornes)

# Même chose en utilisant les quantiles empiriques
bornes<-c(a0,quantile(tremb,seq(1/5,4/5,1/5)),a5)
histtremb<-hist(tremb, prob=T, breaks=bornes)

# Fonction traçant un histogramme à classes de même largeur

histolarg <- function(x, xlim=NULL, ...)
{
# nombre de données
n <- length(x) 
# nombre de classes (règle de Sturges)
if (n<12) k<-5 else k <- round(log2(n)+1) 
# bornes des classes
rangex <- max(x)-min(x)
a0 <- min(x)-0.025*rangex
ak <- max(x)+0.025*rangex
bornes <- seq(a0, ak, length=k+1)
# étendue du tracé
if (is.null(xlim))
xlim<-c(bornes[1], bornes[k+1])
# histogramme
histx<-hist(x, prob=T, breaks=bornes, xlim=xlim, ...)
# histx
}

# Appel de la fonction.
histolarg(tremb)
histolarg(tremb, xlim=c(0,1))

# Histogramme à classes de même effectif

histoeff <- function(x, xlim=NULL, ...)
{
sx <- sort(x)
n <- length(x)
k <- round(log(n)/log(2)+1)
rangex <- max(x)-min(x)
breaks <- c(min(x)-0.025*rangex, quantile(x, seq(1, k-1)/k), max(x)+0.025*rangex)
col <- 0
if (is.null(xlim)) xlim<-c(breaks[1], breaks[k+1])
hist(x, breaks=breaks, col=col, xlim=xlim, probability=T, ...)
}

histoeff(tremb)

# Pour imprimer une figure dans un fichier pdf
# possible aussi en postscript, jpeg,...
pdf("fich1exo2histo.pdf")
histolarg(tremb)
dev.off()

# Fonction de répartition empirique.
plot(ecdf(tremb))

par(mfcol=c(1,2))

# Graphe de probabilités pour la loi uniforme.
plot(trembord,seq(1:n)/n)

# Graphe de probabilités pour la loi puissance.
plot(log(trembord),log(seq(1:n)/n))

# Superposition de la droite des moindres carrés.
abs<-log(trembord)
ord<-log(seq(1:n)/n)
reg<-lm(ord~abs)
lines(abs, fitted.values(reg))

# Estimation graphique des paramètres.
reg$coefficients
c<-reg$coefficients[2]
c
theta<-exp(-reg$coefficients[1]/reg$coefficients[2])
theta

