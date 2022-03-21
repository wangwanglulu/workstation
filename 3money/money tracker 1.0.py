print("简易记账本（三月）")
March=[]
for date in range(31):
    March.append([])

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
                March[day-1].append(each)
                n = n + 1
            print("记录成功")


total=0
for each_day in March:
    if each_day:
        total = total + sum(each_day)

print("本月支出汇总报告")
print("总支出：" + str(total))







