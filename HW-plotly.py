#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 21:29:56 2018

@author: AppleMoony
"""

import numpy as np
import json
import plotly
import plotly.plotly as py
import plotly.graph_objs as go


plotly.tools.set_credentials_file(username='xiaoruyue1986', api_key='7CcIFG2wXVzjVaL6nFVn')
py.sign_in('xiaoruyue1986', '7CcIFG2wXVzjVaL6nFVn') 

with open('Number of California Bridges Built by Year Since 1940.json') as F:
    dd = json.load(F)
   
x=dd['data'][0]['x']
x.sort()
#x
x=x[4: -2]
x
x=np.asarray(x)
#x.dtype
unique, counts = np.unique(x, return_counts=True)

np.asarray((unique, counts)).T
cumsum = np.cumsum(counts)
cumsum

trace = go.Scatter(x=unique, y=cumsum, marker=dict(color='orange'),
                  fill='tonexty',
                  mode='lines'
                 )
layout = go.Layout(title="Total Bridges Built in CA since 1900",
    autosize=False,
    width=600,
    height=400,
    xaxis= dict(
        title= 'Year',
        range=[1900, 2010],
        dtick=10,
    ),
    yaxis=dict(
        title= 'Total Bridges',
        ticklen= 5,
        gridwidth= 2,
    ),
    font=dict(
        family="Times New Roman"
    ),)

fig = go.Figure(data=go.Data([trace]), layout=layout)
py.iplot(fig, filename='Total Bridges Built in CA since 1900')
py.image.save_as(fig, filename='Total Bridges Built in CA since 1900.png', scale=3)