print("简易记账本（三月）")
March=[]
for date in range(20210301,20210332):
    March.append([date])
print()

while True:
    day=input("请问要输入几号的开销？如果结束请输入ok: ")
    if day=="ok":
        break
    else:
        print("请输入每一笔开销，结束请输入ok")
        expense=[]
        n=1
        while n!=0:
            each = input("第"+str(n)+"笔:")
            if each == "ok":
                n=0
            else: 
                expense.append(float(each))
                n=n+1
            print("记录成功")

        March[int(day)-1].append(sum(expense))

expense_total=0
for each_day in March:
    if len(each_day) == 2:
        expense_total = expense_total + each_day[1]

print()
print("本月支出汇总报告")
print("总支出：" + str(expense_total))






