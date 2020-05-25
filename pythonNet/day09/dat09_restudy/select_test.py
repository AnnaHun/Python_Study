#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : select_test.py
    @Software    : PyCharm
    @Create Time : 2020/5/24 4:16 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0

    @Descriptions: select函数讲解
"""
from socket import *
from select import select

fd = open('lot.txt', 'a+')
# 创建几个io用做监控
s = socket()
s.bind(('0.0.0.0', 8888))
s.listen(3)

print("start io")
rs, ws, xs = select([s,fd], [fd], [], 3)

print("rs:", rs)
print("ws:", ws)
print("xs:".xs)
