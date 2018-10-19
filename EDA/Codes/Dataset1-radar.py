# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 16:09:10 2018

@author: 47532
"""

import pandas as pd

xl = pd.ExcelFile("Dataset1-maryland_4area_crime.xls")
df = xl.parse()
df.columns = ['Area','population','vio_cri','Murder', 'Rape', 'Robbery', 'Aggravated Assault', 'prop_cri',
                'Burglary', 'Larceny Theft', 'Motor Vehicle Theft']

df = df.drop(['vio_cri', 'prop_cri'], axis=1)

df_norm = df.T.rename(columns=df.T.iloc[0]).drop(['Total number', 'Rate per 100,000 inhabitant'], axis = 1).iloc[1:]
df_norm = df_norm.iloc[1:]

df_norm['Metropolitan Statistical Area'] = 10000 * df_norm['Metropolitan Statistical Area'] / 5901111.0 
df_norm['Cities outside metropolitan areas'] = 10000 * df_norm['Cities outside metropolitan areas'] / 52511.0
df_norm['Nonmetropolitan counties'] = 10000 * df_norm['Nonmetropolitan counties'] / 98555.0
df_norm = df_norm.T
df_norm['Area'] = df_norm.index
df_norm = df_norm.reset_index(drop=True)
df_norm_3 = df_norm.drop(['Larceny Theft', 'Murder', 'Rape', 'Burglary'], axis = 1)

df_norm.drop(['Area', 'Larceny Theft', 'Murder', 'Rape', 'Burglary'], axis = 1).T.to_csv('chi_df.csv')
#%% ===================================plot1============================= 
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
 
# ------- PART 1: Define a function that do a plot for one line of the dataset!
 
def make_spider(row, title, color):
    print('hey')
    # number of variable
    # Ind1
    values=df_norm.loc[row].drop(['Area']).values.flatten().tolist()
    print(sum(values))
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid', label = df['Area'][row])
    ax.fill(angles, values, color=color, alpha=0.4)
 
# initialize the figure
plt.figure(figsize=(5, 5), dpi=800)

categories=['Murder', 'Rape', 'Robbery', 'Aggravated assault', 'Burglary', 'Larceny theft', 'Motor vehicle theft']
N = len(categories)

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialise the spider plot
ax = plt.subplot(111, polar=True,)

# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories, color='grey', size=8)

ylim = 300#sum(df.loc[row].drop(['Area']).values.flatten().tolist())
# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([ylim*0.25, 
           ylim*0.5,
           ylim*0.75], 
           [str(ylim*0.25),
            str(ylim*0.5), 
            str(ylim*0.75)], color="grey", size=7)

plt.ylim(0, ylim)

# Create a color palette:
my_palette = plt.cm.get_cmap("Set2", len(df_norm.index))
# Loop to plot
for row in range(0, 3):
    make_spider(row=row, title='Crime distribution: ' + df_norm['Area'][row]+' (Below)', color=my_palette(row))
    
plt.title('Crime Type Distribution (per 10,000 Persons) Across Three Community Types', size=11, y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.show()

 #%% ===================================plot2============================= 
# ------- PART 1: Define a function that do a plot for one line of the dataset!
 
def make_spider3( row, title, color):
    print('hey')
    # number of variable
    # Ind1
    values=df_norm_3.loc[row].drop(['Area']).values.flatten().tolist()
    print(sum(values))
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid', label = df['Area'][row])
    ax.fill(angles, values, color=color, alpha=0.4)
 
# initialize the figure
plt.figure(figsize=(5, 5), dpi=800)

categories=['Robbery', 'Aggravated assault', 'Motor vehicle theft']
N = len(categories)

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialise the spider plot
ax = plt.subplot(111, polar=True,)

# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories, color='grey', size=8)

ylim = 100#sum(df.loc[row].drop(['Area']).values.flatten().tolist())
# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([ylim*0.5*0.25, 
           ylim*0.5*0.5,
           ylim*0.5*0.75], 
           [str(ylim*0.5*0.25),
            str(ylim*0.5*0.5), 
            str(ylim*0.5*0.75)], color="grey", size=7)

plt.ylim(0, ylim*0.5)

# Create a color palette:
my_palette = plt.cm.get_cmap("Set2", len(df_norm_3.index))
# Loop to plot
for row in range(0, 3):
    make_spider3(row=row, title='Crime distribution: ' + df_norm_3['Area'][row]+' (Below)', color=my_palette(row))
    
plt.title('Crime Type Distribution (per 10,000 Persons) Across Three Community Types', size=11, y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.show()
