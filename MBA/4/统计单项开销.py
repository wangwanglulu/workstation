#统计单项开销

st = {}
category = ['a', 'b', 'c', 'd', 'e']
for type in category:
    for each_day in March:
        st[type] = each_day.get(type,0)+st.get(type,0)
        
print("衣：", st['a'], "食：", st['b']) 
print("住：", st['c'], "行：", st['d']) 
print("其他：", st['e'])   
