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

from datetime import datetime

date, close_p = [], []
for y in data:
    date.append(datetime.strptime(y[0],"%Y%m%d"))
    close_p.append(y[2])

fig, ax = plt.subplots()
ax.plot(date,close_p, linewidth=0.5)
ax.scatter(date,close_p, s=5)
fig.autofmt_xdate()
plt.savefig('maotai.jpg',dpi=300)
