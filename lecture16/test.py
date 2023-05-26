from moviepy.editor import *
clip = VideoFileClip("ultraman.flv")
clip = clip.subclip(0, 8) #剪切前8秒
clip.write_gif("video.gif") #保存为gif

from PIL import Image
#将gif的每一帧保存为png图片到images文件夹
def get_imgs():
    gif = Image.open('video.gif')
    try:
        gif.save(f"images/{gif.tell()}.png")
        while True:
            gif.seek(gif.tell()+1)
            gif.save(f"images/{gif.tell()}.png")
    except Exception as e:
        print("finished")
get_imgs()

ASCII_CHAR = "$@B%8&WM#*oahkbdpqwmZO0QLaCJUYXzczjhdhsdavunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."        
def rgb_to_ascii(r, g, b, alpha=256): 
    # 通过灰度值的映射
    # 将没一个rgb值对应成一个ascii符
    # 也就实现了rgb -> ascii
    # 当像素透明时，直接返回一个空白字符串
    if alpha == 0:
        return ' '
    length = len(ASCII_CHAR)
    gray = int(0.299 * r + 0.587 * g + 0.114 * b)
    # 灰度值和字符串的对应关系
    # 每个字符串对应灰度值的区间是
    unit = (256.0 + 1)/length
    # 找到灰度值所对应字符串的下标
    index = int(gray/unit)
    return ASCII_CHAR[index]


def image_to_ascii_chart(image):
    width, height = image.size
    text = ''
    for y in range(0,height,10):
        line = ''
        for x in range(0,width,5):
            # 找到对应位置的像素点
            dot = image.getpixel((x, y))
            line += rgb_to_ascii(*dot)
        text += line
        text += '\n'
    return text

# 每个图转化为字符串
import os
files = os.listdir('images')
xxx = []
for i in range(0,len(files)):
    pic = Image.open(f'images/{i}.png').convert('RGB')
    xxx.append(image_to_ascii_chart(pic))


def Start():
    os.system("clear")
    print('Press any key...')
    input()
    os.system("clear")
    i=0
    print(xxx[i])
    c = input()
    while c != 'q':
        os.system("clear")
        print(xxx[i])
        c = input()
        i=i+1
    print('End')



Start()


