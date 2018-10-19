# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 16:34:44 2018

@author: 47532
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

df5 = pd.read_csv("Dataset5-Violent_Crime_Property_Crime_by_County_1975_to_Present.csv")
dates = df5['YEAR']
date_split = dates.apply(lambda x: time.strptime(x, "%m/%d/%Y %I:%M:%S %p"))  
df5['YEAR'] = date_split.apply(lambda x: time.strftime("%Y", x ))
df5.loc[(df5["JURISDICTION"] == "Allegany County "), 'JURISDICTION'] = "Allegany County"
df5.loc[(df5["JURISDICTION"] == "Anne Arundel County "), 'JURISDICTION'] = "Anne Arundel County"
df_bubble = df5[['YEAR', 'POPULATION', 'JURISDICTION', 'PROPERTY CRIME PERCENT', 'VIOLENT CRIME PERCENT']]
df_bubble['PROPERTY CRIME PERCENT'] = [float(x.strip('%')) for x in df_bubble['PROPERTY CRIME PERCENT']]
df_bubble['VIOLENT CRIME PERCENT'] = [float(x.strip('%')) for x in df_bubble['VIOLENT CRIME PERCENT']]
l = df_bubble['YEAR'].unique()[0::14]
df_bubble = df_bubble[(df_bubble['YEAR'] == l[0]) |
                    (df_bubble['YEAR'] == l[1]) | 
                    (df_bubble['YEAR'] == l[2])]

sns.set(font_scale=1.7)
g = plt.figure()
sns.relplot(x="PROPERTY CRIME PERCENT", y="VIOLENT CRIME PERCENT", size="POPULATION",
        sizes=(100, 900), 
        col ="YEAR", data=df_bubble).set_titles("Population v.s. Crime Type in {col_name}")