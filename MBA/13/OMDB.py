# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 22:29:25 2025

@author: Lu
"""

import requests
import pandas as pd
# 电影名称
title = "Inception"
url = f"https://www.omdbapi.com/?t={title}&apikey=7677a2d8"
# 发起 GET 请求
response = requests.get(url)
data = response.json()
print(data)   
# 选取想要的字段
movie_info = {
    "Title": data.get("Title"),
    "Year": data.get("Year"),
    "Runtime": data.get("Runtime"),
    "Genre": data.get("Genre"),
    "Director": data.get("Director"),
    "imdbRating": data.get("imdbRating"),
    "Plot": data.get("Plot")
}
# 映射到 DataFrame（适合进一步分析）
df = pd.DataFrame([movie_info])
print(df)