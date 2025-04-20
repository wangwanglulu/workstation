# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
from pathlib import Path
from textblob import TextBlob 


folder_path = "marvel/"
summary = []

for filename in os.listdir(folder_path):
    path = Path(os.path.join(folder_path, filename))
    contents = path.read_text(errors="ignore")
    lines = contents.splitlines()
    scores = []

    for line in lines:
        line = line.strip()
        if line:
            polarity = TextBlob(line).sentiment.polarity
            scores.append(polarity) 

    if scores:
        average = sum(scores) / len(scores)
        summary.append((average, filename))

summary.sort()
for score, movie in summary:
    print(movie, score)
