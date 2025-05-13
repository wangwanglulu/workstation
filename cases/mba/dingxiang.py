import os
import re
import pypandoc
import requests
from bs4 import BeautifulSoup

# 爬取搜索结果
keywords="粗粮"
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/70.0.3538.25 \
        Safari/537.36 Core/1.70.3823.400 \
        QQBrowser/10.7.4307.400'}
params ={"query":keywords}
r=requests.get("https://dxy.com/search/result", \
                 params=params,headers=headers)
print(r.status_code)

# 解析搜索结果网页，
soup=BeautifulSoup(r.content, 'lxml')
list_a = soup.find_all(attrs={"class":"content-title-more common-text-link"})
all_url = list_a[0]["href"]

# 打开“查看更多”并且获取内容
r_all = requests.get(all_url)
soup_all = BeautifulSoup(r_all.content, 'lxml')
content_list = soup_all.find_all(attrs={"class":"article-title"})
print(content_list[0])

# 不停的翻页获取所有文章的链接，并提取文章的名字
num = 1
pag=1
article_url = []
article_title = []
while pag:
    params_page={"page_index":str(num)}
    r_all = requests.get(all_url,params=params_page,headers=headers)
    soup_all = BeautifulSoup(r_all.content, 'lxml')
    pag = soup_all.find_all(attrs={"class":"pagination"})
    content_list = soup_all.find_all(attrs={"class":"article-title"})
    for i in range(len(content_list)):
        article_url.append(content_list[i]["href"])
        article_title.append(content_list[i].contents[0].string)
    num = num+1

# 创建装文件的文件夹，之后所有文章都会下载到这里
folder = 'dingxiang_'+keywords
exist=os.path.exists(folder) 
if not exist:
    os.mkdir(folder)
os.chdir(folder)

# 因为文章名带有特殊符号，所以提取有效文字，做成word文件名
# 最后保存每篇文章为word文件
for j in range(len(article_url)):
    url = article_url[j]
    title = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])",
                   "",article_title[j])+'.docx'
    output = pypandoc.convert_file(url,'docx','html',outputfile=title) 
os.chdir('..')