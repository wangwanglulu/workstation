#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 22:26:07 2023

@author: wangwanglulu
"""

import json

filename = 'data.json'
with open(filename, "r", encoding="utf-8") as f:
    data=json.load(f)
    fre = dict()
    for cx in data:
        if cx[1] not in fre:
            fre[cx[1]] = 1
        else:
            fre[cx[1]]+=1
name = []
count =[]
for x, y in fre.items():
    name.append(x)
    count.append(y)

# Visualize the results.

from plotly.graph_objs import Bar, Layout
from plotly import offline

data=[Bar(x=name,y=count)]
x_axis_config={'title': 'result'}
y_axis_config={'title': 'frequencies'}
my_layout=Layout(title='canteen',
xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='canteen.html')