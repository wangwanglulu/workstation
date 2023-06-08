from wordcloud import WordCloud
import jieba
filename = 'sanguo.txt'
with open(filename, encoding="utf-8") as f_obj:
    contents = f_obj.read()
def sw(filename):
    with open(filename, encoding="utf-8") as f_obj:
        x = f_obj.readlines()
    y = [word.strip() for word in x]
    return y
name_list = ['baidu_stopwords.txt', 'cn_stopwords.txt', 
             'hit_stopwords.txt','scu_stopwords.txt']
stop_word = []
for x in name_list:
    stop_word.extend(sw(x))
stop_word = list(set(stop_word))
s = jieba.lcut(contents) 
result = [word for word in s if word not in stop_word]
s = [word for word in result if len(word)>1]
txt = " ".join(s)
#font = r'C:\Windows\Fonts\Arial.TTF'
font = "/System/Library/Fonts/STHeiti Medium.ttc"
wc = WordCloud(font_path=font, 
               background_color='white',
               width=1000,
               height=800,
               ).generate(txt)
wc.to_file('s5.png') 
