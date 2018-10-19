# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:41:02 2018

@author: 47532
"""
import pandas as pd
df4 = pd.read_csv("Dataset4-Violent_Crime_Property_Crime_Statewide_Totals_1975_to_Present.csv")
df4.rename(columns={'M/V THEFT PER 100,000 PEOPLE':'MotorVehicle Theft', 
                   'LARCENY THEFT PER 100,000 PEOPLE':'Larceny Theft',
                   'B & E PER 100,000 PEOPLE':'B&E',
                   'AGG. ASSAULT PER 100,000 PEOPLE':'Aggregrated Assult',
                   'ROBBERY PER 100,000 PEOPLE':'Robbery',
                   'RAPE PER 100,000 PEOPLE':'Rape',
                   'MURDER PER 100,000 PEOPLE': 'Murder'}, inplace=True)

sub = df4[['Murder', 'Rape', 'Robbery', 'Aggregrated Assult', 'B&E', 'Larceny Theft', 'MotorVehicle Theft']]
sub['year'] = list(range(1975, 2017))
sub_year = sub.copy()
sub = pd.melt(sub, id_vars=['year'], value_vars=['Murder', 'Rape', 'Robbery', 'Aggregrated Assult', 'B&E', 'Larceny Theft', 'MotorVehicle Theft'])
sub["type"] = "" 
sub.loc[(sub["variable"] == "Murder") | (sub["variable"] == "Rape") | (sub["variable"] == "Aggregrated Assult") | (sub["variable"] == "Robbery"), 'type'] = "Voilent"
sub.loc[(sub["variable"] == "MotorVehicle Theft") | (sub["variable"] == "B&E")  | (sub["variable"] == "Larceny Theft"), 'type'] = "Property"

import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize = (10,10))
ax = sns.boxplot(x="variable", y="value", hue="type", data=sub, palette="muted")
plt.title('Distributon of Violent Crime and Property Crime')
plt.show()