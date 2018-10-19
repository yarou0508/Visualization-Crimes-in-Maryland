# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:21:45 2018

@author: 47532
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Dataset7-Crime by State 2017.csv', header = 3)
state = df[(~df['State'].isnull()) & (df['State'].str.len() <= 21)]['State']
df1 = df[df['Area'].str.contains('Total') == True]
df1['State'] = state.str.replace('\d+', '').str.title().tolist()

for i in df1.columns:
    df1[i] = df1[i].str.replace(',', '')
df1['CrimeRate'] = (df1['Violent\ncrime1'].astype(int) + df1['Property \ncrime'].astype(int))/df1['Population'].astype(int)
df1['ViolentRate'] = df1['Violent\ncrime1'].astype(int)/df1['Population'].astype(int)
df1['PropertyRate'] = df1['Property \ncrime'].astype(int)/df1['Population'].astype(int)
index = df1['State'].tolist().index('Maryland')
plt.figure(figsize = (20, 10))
df1 = df1.sort_values(by=['CrimeRate'], ascending = False)
df1.set_index('State', inplace = True)
ind = np.arange(df1.shape[0])
p1 = plt.bar(ind, df1['ViolentRate'].tolist(), color='lightgray')
p2 = plt.bar(ind, df1['PropertyRate'].tolist(), bottom=df1['ViolentRate'].tolist(), color='lightblue')
p1[27].set_color('darkgray')
p2[27].set_color('dodgerblue')
plt.legend((p1[0], p2[0]), ('ViolentRate', 'PropertyRate'), fontsize = 18)
plt.ylabel('Proportion')
plt.title('Crime Rate by State in 2017', fontsize=30)
plt.xticks(ind, (df1.index), rotation='vertical')
