import requests


api_access = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiN2JmNTExZGFmM2ZjMDY4NGEzNTQxNWJjM2MzZmZmZSIsInN1YiI6IjVkNTBmMDk5MDEwMmM5Mjc2ZDc0ZTI5OSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.n48HcsjdiXRSY4Xs8qFRtvy50P2W1sppZ5OaAMU_Rd0"

page = 1
url = f"https://api.themoviedb.org/3/movie/\
top_rated?page={page}"
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_access}"
}
response = requests.get(url, headers=headers)
response_dict = response.json()
# print(response_dict)

movies=response_dict["results"]
print(len(movies))
for key, value in movies[0].items():
    print(f"{key}: {value}")


from pathlib import Path
poster = movies[0]['poster_path']
title = movies[0]['title']
img_url = f"https://image.tmdb.org/t/p/w500{poster}"
r = requests.get(img_url, headers=headers)
if r.status_code == 200:
    save_path = Path(f"{title}.jpg")
    save_path.write_bytes(r.content)
else:
    print("download failed")




