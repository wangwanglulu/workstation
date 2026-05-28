#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 12:58:16 2023

@author: wangwanglulu
"""

# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI(api_key="sk-2356f259ef8f42628664c056553c250d", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "鲁迅暴打周树人"},
    ],
    stream=False
)

print(response.choices[0].message.content)

