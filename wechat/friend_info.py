# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 11:22:46 2018

@author: LU WANG
"""
import itchat
itchat.auto_login()

friends = itchat.get_friends(update=True)[0:]
print(friends)

male = 0
female = 0
other = 0

for i in friends[1:]:
    sex = i['Sex']
    if sex == 1:
        male = male + 1
    elif sex ==2:
        female = female + 1
    else:
        other = other + 1

total = len(friends[1:])

print('男性好友： {}%'.format(male/total*100))
print('女性好友： {}%'.format(female/total*100)) 
print('其他： {}%' .format(other/total*100))

itchat.logout() 