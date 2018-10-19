# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 00:23:14 2018

@author: 47532
"""

import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import re


crime = pd.read_csv('Dataset2-Crime_type_in_MD_with_lat_lng.csv')
crime_clean = crime.iloc[:,[7,8,15]]
text = ' '
crime_clean['crime_info'] = crime_clean.iloc[:,0] + ' '+ crime_clean.iloc[:,1] + ' ' + crime_clean.iloc[:,2]
crime_clean = crime_clean.dropna(subset = ['crime_info'])
for i in range(len(crime_clean)):
    line = crime_clean.iloc[i,3].lower()
    line = re.sub('[\=\s+\.\!\?\;\,\/\\\_\。\$\%^*(+\"\:\-\@\#\&\|\[\]\<\>)]+', " ", line)
    text = text + ' ' + line                                              

stopwords = set(STOPWORDS) 
wordcloud = WordCloud(width = 1080, height = 720, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(text)
plt.figure(figsize=(20,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('wordcloud.png', bbox_inches='tight')