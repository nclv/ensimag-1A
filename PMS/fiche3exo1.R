# Principes et Méthodes Statistiques
# Fiche 3 - Exercice 1

# Création du vecteur des données
partic<-c(75,265,225,402,35,105,411,346,159,229,62,256,431,177,56,144,354,178,386,294)
n<-length(partic)

# Indicateurs statistiques
summary(partic)

# Variance et écart-type empiriques (sans biais)
var(partic)
sd(partic)

# Coefficient de variation empirique
sqrt((n-1)/n)*sd(partic)/mean(partic)

par(mfcol=c(1,2))
# Histogramme à classes de même largeur
a0<-min(partic)-0.025*(max(partic)-min(partic))
a5<-max(partic)+0.025*(max(partic)-min(partic))
bornes<-seq(a0,a5,(a5-a0)/5)
hist(partic, prob=T, breaks=bornes)

# Histogramme à classes de même effectif, en utilisant la commande quantiles
borneseff<-c(a0,quantile(partic,seq(1/5,4/5,1/5)),a5)
hist(partic, prob=T, breaks=borneseff)

par(mfcol=c(1,1))
# Graphe de probabilités pour la loi uniforme
plot(sort(partic), seq(1:n)/n)

# Estimation de a et b par le graphe de probabilités
reg<-lm(seq(1:n)/n~sort(partic))
abline(reg)
-reg$coefficients[1]/reg$coefficients[2]
(1-reg$coefficients[1])/reg$coefficients[2]

