import unicodedata
import random

filename = 'idiom_dictionary.txt'
with open(filename, encoding="utf-8") as file_object:
    lines = file_object.readlines() #List

def load_dic():
# 1. 加载成语词典
    global d_game
    d_game = {}
    for line in lines:
        if line!="\n":
            endpoint=line.find("拼音")
            idiom = line[:endpoint].strip()
            pinyin_start = line.find("：", endpoint)
            pinyin_end =line.find("释义")
            each= line[pinyin_start+1: pinyin_end]
            #each = unicodedata.normalize('NFKD', each).encode('ascii','ignore').decode()
            pinyin_list = each.split()
            d_game[idiom] = pinyin_list

"""
# 2. 给定一个成语，找到可以接上的所有成语
idiom = input("请输入第一个成语\n")
char_4th = d_game[idiom][-1]
for x, y in d_game.items():
    if char_4th == y[0]:
        print(x)
"""

def computer(idiom):
    idiom_com_list = []
    char_4th = d_game[idiom][-1]
    for x, y in d_game.items():
        if char_4th == y[0]:
            idiom_com_list.append(x)

    if idiom_com_list:
        idiom_com = random.choice(idiom_com_list)
        print(idiom_com)
    else:
        idiom_com = ""
        print("没有成语了, 你赢了") 
    return idiom_com




def player(idiom_com):
    while True:
        idiom  = input("请接上, 认输请输入0")
        if idiom == "0":
            break
        if idiom in d_game:
            if d_game[idiom][0] == d_game[idiom_com][-1]:
                break
            else:
                print("该成语接不上, 请重新输") 
        else:
            print("词典里没有该成语，请换一个")
    return idiom

def main():
    load_dic()
    while True:
        idiom = input("请输入第一个成语\n")
        if idiom in d_game:
            break
        else:
            print("词典里没有该成语，请换一个")
    
    while idiom != "0":
        idiom_com = computer(idiom)
        if idiom_com:
            idiom = player(idiom_com)
        else:
            break
    print("Game Over")    

main()










