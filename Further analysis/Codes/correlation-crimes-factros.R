setwd("C:/Users/47532/Desktop/503Visualization/Project/project2")
library(gclus)
dta <- read.csv('crimes_factors.csv')
dta <- dta[,c(2:7)]
dta.r <- abs(cor(dta[,unlist(lapply(dta, is.numeric))]))
dta.col <- dmat.color(dta.r)
dta.o <- order.single(dta.r) 
cpairs(dta, dta.o, panel.colors=dta.col, gap=.5,
      main="Relationship between crimes and some factors", cex.labels=1.5)
