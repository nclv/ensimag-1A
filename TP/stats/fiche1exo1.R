# Principes et Méthodes Statistiques
# Fiche 1 - Exercice 1

# Visualisation de la densité d'une loi normale
m<-2
sigma<-1
curve(dnorm(x,m,sigma),-12,12, col="blue")

# On change la moyenne
m<--3
curve(dnorm(x,m,sigma),add=T, col="red")

# On change la variance
sigma<-3
curve(dnorm(x,m,sigma),add=T, col="green")

# Remarquer que l'aire sous la densité est constante (elle vaut 1)

# Même chose avec la fonction de répartition
m<-2
sigma<-1
curve(pnorm(x,m,sigma),-12,12, col="blue")
pnorm(0,m,sigma)

m<--3
curve(pnorm(x,m,sigma),add=T, col="red")
pnorm(0,m,sigma)

sigma<-3
curve(pnorm(x,m,sigma),add=T, col="green")
pnorm(0,m,sigma)


# Loi normale centrée-réduite
m<-0
sigma<-1
curve(dnorm(x,m,sigma),-4,4)


# Voir la table 1 de la loi normale centrée-réduite en 8.2.1.

pnorm(0)
lines(c(0,0),c(0,dnorm(0)),col="red",lwd=2)

pnorm(1.25)
lines(c(1.25,1.25),c(0,dnorm(1.25)),col="blue",lwd=2)

pnorm(1)
1-pnorm(1)
pnorm(-1)

# Voir la table 2 de la loi normale centrée-réduite en 8.2.2.

qnorm(1-0.05/2)
qnorm(1-0.25/2)

curve(dnorm(x,m,sigma),-4,4)
lines(c(qnorm(1-0.05/2),qnorm(1-0.05/2)),c(0,dnorm(qnorm(1-0.05/2))),col="blue",lwd=2)
lines(c(-qnorm(1-0.05/2),-qnorm(1-0.05/2)),c(0,dnorm(qnorm(1-0.05/2))),col="blue",lwd=2)



