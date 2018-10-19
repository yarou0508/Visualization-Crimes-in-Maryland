require(ggplot2)
require(plyr)
require(reshape2)

test <- read.csv('Dataset6-Law Enforcement.csv')
name <- test$County

test <- melt(subset(test, select = -c(Population, Total.law.enforcement.employees, Total.officers, Total.civilians)), id=c("County"))

test$County <- factor(test$County, levels = rev(name))
ggplot(data=test,aes(x = County, fill = variable)) + 
ggtitle("Pyramid Chart of County Law Enforcement Employees Rate in 2016") +
geom_bar(aes(y = value), data = test[test$variable == 'OfficerRate', ], stat = 'identity') + 
geom_bar(aes(y = -value), data = test[test$variable == 'CivilianRate',], stat = 'identity') + 
scale_y_continuous(breaks = seq(-2, 2, 1), 
                     labels = paste0(as.character(c(2, 1, 0, 1, 2)), "*10^(-3)")) +
scale_fill_brewer(palette = "Set2") + 
coord_flip()
