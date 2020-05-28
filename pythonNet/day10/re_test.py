#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : re_test.py
    @Software    : PyCharm
    @Create Time : 2020/5/27 11:58 上午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Descriptions: 
  
"""
import re

s='Levi:1994,Sunny:1993'
pattern=r'\w+:\d+'

# l=re.findall(  pattern,s)
# print(l)

# compile对象调用
regex=re.compile(pattern)
l=regex.findall(s)
print(l)