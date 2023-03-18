# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 20:57:15 2018

@author: LU WANG
"""

import csv

filename = 'data.csv'

with open(filename, "r",  encoding = 'utf-8') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

complete_data = []
for xx in range(0,len(rows),2):
    complete_data.append(rows[xx]+rows[xx+1]) #因为date和其他数据是分离的,这一步合并

# print(complete_data) # 初始数据

info = []
for yy in complete_data:
    individual_info = []
    nn = yy[1].find('\\')
    mm = yy[4].find(' ')
    individual_info.append(yy[4][:mm])
    individual_info.append(yy[1][:nn])
    individual_info.append(yy[2])
    info.append(individual_info)
    
for s in info:
    print(s) #整理出来的数据
    
###########################################################
#############下面是饼状图###################################
###########################################################
carteen_info = []
for zz in info:
    carteen_info.append(zz[1])
print(carteen_info)
    
carteen = dict()
for cx in carteen_info:
    if cx not in carteen:
    	carteen[cx] = 1
    else: 
    	carteen[cx] = carteen[cx] +1
print(carteen)

name = []
count =[]
for x, y in carteen.items():
    name.append(x)
    count.append(y)

from matplotlib import pyplot as plt 
plt.rcParams['font.sans-serif']=['SimHei'] #中文乱码
plt.figure(figsize=(6,9)) #调节图形大小，宽，高
labels = name #定义饼状图的标签，标签是列表
sizes = count #每个标签占多大，会自动去算百分比

plt.pie(sizes,
        labels=labels,
        labeldistance = 1.1, #文本的位置离远点有多远，1.1指1.1倍半径的位置
        autopct = '%3.1f%%', #圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
        shadow = False, #饼是否有阴影
        startangle = 90, #起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
        pctdistance = 0.6) #百分比的text离圆心的距离

plt.axis('equal') # x，y轴刻度设置一致，保证饼图为圆形
plt.show()
