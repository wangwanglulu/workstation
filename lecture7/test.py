# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:38:13 2026

@author: Lu
"""
import random
ranks = list(map(str, [value for value in range(2, 15)]))
suits = ["\u2660", "\u2665", "\u2663", "\u2666"]
deck = [y + x for x in ranks for y in suits]

random.shuffle(deck)

# 简化处理，一次性发了7张
hand = [deck.pop() for x in range(7)]
print(hand)
all = [c[0] for c in hand]
max_suits = [all.count(x) for x in suits]
if max(max_suits) >=5:
    print("Yes")
else:
    print("No")