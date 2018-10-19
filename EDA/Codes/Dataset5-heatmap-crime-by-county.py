# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:49:41 2018

@author: 47532
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df5 = pd.read_csv("Dataset5-Violent_Crime_Property_Crime_by_County_1975_to_Present.csv")
df5.loc[(df5["JURISDICTION"] == "Allegany County "), 'JURISDICTION'] = "Allegany County"
df5.loc[(df5["JURISDICTION"] == "Anne Arundel County "), 'JURISDICTION'] = "Anne Arundel County"

df_voilent = df5[['YEAR', 'JURISDICTION', 'VIOLENT CRIME PERCENT']]
df_voilent['VIOLENT CRIME PERCENT'] = [float(x.strip('%')) for x in df_voilent['VIOLENT CRIME PERCENT']]
table_violent = df_voilent.pivot(index='JURISDICTION', columns='YEAR',  values='VIOLENT CRIME PERCENT')
table_violent.columns = range(1975, 2017)
table_violent = table_violent.convert_objects(convert_numeric=True)
table_violent['sort'] = table_violent.mean(axis=1)
table_violent = table_violent.sort_values(by=['sort'], ascending = False)

df_property = df5[['YEAR', 'JURISDICTION', 'PROPERTY CRIME PERCENT']]
df_property['PROPERTY CRIME PERCENT'] = [float(x.strip('%')) for x in df_property['PROPERTY CRIME PERCENT']]
table_property = df_property.pivot(index='JURISDICTION', columns='YEAR',  values='PROPERTY CRIME PERCENT')
table_property.columns = range(1975, 2017)
table_property = table_property.convert_objects(convert_numeric=True)
table_property['sort'] = table_property.mean(axis=1)
table_property = table_property.sort_values(by=['sort'], ascending = True)

f1, (ax1,ax2) = plt.subplots(nrows=2, figsize=(15, 17))
sns.heatmap(table_violent, linewidths=.5, cmap = sns.cm.rocket_r, ax=ax1)
sns.heatmap(table_property, linewidths=.5, cmap="YlGnBu", ax=ax2)
ax1.set_title('Voilent Crime Percentage from 1975 to 2016')
ax2.set_title('Property Crime Percentage from 1975 to 2016')
