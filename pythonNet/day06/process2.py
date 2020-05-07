#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author      :   朱昭明
@File        :   process2.py
@Create Time :   2020/5/7 9:10 下午    
@Contact     :   18327510516@163.com
@License     :   (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
@version     :   v1.0

@Desciption  : 
  
"""

from multiprocessing import Process
from time import sleep
import os


def th1():
    sleep(3)
    print("吃饭")
    print(os.getppid(), '------', os.getpid())


def th2():
    sleep(2)
    print("睡觉")
    print(os.getppid(), '------', os.getpid())


def th3():
    sleep(2)
    print("打豆豆")
    print(os.getppid(), '------', os.getpid())


things = [th1, th2, th3]
jobs = []

if __name__ == '__main__':
    for th in things:
        p = Process(target=th)
        # 用列表保存进程对象
        jobs.append(p)
        p.start()

    for i in jobs:
        i.join()
