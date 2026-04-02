# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 1. 加载成语词典
from pathlib import Path
path = Path('idiom_dictionary.txt')
contents = path.read_text()
lines = contents.splitlines()
d_game={}
for index, line in enumerate(lines):
    if line!="":
        endpoint=line.find("拼音")
        if endpoint == -1:
            print(index)
