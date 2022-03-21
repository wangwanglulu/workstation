import unicodedata

# 1. 加载成语词典
filename = 'idiom_dictionary.txt'
with open(filename, encoding="utf-8") as file_object:
    lines = file_object.readlines() #List

d_game={}
for line in lines:
    if line!="\n":
        endpoint=line.find("拼音")
        idiom = line[:endpoint].strip()
        pinyin_start = line.find("：", endpoint)
        pinyin_end =line.find("释义")
        each= line[pinyin_start+1: pinyin_end]
        each = unicodedata.normalize('NFKD', each).encode('ascii','ignore').decode()
        pinyin_list = each.split()
        d_game[idiom] = pinyin_list
len(d_game)

# 2. 给定一个成语，找到可以接上的所有成语
idiom = input("请输入第一个成语\n")
char_4th = d_game[idiom][-1]
for x, y in d_game.items():
    if char_4th == y[0]:
        print(x)




"""
# 3. 从一个给定的成语开始，一直接下去，到不能接下去为止。
idiom = input("请输入第一个成语\n")
char_4th = d_game[idiom][-1]
enter=""
exist = True
while enter!="q" and exist:
    char_4th = d_game[idiom][-1]
    for x, y in d_game.items():
        if char_4th == y[0]:
            idiom = x
            print(idiom)
            exist = True
            break
        else:
            exist = False
    if exist:
        enter=input("continue?")
    else:
        print("对不起，没有成语了") 



#基本查释义功能
d_ex={}
for line in lines:
    if line!="\n":
        endpoint=line.find("拼音")
        x = line[:endpoint].strip()
        pinyin_end =line.find("释义")
        pinyin_start = line.find("：", endpoint)
        y = line[pinyin_end:]
        d_ex[x]=y
words=input("请输入要查询的词语\n")
print(d_ex[words])

"""