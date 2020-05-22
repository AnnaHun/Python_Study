#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : select_test.py
    @Software    : PyCharm
    @Create Time : 2020/5/20 10:19 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Descriptions: 
  
"""
from select import select
from socket import *


# 创建几个io用做监控
s=socket()
s.bind(('0.0.0.0',8888))
s.listen(3)

print("开始提交监控的io")
rs,ws,xs=select([s],[],[])

print(rs)
print(ws)
print(xs)
