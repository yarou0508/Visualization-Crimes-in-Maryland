install.packages("reshape2") 
library(reshape2)
library(ggplot2)
setwd("C:/Users/47532/Desktop/503Visualization/Project/Datasets")
# Load Crime data and map data
Crime<-read.csv('Dataset3-Crime_in_US.csv')
# Select useful columns
sub_crime1 <- Crime[,-c(2,3,5,7,8,9,11,13,15,17,19,21)]
colnames(sub_crime1)<-c('year','violent','murder','rape','robbery','agg.assault','property','burglary','larceny','motorvehicle')
# Normalize dataset
crime_norm <- as.data.frame(apply(sub_crime1[, -1], 2, function(x) (x - min(x))/(max(x)-min(x))))
crime_norm$year <- sub_crime1$year
# Convert dataset into long dataset
crime_new1 <- melt(crime_norm, id=c("year"))

p5 <- ggplot(crime_new1, aes(x = year, y = value, group = 1))
p5 + geom_line() +
    facet_wrap(~variable, ncol = 5) +
  theme(axis.text.x =
          element_text(size  = 10,
                       angle = 45,
                       hjust = 1,
                       vjust = 1)) +
  labs(x="Year", y="Crime rate", title="Crime rate per 100,000 civilians after normalization") +
  theme(axis.text.x = element_text(size  = 10,
                       angle = 45,
                       hjust = 1,
                       vjust = 1))

# Select useful columns
sub_crime2 <- Crime[,c(1,2,3,15)]
colnames(sub_crime2)<-c('year','population','violent_crime','property_crime')
sub_crime2$total_crime <- sub_crime2$violent_crime + sub_crime2$property_crime
write.csv(sub_crime2,'sub_crime2.csv')
# Convert dataset into long dataset
crime_new2 <- melt(sub_crime2, id=c("year"))
write.csv(crime_new2,'crime_new2.csv')

# sub_crime2$pred.SC <- predict(lm(total_crime ~ year, data = sub_crime2))
# ggplot(sub_crime2,
#        aes(y = total_crime, x = year)) +
#   geom_point(aes(color = total_crime)) +
#   geom_smooth() + geom_line(aes(y = pred.SC))


