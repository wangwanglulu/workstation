from pathlib import Path
from datetime import datetime
import json

path = Path('btc_close_2017.json')
contents = path.read_text()
btc_data = json.loads(contents)

date=[]; close=[]; months=[]

for btc_dict in btc_data:
    date.append(datetime.strptime(btc_dict['date'], "%Y-%m-%d"))
    months.append(int(btc_dict['month']))
    close.append(int(float(btc_dict['close'])))

import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(date,close, linewidth=0.5, c='red')
ax.scatter(date,close, s=5, c='red')
ax.set_title('Close',fontsize=10)
fig.autofmt_xdate()

plt.savefig('close.jpg',dpi=300)