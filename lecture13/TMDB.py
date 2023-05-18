import requests


api_access = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiN2JmNTExZGFmM2ZjMDY4NGEzNTQxNWJjM2MzZmZmZSIsInN1YiI6IjVkNTBmMDk5MDEwMmM5Mjc2ZDc0ZTI5OSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.n48HcsjdiXRSY4Xs8qFRtvy50P2W1sppZ5OaAMU_Rd0"
page = 1
url = f"https://api.themoviedb.org/3/movie/now_playing?language=en-US&page={page}"
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
