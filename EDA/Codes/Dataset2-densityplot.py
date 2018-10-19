# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:39:05 2018

@author: 47532
"""
import pandas as pd
import time
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date

crime = pd.read_csv('Dataset2-Crime_type_in_MD_with_lat_lng.csv')
#Remove columns with useless information in Crime data.
crime_clean = crime.iloc[:,[3,5,6,20,21]]
# 补齐crime time,通过三个time column相互补充
for i in range(len(crime_clean)):
    if (crime_clean.iloc[i,3] == 'nan') & (crime_clean.iloc[i,4] != 'nan'):
        crime_clean.iloc[i,3] = crime_clean[i,4]
    elif (crime_clean.iloc[i,3] == 'nan') & (crime_clean.iloc[i,0] !='nan'):
        crime_clean.iloc[i,3] = crime_clean[i,0]
# There are 124105 crimes data
dates = crime_clean.iloc[:,3]
# After cleaning nan, there are 122153 crimes have time
dates = dates.dropna() 
crime1 = pd.DataFrame(dates)

date_split = dates.apply(lambda x: time.strptime(x, "%m/%d/%Y %I:%M:%S %p"))   
crime1['month'] = date_split.apply(lambda x: time.strftime("%m", x ))
crime1['day'] = date_split.apply(lambda x: time.strftime("%d", x ))
crime1['year'] = date_split.apply(lambda x: time.strftime("%Y", x ))
crime1['hour'] = date_split.apply(lambda x: time.strftime("%H", x ))

crime1.loc[crime1['month'].isin(['12','01','02']), 'season'] = 0
crime1.loc[crime1['month'].isin(['03','04','05']), 'season'] = 1
crime1.loc[crime1['month'].isin(['06','07','08']), 'season'] = 2
crime1.loc[crime1['month'].isin(['09','10','11']), 'season'] = 3

crime1['weekday'] = 'nan'
for i in range(len(crime1)):
    crime1.iloc[i,6] = date(int(crime1.iloc[i,3]), int(crime1.iloc[i,1]), int(crime1.iloc[i,2])).weekday() + 1

crime_2016 = crime1[crime1['year']=='2016']
crime_2017 = crime1[crime1['year']=='2017']
crime_2018 = crime1[crime1['year']=='2018']

plot1 = sns.jointplot(x='weekday', y='hour', data=crime_2016, kind="kde").set_axis_labels("Day of Week (2016)", "Time of Day",size = 20)
plot2 = sns.jointplot(x='weekday', y='hour', data=crime_2017, kind="kde").set_axis_labels("Day of Week (2017)", "Time of Day",size = 20)
plot3 = sns.jointplot(x='weekday', y='hour', data=crime_2018, kind="kde").set_axis_labels("Day of Week (2018)", "Time of Day",size = 20)

# subplots migration
f1 = plt.figure()
for plot in [plot1,plot2,plot3]:
    for A in plot.fig.axes:
        f1._axstack.add(f1._make_key(A), A)
#subplots size adjustment
f1.axes[0].set_position([0.1, 0.1, 0.8,  0.8])
f1.axes[1].set_position([0.1, 0.9, 0.8,  0.1])
f1.axes[2].set_position([0.9, 0.1, 0.1, 0.8])
f1.axes[3].set_position([1.2, 0.1, 0.8,  0.8])
f1.axes[4].set_position([1.2, 0.9, 0.8,  0.1])
f1.axes[5].set_position([2.0, 0.1, 0.1, 0.8])
f1.axes[6].set_position([2.3, 0.1, 0.8,  0.8])
f1.axes[7].set_position([2.3, 0.9, 0.8,  0.1])
f1.axes[8].set_position([3.1, 0.1, 0.1, 0.8])
f1.suptitle('Crime distribution through day of week & time of day in 2016,2017,2018', fontsize=30, x=1.5, y=1.7)
      

plot4 = sns.jointplot(x='season', y='month', data=crime_2016, kind="kde").set_axis_labels("Season", "Month",size = 20)
plot5 = sns.jointplot(x='season', y='month', data=crime_2017, kind="kde").set_axis_labels("Season", "Month",size = 20)
plot6 = sns.jointplot(x='season', y='month', data=crime_2018, kind="kde").set_axis_labels("Season", "Month",size = 20)
# subplots migration
f2 = plt.figure()
for plot in [plot4,plot5,plot6]:
    for A in plot.fig.axes:
        f2._axstack.add(f2._make_key(A), A)
#subplots size adjustment
f2.axes[0].set_position([0.1, 0.1, 0.8,  0.8])
f2.axes[1].set_position([0.1, 0.9, 0.8,  0.1])
f2.axes[2].set_position([0.9, 0.1, 0.1, 0.8])
f2.axes[3].set_position([1.2, 0.1, 0.8,  0.8])
f2.axes[4].set_position([1.2, 0.9, 0.8,  0.1])
f2.axes[5].set_position([2.0, 0.1, 0.1, 0.8])
f2.axes[6].set_position([2.3, 0.1, 0.8,  0.8])
f2.axes[7].set_position([2.3, 0.9, 0.8,  0.1])
f2.axes[8].set_position([3.1, 0.1, 0.1, 0.8])
f2.suptitle('Crime distribution through season & month in 2016,2017,2018', fontsize=30, x=1.5, y=1.7)
