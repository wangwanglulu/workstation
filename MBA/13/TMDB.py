import requests
from pathlib import Path

api_access = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ZWMzMDlmYWZjMjM4NjdmZmViNzRjMjZjN2E4YTU3OSIsIm5iZiI6MTczMjQxMTUwMy40OTM0MjMsInN1YiI6IjVkNTBmMDk5MDEwMmM5Mjc2ZDc0ZTI5OSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.i5Gpj1yc_9I7JarSzgoBcI2uWKOd3W0wiftwwOIFYak"

page = 1
url = f"https://api.tmdb.org/3/movie/\
now_playing?language=en-US&page={page}" #改成api.tmdb.org
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_access}"
}
response = requests.get(url, headers=headers)
response_dict = response.json()
 
movies=response_dict["results"]
top10 = movies[:10]

for movie in top10:
    poster = movie['poster_path']
    title = movie['title']
    img_url = f"https://image.tmdb.org/t/p/w500{poster}"
    r = requests.get(img_url, headers=headers)
    if r.status_code == 200:
        with open(f'{title}.jpg', 'wb') as f:
            f.write(r.content)
    else:
        print("download failed")
