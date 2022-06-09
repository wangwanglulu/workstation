import datetime
import calendar
import json
import matplotlib.pyplot as plt


def main():
    control = True
    while control:
        menu()
        option = int(input("请选择？"))
        if option == 0:
            control =False
        elif option == 1:
            input_month()
        elif option == 2:
            insert()
        elif option == 3:
            report()
        elif option == 4:
            fig()


def menu():
    print(""" 
        ——————————————————简易记账本——————————————————
        =====================菜单====================
        
        1 选择年月 
        2 录入新的支出信息
        3 汇总报告
        4 绘制表格
        0 退出
        _____________________________________________
        """
       )

def insert():  
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
    filename = "{}-{}.json".format(year,month)
    with open(filename,"w") as f_obj:
        json.dump(March,f_obj)


def report():
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

def input_month():
    global March, year, month
    this_year = input("是今年吗？请选择：1.是 2.不是")
    if int(this_year)==1:
        today = datetime.date.today()
        year = today.year
    else:
        which_year = input("请输入四位年份数字")
        year = int(which_year)
    this_month = input("是本月吗？请选择：1.是 2.不是")
    if int(this_month)==1:
        today = datetime.date.today()
        month = today.month
    else:
        which_month = input("请输入月份数字：")
        month = int(which_month)
    try:
        filename =  "{}-{}.json".format(year,month)
        with open(filename) as f_obj:
            March = json.load(f_obj)
    except:
        month_range = calendar.monthrange(year,month)
        March = []
        for date in range(month_range[1]):
            March.append({})

def fig():
    consumption = []
    day = []
    for each_day in March:
        if each_day:
            consumption.append(sum(each_day.values()))
        else:
            consumption.append(0)
    day = list(range(1,len(consumption)+1))
    plt.style.use("seaborn")
    fig, ax = plt.subplots()
    ax.plot(day,consumption,c="red")
    ax.set_title("Daily Consumption {}-{}".format(year,month),fontsize=24)
    ax.set_xlabel("Day",fontsize=16)
    ax.set_ylabel("Consumption", fontsize=16)
    ax.tick_params(axis='both',which='major',labelsize=16)
    fig.savefig("{}-{}.jpg".format(year,month),dpi=300)


main()

