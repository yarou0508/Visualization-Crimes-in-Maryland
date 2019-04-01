# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:21:16 2018

@author: 47532
"""
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd


baltimore = pd.read_csv('baltimore-crimes-1975-present.csv')
montgomery = pd.read_csv('montgomery-crimes-1975-present.csv')

# For preperty crime
trace1 = go.Scatter(
        x = list(baltimore['Year']),
        y = list(baltimore['property_crime_rate']),
        name = 'Baltimore',
        mode = "lines+markers")
trace2 = go.Scatter(
        x = list(montgomery['Year']),
        y = list(montgomery['property_crime_rate']),
        name = 'Montgomery',
        mode = "lines+markers")


# For violent crime
trace1 = go.Scatter(
        x = list(baltimore['Year']),
        y = list(baltimore['violent_crime_rate']),
        name = 'Baltimore',
        mode = "lines+markers")
trace2 = go.Scatter(
        x = list(montgomery['Year']),
        y = list(montgomery['violent_crime_rate']),
        name = 'Montgomery',
        mode = "lines+markers")

data = [trace1, trace2]


layout = dict(
    title='Violent Crime Rate in Baltimore & Montgomery',
    xaxis=dict(
        rangeslider=dict(
            visible = True
        ),
        type='date'
    )
)


fig = dict(data=data, layout=layout)
py.iplot(fig, filename='plotly-slider-property-crime')
plotly.offline.plot(fig, filename = 'plotly-slider-property-crime.html')

py.iplot(fig, filename='plotly-slider-violent-crime')
plotly.offline.plot(fig, filename = 'plotly-slider-violent-crime.html')
