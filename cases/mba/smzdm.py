import requests
import pandas as pd
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/70.0.3538.25 \
        Safari/537.36 Core/1.70.3823.400 QQBrowser/10.7.4307.400'}
data=[]
for page in range(1,6):
    params ={"p":page, "past_num":page*20}
    r=requests.get("https://www.smzdm.com/homepage/json_more", \
                    params=params, headers=headers)
    x = r.json()
    data = data + x['data']

title=[]; price=[]; date=[]; category=[]; atype=[]; mall=[]
for i in range(len(data)):
    if 'article_price' in data[i]:
        atype.append(data[i]['article_type'])   
        title.append(data[i]['article_title'])
        price.append(data[i]['article_price'])
        date.append(data[i]['article_date'])
        category.append(data[i]['top_category'])
        mall.append(data[i]['article_mall'])

