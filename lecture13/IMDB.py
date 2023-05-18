import requests

api_key = 'k_kvjck39o'

url=f"https://imdb-api.com/en/API/Top250Movies/{api_key}"
r = requests.get(url)
print(r.status_code)
response_dict = r.json() 
top250 = response_dict["items"]
print(top250[0])


