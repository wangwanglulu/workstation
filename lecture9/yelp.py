# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pathlib import Path
import json

path = Path('yelp_sample.json')
contents = path.read_text()
lines = contents.splitlines()
yelp = []
for line in lines:
    yelp.append(json.loads(line))
    
print(len(yelp))
print(yelp[100])
