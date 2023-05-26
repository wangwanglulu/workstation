from matplotlib import pyplot as plt
from wordcloud import WordCloud

filename = 'sanguo.txt'
with open(filename , encoding="utf-8") as f_obj:
    contents = f_obj.read()


font = r'C:\Windows\Fonts\simkai.ttf'

wc = WordCloud(font_path=font, #如果是中文必须要添加这个，否则会显示成框框
               background_color='white',
               width=1000,
               height=800,
               ).generate(contents)
wc.to_file('ss.png') #保存图片
plt.imshow(wc)  #用plt显示图片
plt.axis('off') #不显示坐标轴
plt.show() #显示图片