#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : sem.py
    @Software    : PyCharm
    @Create Time : 2020/5/10 12:00 下午
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0

    @Desciption  :

"""

from multiprocessing import Semaphore, Process
from time import sleep
import os

# 创建信号量
# 服务程序最多允许三个进程同时执行事件
sem = Semaphore(3)


def handle():
    print("%d 想执行时间" % os.getpid())
    # 想执行必须获取信号量
    sem.acquire()
    print("%d 开始执行操作" % os.getpid())
    sleep(3)
    print("%d 完成操作" % os.getpid())
    # 增加信号量
    sem.release()


jobs = []
for i in range(5):
    p = Process(target=handle)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()

print(sem.get_value())
