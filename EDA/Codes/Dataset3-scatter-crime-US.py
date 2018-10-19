# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 13:20:56 2018

@author: 47532
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
#%% ===================================R code for data cleaning ============================= 
Crime<-read.csv('Dataset3-Crime_in_US.csv')
# Select useful columns
sub_crime2 <- Crime[,c(1,2,3,15)]
colnames(sub_crime2)<-c('year','population','violent_crime','property_crime')
sub_crime2$total_crime <- sub_crime2$violent_crime + sub_crime2$property_crime
write.csv(sub_crime2,'sub_crime2.csv')

# Convert dataset into long dataset
crime_new2 <- melt(sub_crime2, id=c("year"))
write.csv(crime_new2,'crime_new2.csv')
#%% ===================================visualization============================= 
# Plot 1
crime = pd.read_csv('crime_new2.csv')
sns.set(style="darkgrid")
crime_total = crime[crime['variable']=='total_crime']
f = plt.figure(figsize=(14, 10))
sns.set(font_scale=2)
sns.regplot(x="year", y="value", data=crime_total).set(xlabel = "Year", ylabel= "Crime Rate")
f.suptitle('Total crime rate per 100,000 civilians in US from 1998-2017', fontsize=30, x=0.5, y=1)

# Plot 2
crime_2type = pd.read_csv('sub_crime2.csv')
violent_rate= crime_2type['violent_crime']/crime_2type['total_crime']
property_rate = crime_2type['property_crime']/crime_2type['total_crime']
crime_rate = pd.DataFrame(pd.concat([violent_rate, property_rate]),columns = ['crime_rate'])
crime_rate['year'] = crime.iloc[:40,1]
crime_rate['variable'] = crime.iloc[20:60,2].values

sns.set(font_scale=1.7)
p2 = sns.lmplot(x="year", y="crime_rate", data=crime_rate, col='variable',hue = 'variable',order = 4, sharex=False,sharey=False)
p2.set_titles("{col_name} Proportion")
p2.set_axis_labels("Year", "Crime Rate")





