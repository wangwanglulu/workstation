import requests
import matplotlib.pyplot as plt

url="http://img1.money.126.net/data/hs/kline/day/history/2022/0600519.json"
r = requests.get(url)
print(r.status_code)
response_dict = r.json() 
print(response_dict)

data = response_dict['data']

for x in data[:5]:
    print("""日期: {}，开盘价：{}，收盘价：{}，最高价：{}
        最低价：{}，交易量：{}，涨幅跌幅：{}""".format(x[0],\
        x[1], x[2], x[3], x[4], x[5], x[6]))
date=[]; open_p=[]; close_p=[]; high=[]
low=[]; volume=[]; percent=[]
for y in data:
    date.append(y[0]); open_p.append(y[1])
    close_p.append(y[2]); high.append(y[3])
    low.append(y[4]); volume.append(y[5])
    percent.append(y[6])

fig, ax = plt.subplots()

ax.plot(close_p, linewidth=0.5)
ax.scatter(date,close_p, s=5)
ax.set_xticks(date[::20])
ax.set_xticklabels(date[::20],rotation=45,fontsize=6)
ax.set_title('Maotai',fontsize=10)
#ax.tight_layout()
plt.savefig('maotai.jpg',dpi=300)