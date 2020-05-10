#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : value.py
    @Software    : PyCharm
    @Create Time : 2020/5/9 6:42 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Desciption  : 
  
"""

from multiprocessing import Process, Value
import time
import random

# 创建共享内存
money = Value("i", 5000)


# 操作共享内存
def man():
    for i in range(30):
        time.sleep(0.2)
        money.value += random.randint(1, 1000)


def girl():
    for i in range(30):
        time.sleep(0.15)
        money.value -= random.randint(100, 800)


m = Process(target=man)
g = Process(target=girl)

m.start()
g.start()

m.join()
g.join()

print("一月剩余额度：", money.value)
