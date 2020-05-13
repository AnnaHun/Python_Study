#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : single.py
    @Software    : PyCharm
    @Create Time : 2020/5/12 1:56 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Descriptions: 
  
"""

from text import *
import time
import threading

#
# st = time.time()
#
# for i in range(10):
#     count(1, 1)
#
# print("Single CPU:", time.time() - st)
jobs = []
st = time.time()
for i in range(10):
    t = threading.Thread(target=count, args=(1, 1))
    jobs.append(t)

# for i in jobs:
#     i.join()

print("Thread cpu:", time.time() - st)
