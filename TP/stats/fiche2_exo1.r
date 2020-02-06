x <- rnorm(1000, mean=2)
# hist(x)

# Compute the density data
# dens <- density(x)
# plot density
# plot(dens) 

# Superpose histogram and density plot
histdens <- function(x, histogram, xlim=NULL, ...)
{
  h <- histogram
  xfit <- seq(min(x), max(x), length=1000)
  yfit <- dnorm(xfit, mean=mean(x),sd=sd(x))
  yfit <- yfit * diff(h$mids[1:2]) * length(x)
  lines(xfit, yfit, col="blue", lwd=2)
}


# Stockage dans un vecteur
bruit <- c(54.8, 55.4, 57.7, 59.6, 60.1, 61.2, 62.0, 63.1, 63.5, 64.2, 65.2, 65.4, 65.9, 66.0, 67.6, 68.1, 69.5, 70.6, 71.5, 73.4)
summary(bruit)
# Standard Deviation, Variance, Coefficient de variation en %
sd(bruit)
var(buit)
sd(bruit)/mean(bruit)*100

classes <- nclass.Sturges(bruit)
hist(bruit)

# Classes de même largeur
histolarg <- function(x, xlim=NULL, ...)
{
  # nombre de donn?es
  n <- length(x) 
  # nombre de classes (r?gle de Sturges)
  if (n<12) k<-5 else k <- round(log2(n)+1) 
  # bornes des classes
  rangex <- max(x)-min(x)
  a0 <- min(x)-0.025*rangex
  ak <- max(x)+0.025*rangex
  bornes <- seq(a0, ak, length=k+1)
  # ?tendue du trac?
  if (is.null(xlim))
    xlim<-c(bornes[1], bornes[k+1])
  # histogramme
  histx<-hist(x, prob=T, breaks=bornes, xlim=xlim, ...)
  # histx
}
histolarg(bruit)

histoeff <- function(x, xlim=NULL, ...)
{
  sx <- sort(x)
  n <- length(x)
  k <- round(log(n)/log(2)+1)
  rangex <- max(x)-min(x)
  breaks <- c(min(x)-0.025*rangex, quantile(x, seq(1, k-1)/k), max(x)+0.025*rangex)
  col <- 0
  if (is.null(xlim)) xlim<-c(breaks[1], breaks[k+1])
  return(hist(x, breaks=breaks, col=col, xlim=xlim, probability=T, ...))
}

histoeff(bruit)
histdens(bruit, histoeff(bruit))

