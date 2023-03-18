# Step 1: Create a list containing dictionaries
print("简易记账本（三月）")
Month = []
for date in range(31):
    Month.append({}) 

# Step 2: Require Users to enter the date
while True:
    day = int(input("请问输入几号的开销？结束请输入0:\n"))
    if day == 0:
        break
    else:
        #Step 3: Enter the expenses one by one
        print("请输入每一笔开销，结束请输入0:\n") 
        while True:
            each = float(input("请输入金额:\n"))
            if each == 0:
                break
            else: 
                type = input("请选择类型: a.衣 b.食 c.住 d.行 e.其他\n")
                Month[day-1][type] = Month[day-1].get(type,0) + each
                print("记录成功\n")

# Report 
total=0
for each_day in Month:
    if each_day:
        total = total + sum(each_day.values())
print("总支出：", total)

sub = {}
category = ['a', 'b', 'c', 'd', 'e']
for z in category:
    for each_day in Month:
        sub[z] = each_day.get(z,0)+sub.get(z,0)

print("衣：", sub['a']) 
print("食：", sub['b']) 
print("住：", sub['c']) 
print("行：", sub['d']) 
print("其他：", sub['e'])   


