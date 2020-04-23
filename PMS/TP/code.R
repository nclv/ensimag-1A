library(ggplot2)

# Q7.

# Graphe des probabilités
# plot(1:theta, rep(p, theta), main="Graphe des probabilités", type="h", lwd=2, ylim=c(0,1), xlim=c(1, theta), col="blue", ylab="Probabilités", xlab="Valeurs observées")
# points(1:theta, rep(p, theta), pch=16, cex=1, col="dark red")

histogram <- function(observations) {
    # Histogramme des observations
    # observations <- as.factor(observations)
    # plot(observations)
    # totals <- table(observations)
    # print(totals)
    # print(paste("Valeur moyenne :", mean(totals)))  # l'inverse du nombre de lancers
    # barplot(totals,
    #         main = "Loi uniforme discrète",
    #         ylab = "Nombre d'observations",
    #         xlab = "Valeurs observées")
    
    # classes de même largeur
    # ce n'est pas adapté à toutes les distributions
    # il faudrait adapter l'histogramme à chaque échantillon pour avoir qqch d'utile
    h <- hist(observations,
              main = "Histogramme des observations",
              ylab = "Nombre d'observations",
              xlab = "Valeurs observées")
    text(h$mids,
         h$counts,
         labels = h$counts,
         adj = c(0.5, -0.5))
}

probability_graph <-
    function(nombre_observations, theta) {
        observations <- sample(1:theta, nombre_observations, replace = T)
        # nombre_lancers premières composantes du vecteur d'observations triées
        observations.clip = sort(observations)[1:nombre_observations]
        probabilites_cumulee = seq(1:nombre_observations) / theta
        plot(
            observations.clip,
            probabilites_cumulee,
            main = "Graphe de probabilités",
            ylim = c(0, max(probabilites_cumulee)),
            # doit rester inférieur à 1
            xlim = c(1, theta),
            col = "blue",
            ylab = "Probabilités cumulées",
            xlab = "Valeurs observées"
        )
        
        # Régression linéaire
        observations.lm <-
            lm(probabilites_cumulee ~ observations.clip)
        # print(coef(observations.lm))
        # print(summary(observations.lm)$r.squared)
        
        # Tracé de la droite
        clip(1, theta, 0, 1)
        abline(observations.lm,
               ylim = c(0, max(probabilites_cumulee)),
               # doit rester inférieur à 1
               xlim = c(1, theta))
        
        # on récupère l'inverse de la pente de la droite de régression
        theta_graph <- 1 / coef(observations.lm)[2]
        
        return(theta_graph)
    }


estimateur.graph <- function(theta, nombre_observations) {
    observations = sample(1:theta, nombre_observations, replace = T)
    observations.clip = sort(observations)[1:nombre_observations]
    probabilites_cumulee = seq(1:nombre_observations) / theta
    observations.lm <-
        lm(probabilites_cumulee ~ observations.clip)
    return(1 / coef(observations.lm)[2])
}

estimateur.moments <-
    function(theta, nombre_observations, replace) {
        observations = sample(1:theta, nombre_observations, replace = replace)
        return(2 * mean(observations) - 1)
    }

estimateur.mediane <-
    function(theta, nombre_observations, replace) {
        observations = sample(1:theta, nombre_observations, replace = replace)
        return(2 * median(observations) - 1)
    }

estimateur.max <- function(theta, nombre_observations, replace) {
    observations = sample(1:theta, nombre_observations, replace = replace)
    return(max(observations))
}

estimateur.variance_min <-
    function(theta, nombre_observations, replace) {
        observations = sample(1:theta, nombre_observations, replace = replace)
        n = length(observations)
        m = max(observations)
        return((m ^ (n + 1) - (m - 1) ^ (n + 1)) / (m ^ n - (m - 1) ^ n))
    }

estimateur.max_unbiaised <-
    function(theta, nombre_observations, replace) {
        observations = sample(1:theta, nombre_observations, replace = replace)
        return((1 + 1 / length(observations)) * max(observations) - 1)
    }

estimateur.max_min <-
    function(theta, nombre_observations, replace) {
        observations = sample(1:theta, nombre_observations, replace = replace)
        return(max(observations) + min(observations) - 1)
    }


estimate_avec_remise <- function(nombre_observations, theta) {
    # Nombre de répétitions (ou d'échantillons)
    m = 5000
    
    # Estimateur des moments
    theta_moments <-
        replicate(m,
                  estimateur.moments(theta, nombre_observations, replace = T))
    # Estimateur de la médiane empirique
    theta_mediane <-
        replicate(m,
                  estimateur.mediane(theta, nombre_observations, replace = T))
    # Estimateur du maximum de vraisemblance
    theta_max <-
        replicate(m, estimateur.max(theta, nombre_observations, replace = T))
    # Estimateur graphique
    theta_graph <-
        replicate(m, estimateur.graph(theta, nombre_observations))
    # Estimateur de variance minimale
    theta_min <-
        replicate(m,
                  estimateur.variance_min(theta, nombre_observations, replace = T))
    
    return_list <-
        list(
            "moments" = theta_moments,
            "mediane" = theta_mediane,
            "max" = theta_max,
            "graph" = theta_graph,
            "variance_min" = theta_min
        )
    return(return_list)
}

estimate_sans_remise <- function(nombre_observations, theta) {
    # Nombre de répétitions (ou d'échantillons)
    m = 5000
    
    # Estimateur des moments
    theta_moments <-
        replicate(m,
                  estimateur.moments(theta, nombre_observations, replace = F))
    # Estimateur du maximum de vraisemblance
    theta_max <-
        replicate(m, estimateur.max(theta, nombre_observations, replace = F))
    # Estimateur sans biais
    theta_ss_biais <-
        replicate(m,
                  estimateur.max_unbiaised(theta, nombre_observations, replace = F))
    # Estimateur proposé
    theta_prop <-
        replicate(m,
                  estimateur.max_min(theta, nombre_observations, replace = F))
    
    return_list <-
        list(
            "moments" = theta_moments,
            "max" = theta_max,
            "max_unbiaised" = theta_ss_biais,
            "max_min" = theta_prop
        )
    return(return_list)
}


# Affichages graphiques
plot_estimations <- function(estimations) {
    for (name in names(estimations)) {
        print(
            qplot(
                estimations[[name]],
                main = paste("Distribution de l'estimateur", name),
                ylab = "Nombre d'observations",
                xlab = "Valeurs de theta estimées",
                fill = ..count..
                    ) + theme_minimal() + geom_vline(aes(xintercept = 1000), lty = 3) + scale_fill_gradient(low = "blue", high = "red") + annotate("text", x = (min(estimations[[name]]) + 1000)/2, y = 5000/6, label = paste("sd<theta> :", round(sd(estimations[[name]]), digits = 2)), fontface = 2) + annotate("text", x = (min(estimations[[name]]) + 1000)/2, y = 5000/6  - 60, label = paste("<theta> :", round(mean(estimations[[name]]), digits = 2)), fontface = 2)
        )
        moyenne_glissante <- vector()
        for (i in 1:5000) {
            moyenne_glissante[i] <- mean(estimations[[name]][1:i])
        }
        print(
            qplot(
                1:5000,
                moyenne_glissante,
                xlab = "Numéro de l'observation",
                ylab = "Moyenne glissante"
            ) + geom_line() + geom_hline(yintercept = 1000, color = "red")
        )
    }
}

# Analyse des graphes
# Pour vérifier si l'estimateur est biaisé ou non on fait 5000 simulations
# avec theta et n fixés. On applique ensuite les estimateurs à chaque échantillon
# et on observe la distribution obtenue.
# Un estimateur non biaisée aura, sur de nombreuses simulations, une valeur moyenne égale au nombre réel de tanks (ie. theta).
# L'efficacité de l'estimateur est observé en regardant la valeur de la variance. 
# Un estimateur non-biaisé efficace aura la plus petite variance parmi les autres estimateurs non biaisés.
# On peut aussi observer la consistance de l'estimateur. On devrait observer que la distribution se concentre autour de la valeur réelle de theta lorsque le nombre d'observations augmente.
# Plus l'on capture de tanks, plus notre estimation de theta aura de chance d'être correcte.

superposed_histplot <- function(estimations) {
    df <- stack(as.data.frame(do.call(cbind, estimations)))
    colnames(df)[2] <- "n_values"
    ggplot(df, aes(x=values, fill=n_values)) + geom_histogram(alpha=0.2, position="identity") + geom_vline(xintercept = 1000, color = "red") + ylab("Nombre d'observations") + xlab("Valeurs de theta estimées") 
}

consistance <- function(theta, estimateur) {
    n <- 5000
    new_list <- list()
    for (nombre_observations in seq(20, theta, length.out = 3)) {
        estimations <-
            replicate(n,
                      estimateur(theta, nombre_observations, replace = F))
        new_list <- c(new_list, list(estimations))
    }
    names(new_list) <- seq(20, theta, length.out = 3)
    return(new_list)
}


bias <- function(observations, theta) {
    return(mean(observations) - theta)
}

mse <- function(observations, theta) {
    return(var(observations) + bias(observations, theta) ^ 2)
}

estimators.summary <- function(estimations, theta) {
    # Si un estimateur est non biaisé, sa variance est égale à sa MSE
    # La variance mesure la précision de l'estimateur.
    # Le biais mesure son exactitude.
    # Un estimateur avec une bonne MSE à une petite variance et un petit biais. 
    estimations.mean <- sapply(estimations, mean)
    estimations.sd <- sapply(estimations, sd)
    estimations.var <- sapply(estimations, var)
    estimations.bias <- sapply(estimations, bias, theta = theta)
    estimations.mse <- sapply(estimations, mse, theta = theta)
    estimations.summary <- list(
        estimations.mean = estimations.mean,
        estimations.sd = estimations.sd,
        estimations.var = estimations.var,
        estimations.bias = estimations.bias,
        estimations.mse = estimations.mse
    )
    print(estimations.summary)
}

# le nombre d'observations est toujours inférieur à theta
# (on ne peut pas observer plus de tanks que le nombre de tanks produits)
probability_graph(nombre_observations = 20, theta = 1000)
estimations <-
    estimate_avec_remise(nombre_observations = 20, theta = 1000)
estimators.summary(estimations, theta = 1000)
# theta = 1000 et n = 20
histogram(sample(1:1000, 20, replace = T))
# on n'affiche pas l'estimateur graphique
plot_estimations(estimations[- 4])

estimations <-
    estimate_sans_remise(nombre_observations = 20, theta = 1000)
estimators.summary(estimations, theta = 1000)
# theta = 1000 et n = 20
histogram(sample(1:1000, 20, replace = F))
plot_estimations(estimations)

# superposed_histplot(consistance(1000, estimateur.moments))

# 2. Comparaison de variances entre estimateurs sans remise non biaisés

var.moments <- function(theta, n) {
    return((theta - n) * (theta - 1) / (3 * n))
}
var.max_unbiaised <- function(theta, n) {
    return(1 / n * (theta - n) * (theta - 1) / (n + 2))
}
var.max_min <- function(theta, n) {
    return(2 / (n + 1) * (theta - n) * (theta - 1) / (n + 2))
}

theta = 1000
values_moments <- vector()
values_max_unbiaised <- vector()
values_max_min <- vector()
for (n in 0:100) {
    values_moments[n] <- var.moments(theta, n = n)
    values_max_unbiaised[n] <- var.max_unbiaised(theta, n)
    values_max_min[n] <- var.max_min(theta, n)
}
print(
    ggplot(data.frame(
        y = values_moments, y1 = values_max_unbiaised, y2 = values_max_min, x = 0:99
    ), aes(x, y)) +
        geom_point() + geom_point(aes(x, y), color = "red") + geom_point(aes(x, y1), color = "green") + geom_point(aes(x, y2), color = "blue") + theme_minimal() +
        ylab("Variances des estimateurs pour theta = 1000") + xlab("n")
)
# On voit que l'estimateur max_unbiaised (en vert) a la plus faible variance des 3 estimateurs toute taille d'échantillons confondue.
# C'est en fait le MVUE.

# Confidence Intervals
# on visualise la distribution de chaque estimateur sur 5000 simulations en faisant varier theta
confidence <- function(nombre_observations, estimateur) {
    m <- 5000
    new_list <- list()
    for (theta in round(seq(100, 160, length.out = 7))) {
        estimations <-
            replicate(m,
                      estimateur(theta, nombre_observations, replace = F))
        new_list <- c(new_list, list(estimations))
    }
    names(new_list) <- round(seq(100, 160, length.out = 7))
    return(new_list)
}

superposed_boxplot <- function(estimations) {
    # Pour tracer la ligne
    observations = sample(1:120, 20, replace = F)
    # Pour tracer tout le reste
    df <- stack(as.data.frame(do.call(cbind, estimations)))
    colnames(df)[2] <- "theta_values"
    ggplot() + geom_boxplot(data = df, aes(x=theta_values, y = values, fill = theta_values), outlier.shape = NA) + ylab("Estimations de theta") + xlab("Valeurs réelles de theta") + geom_point(data = data.frame(x = seq(1, 7), y = round(seq(100, 160, length.out = 7))), aes(x= x, y = y), color = "pink") + geom_line(data = data.frame(x = seq(1, 7), y = round(seq(100, 160, length.out = 7))), aes(x= x, y = y), linetype = "dashed") + geom_hline(yintercept = max(observations), color = "blue")
}
superposed_boxplot(confidence(20, estimateur.moments))

# On réalise ici une estimation de l'intervalle auquel appartient le nombre de tanks.
# Disons que l'on observe un numéro de série maximum de 200 pour des échantillons de 20 tanks, et supposons que theta soit égal à 2000.
# Cela pourrait être vrai que l'on n'ait capturé des tanks présents dans les 200 premiers sortis de l'usine. Cependant c'est peu probable ie. on a plus de chances d'observer un numéro de série supérieur à 200 s'il y a réellement 2000 tanks. Ainsi on est confiant que les allemands ont moins de 2000 tanks.

# On cherche ici une borne supérieure sur theta.
# On trace la droite donnant l'estimation de theta pour la valeur maximale observée sur la première boite avec n = 20.
# On voit que l'estimation de theta est en dessous de ce qu'on observe avec une probabilité de 25% quand theta vaut ... . Ainsi, basé sur notre ligne d'observation, on rejetterai l'hypothèse nulle que theta vaut ... avec une certitude de 75%, parce qu'il est peu probable que le nombre maximal de tanks soit aussi bas s'il y avait vraiment ... tanks. 
# Ainsi, pour n = 20 et pour le maximum de la première boîte, on peut dire que le nombre de tanks produit par les allemands est inférieur à ... avec une confiance de 75%.

# 2.2
# P(max <= k)
# k(k - 1)...(k - n + 1) / theta(theta - 1)...(theta - n + 1)
dunif.max <-
    function(x, k, n) {
        ifelse(x == k, 1, prod(k:(k - n + 1)) / prod(x:(x - n + 1)))
    }

values_n5 <- vector()
for (i in 100:400) {
    values_n5[i - 99] <- dunif.max(x = i, k = 100, n = 5)
}

values_n10 <- vector()
for (i in 100:400) {
    values_n10[i - 99] <- dunif.max(x = i, k = 100, n = 10)
}

# Affichage de la fonction de répartition comme fonction de theta pour n et k fixés:
# 95% du temps, le nombre total de tanks sera inférieur à environ 180 pour un maximum des observations k = 100 et n = 5 tanks.
print(
    ggplot(data.frame(y = values_n5, x = 100:400), aes(x, y)) + geom_point() +
        theme_minimal() + ylab("Fonction de répartition du maximum des observations") + xlab("theta") + geom_hline(aes(yintercept = .05), lty = 3)
)

# Avec 5 tanks supplémentaires capturés, on s'attend à ce que le nombre de tanks soit inférieur à environ 135 95% du temps.
# Augmenter la taille de l'échantillon donne une estimation plus précise de theta.
# On peut estimer theta en prenant la médiane de cette distribution. Ce n'est pas la meilleur estimation.
print(
    ggplot(data.frame(
        y = values_n5, y1 = values_n10, x = 100:400
    ), aes(x, y)) +
        geom_point() + geom_point(aes(x, y1), color = "gray") + theme_minimal() +
        ylab("Fonction de répartition du maximum des observations") + xlab("theta") + geom_hline(aes(yintercept = .05), lty = 3)
)

# P(max = k)
unif.max <- function(x, k, n) {
    choose(k - 1, n - 1) / choose(x, n)
}

values <- vector()
for (i in 100:400) {
    values[i - 99] <- unif.max(i, k = 100, n = 5)
}
# La valeur de theta qui maximise la probabilité est le maximum k de l'échantillon. 100 est certainement une valeur sous-estimée de theta. En effet, cet estimateur est biaisé.
print(
    qplot(y = values, x = 100:400) + geom_line() + theme_minimal() + ylab("Probabilité que le maximum soit égal à k") + xlab("theta")
)
