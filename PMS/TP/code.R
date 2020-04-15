# Q7.
theta = 1000
p = 1/theta

# Graphe des probabilités
plot(1:theta, rep(p, theta), main="Graphe des probabilités", type="h", lwd=2, ylim=c(0,1), xlim=c(1, theta), col="blue", ylab="Probabilités", xlab="Valeurs observées")
points(1:theta, rep(p, theta), pch=16, cex=1, col="dark red")

nombre_lancers = 20
observations = sample(1:theta, nombre_lancers, replace=TRUE)
# nombre_lancers premières composantes du vecteur d'observations triées
observations.clip = sort(observations)[1:nombre_lancers]
probabilites_cumulee = seq(1:nombre_lancers)/theta
plot(observations.clip, probabilites_cumulee, main="Graphe de probabilités", ylim=c(0,1), xlim=c(1, theta), col="blue", ylab="Probabilités cumulées", xlab="Valeurs observées")
# Régression linéaire
observations.lm <- lm(probabilites_cumulee ~ observations.clip)
print(coef(observations.lm))
print(summary(observations.lm)$r.squared)
# Tracé de la droite
clip(1, theta, 0, 1)
abline(observations.lm, ylim=c(0,1), xlim=c(1, theta))

# Simulation
# observations <- as.factor(observations)
# plot(observations)
totals <- table(observations)
print(totals)
print(paste("Valeur moyenne :", mean(totals)))  # l'inverse du nombre de lancers
barplot(totals, main="Loi uniforme discrète", ylab="Nombre d'observations", xlab="Valeurs observées")

# Estimateur des moments
# Estimateur de la médiane empirique
# Estimateur du maximum de vraisemblance
# Estimateur graphique
# Estimateur de variance minimale

