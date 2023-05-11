import json
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)  
date=[]; close=[]; months=[]
for btc_dict in btc_data:
    date.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    close.append(int(float(btc_dict['close'])))

from itertools import groupby
import matplotlib.pyplot as plt
 
xy_map = []
for x, y in groupby(sorted(zip(months, close)), lambda w: w[0]):  
    y_list = []
    for first, second in y:
        y_list.append(second)
    xy_map.append([x, sum(y_list) / len(y_list)])  
    x_unique, y_mean = zip(*xy_map) 


fig, ax = plt.subplots()
plt.style.use('seaborn')
ax.plot(x_unique, y_mean, linewidth=1)
ax.scatter(x_unique, y_mean, s=20)
ax.set_title(u'收盘价',fontsize=10)
 
plt.savefig('close.jpg',dpi=300)