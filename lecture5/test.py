

# 1. 加载成语词典
filename = 'idiom_dictionary.txt'
with open(filename, encoding="utf-8") as file_object:
    lines = file_object.readlines()  # List

# 谐音取词
# 修改第一步
import unicodedata
d_game={}
for line in lines:
    if line!="\n":
        endpoint=line.find("拼音")
        idiom=line[:endpoint].strip()
        pinyin_start=line.find("：", endpoint)
        pinyin_end=line.find("释义")
        each=line[pinyin_start+1: pinyin_end]
        each=unicodedata.normalize('NFKD',each).encode('ascii','ignore').decode()
        pinyin_list=each.split()
        d_game[idiom]=pinyin_list
        
# 2. 给定一个成语，找到可以接上的所有成语
idiom = input("请输入第一个成语\n")
char_4th = d_game[idiom][-1]
for x, y in d_game.items():
    if char_4th == y[0]:
        print(x)

'''
idiom = input("请输入第一个成语\n")
enter = ""
exist = True
while enter != "q" and exist:  
    char_4th = d_game[idiom][-1]
    for x, y in d_game.items():
        if char_4th == y[0]:
            print(x)
            idiom = x
            exist = True
            break
        else:
            exist = False
    if exist == True:
        enter = input('continue?\n')
    else:
        print('没有成语了')

'''