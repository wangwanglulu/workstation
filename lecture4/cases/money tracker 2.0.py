print("简易记账本（三月）")
March=[]
for date in range(31):
    March.append({})

while True:
    day=int(input("请问输入几号的开销？结束请输入0:"))
    if day==0:
        break
    else:
        print("请输入每一笔开销，结束请输入0:")
        n=1
        while True:
            each = float(input("第"+str(n)+"笔:"))
            if each == 0:
                break
            else: 
                y = input("请选择: a.衣 b.食 c.住 d.行 e.其他")
                March[day-1][y]=March[day-1].get(y,0)+each
                n = n + 1
            print("记录成功")

total=0
for each_day in March:
    if each_day:
        total = total + sum(each_day.values())

print("本月支出汇总报告")
print("总支出：" + str(total))

sub = {}
items = ['a', 'b', 'c', 'd', 'e']
for each_day in March:
    for z in items:
        sub[z] = each_day.get(z,0)+sub.get(z,0)
print("衣：", sub['a']) 
print("食：", sub['b']) 
print("住：", sub['c']) 
print("行：", sub['d']) 
print("其他：", sub['e'])   




