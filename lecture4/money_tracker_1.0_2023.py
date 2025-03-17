print("简易记账本(March)")
March = []
for date in range(31):
    March.append({}) 
while True:
    day = int(input("请问输入几号的开销？结束请输入0:\n"))
    if day == 0:
        break
    else:
        print("请输入每一笔开销，结束请输入0:\n") 
        while True:
            each = float(input("请输入金额:\n"))
            if each == 0:
                break
            else: 
                type = input("请选择类型: a.衣 b.食 c.住 d.行 e.其他\n")
                March[day-1][type] = March[day-1].get(type,0) + each
                print("记录成功\n")
total=0
for each_day in March:
    total += sum(each_day.values())
print("总支出：", total)

st = {}
category = ['a', 'b', 'c', 'd', 'e']
for type in category:
    for each_day in March:
        st[type] = each_day.get(type,0)+st.get(type,0)
print("衣：", st['a'], "食：", st['b']) 
print("住：", st['c'], "行：", st['d']) 
print("其他：", st['e'])   

