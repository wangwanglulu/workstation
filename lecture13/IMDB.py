import requests

api_key = 'k_kvjck39o'

url=f"https://imdb-api.com/en/API/InTheaters/{api_key}"
r = requests.get(url)
print(r.status_code)
response_dict = r.json() 
 
in_theaters = response_dict["items"]
 
for movie in in_theaters:
    url = movie['image']
    title = movie['title']
    print(title)
 
    r = requests.get(url)
    if r.status_code == 200:
        with open(f'{title}.jpg', 'wb') as f:
            f.write(r.content)
    else:
        print("download failed")
