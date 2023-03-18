# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 10:05:33 2022

@author: Lu
"""
import json
 
filename = 'lottery.json' 
with open(filename) as f:
    data = json.load(f)
    
# 1. Collect the 5 numbers
five_number=[]
for x in data:
    position=x[1].find('-')
    string_5=x[1][:position]
    list_5=string_5.split()
    five_number.append(list_5)
    
# 2. Frequencies
d={}
for x in five_number:
    for y in x:
        d[y]=d.get(y,0)+1
        
# 3. Sort and display
fre=[]
for x,y in d.items():
    fre.append([y,x])
fre.sort()
for x in fre:
    print(x)