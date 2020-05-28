#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : ecerP.py
    @Software    : PyCharm
    @Create Time : 2020/5/28 4:52 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Descriptions: 
  
"""
import re
import sys

port = sys.argv[1]

f = open('1.txt')
# 找到port段落
while True:
    data = ''
    for line in f:
        if line != '\n':  # 不是空行
            data += line
        else:
            break
    print(">>>>>>", data)
    if not data:
        print("not found the %s" % port)
        break

    # 匹配字符串首个单词
    key_word = re.match(r'\S+', data).group()
    if port == key_word:
        pattern = r'[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}'
        try:
            address = re.search(pattern, data).group()
            print(address)
            break
        except:
            print("not found the %s" % port)
            break