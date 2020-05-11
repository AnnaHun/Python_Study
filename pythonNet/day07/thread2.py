#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : thread2.py
    @Software    : PyCharm
    @Create Time : 2020/5/10 3:07 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Desciption  : 
  
"""

from threading import Thread
from time import sleep


# 含有参数的线程函数
def fun(sec, name):
    print("线程函数传递参数")
    sleep(sec)
    print("%s  线程执行完毕" % name, '\n')


jobs = []
# 创建多个线程
for i in range(5):
    t = Thread(target=fun, args=(2,), kwargs={'name': 'T%d' % i})
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()
