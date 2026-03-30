from pathlib import Path
path = Path('comment.txt')
contents = path.read_text()

words = ["bad", "boring", "awful", "terrible"]


#转化小写
text = contents.lower()

# 去除标点（只保留字母和空格）
cleaned_text = ""
for char in text:
    if char.isalpha() or char.isspace():
        cleaned_text += char # cleaned_text = cleaned_text + char




