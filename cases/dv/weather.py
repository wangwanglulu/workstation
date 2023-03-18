import requests
url = "http://wthrcdn.etouch.cn/weather_mini?citykey=101070101"
r = requests.get(url)
print(r.status_code)

response_dict = r.json()
f = response_dict['data']
ff = f['forecast']
ff_today = ff[0]
ff_1 = ff[1]
ff_2 = ff[2]
ff_3 = ff[3]
ff_4 = ff[4]
def show(day):
	for x in day:
		print(x +': ' + str(day[x]))
	print('\n')
show(ff_today)
show(ff_1)
show(ff_2)
show(ff_3)
show(ff_4)