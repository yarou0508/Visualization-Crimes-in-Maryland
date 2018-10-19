# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:35:41 2018

@author: 47532
"""
import pandas as pd
df = pd.read_csv('Dataset4-Violent_Crime_Property_Crime_Statewide_Totals_1975_to_Present.csv')
#df.columns
Year = pd.to_datetime(df['YEAR']).dt.year
df['YEAR'] = Year
df1 = df[df['YEAR'] == 2016]
df1 = df1[['MURDER', 'RAPE', 'ROBBERY', 'AGG. ASSAULT', 'B & E', 'LARCENY THEFT', 'M/V THEFT']].T
df1.columns = ['']
df1.plot(y = '', kind = 'pie', colormap='Set2', figsize = (15, 15), title = 'Pie Chart of Crime Rate by Type')