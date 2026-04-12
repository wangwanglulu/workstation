# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:38:13 2026

@author: Lu
"""
import time
from playsound import playsound

def countdown(seconds):
    while seconds >= 0:
        print(f"\r剩余：{seconds:02d} 秒", end="", flush=True)
        time.sleep(1)
        seconds -= 1

    print("\n时间到！")
    playsound("dismiss.mp3")
countdown(3)

