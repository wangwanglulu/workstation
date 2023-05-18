import requests
url = "http://t.weather.itboy.net/api/weather/city/101020100"
r = requests.get(url)
print(r.status_code)
response_dict = r.json()  
f = response_dict['data']
ff = f['forecast']
ff_today = ff[0]
ff_1 = ff[1]
ff_2 = ff[2]
def show(day):
    for x in day:
        print(x+': '+str(day[x]))
    print()
show(ff_today)
show(ff_1)
show(ff_2)
