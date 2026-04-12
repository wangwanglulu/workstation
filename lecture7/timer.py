# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 09:44:15 2026

@author: Lu
"""
import time
def countdown(seconds):
    while seconds >= 0:
        print(f"\r剩余：{seconds:02d} 秒", end="", flush=True)
        time.sleep(1)
        seconds -= 1
    print("\n时间到！")
count = 1
def pomodoro(x):
    global count
    while count <=x:
        print(f"第{count}轮")
        if count>1 and count %4 == 0:
            countdown(2)
            countdown(3)
        else:
            countdown(2)
            countdown(2)
        count += 1
    
pomodoro(4)
