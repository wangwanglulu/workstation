import json

filename = 'lottery.json' 
with open(filename) as f:
    data = json.load(f)

five_number=[]
for x in data:
    position=x[1].find('-')
    string_5=x[1][:position]
    list_5=string_5.split()
    five_number.append(list_5)

d={}
for x in five_number:
    for y in x:
        d[y]=d.get(y,0)+1

fre=[]
for x,y in d.items():
    fre.append([y,x])
fre.sort()
for x in fre:
    print(x)