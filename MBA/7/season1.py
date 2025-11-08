from pathlib import Path
import json
from textblob import TextBlob
path = Path('season1.json')
contents = path.read_text()          # 读取整个文件为一个字符串
x = json.loads(contents)   
total = []     # 按行拆分，每一行是一个独立的 JSON 对象字符串
for m, n in x["Game Of Thrones S01E01 Winter Is Coming.srt"].items():
    total.append(n)
scores=[]
for line in total:
    polarity = TextBlob(line).sentiment.polarity
    scores.append(polarity)
if scores:
    average = sum(scores)/len(scores)
print(average)