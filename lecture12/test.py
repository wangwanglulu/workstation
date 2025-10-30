from pathlib import Path
import csv

file_path = Path("sitka_weather_07-2021_simple.csv")
with file_path.open("r", encoding="utf-8") as file:  # 指定编码
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)  # 逐行处理
