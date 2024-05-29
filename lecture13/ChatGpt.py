#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 12:58:16 2023

@author: wangwanglulu
"""


from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="sk-YZFYlSZtjmx7n02gGGDwI0z2GPQPWbgBoDL06nB8Nbin6xQB",
    base_url="https://api.chatanywhere.tech/v1"
    # base_url="https://api.chatanywhere.cn/v1"
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": '鲁迅为什么暴打周树人'}
  ]
)

print(completion.choices[0].message)