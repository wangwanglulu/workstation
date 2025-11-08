from pathlib import Path
import json
path = Path('season1.json')
contents = path.read_text()          # 读取整个文件为一个字符串
x = json.loads(contents)        # 按行拆分，每一行是一个独立的 JSON 对象字符串


print(x["Game Of Thrones S01E01 Winter Is Coming.srt"]["1"])
