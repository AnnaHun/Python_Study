#!/usr/bin/python2.7
# -*- encoding: utf-8 -*-
"""
@Author      : 朱昭明 -- apple
@Project     : Python_Study
@File        : pipe.py
@Software    : PyCharm
@Create Time : 2020/5/8 1:11 下午    
@Contact     : 18327510516@163.com
@License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
@version     :  v1.0

@Desciption  : 
  
"""
from multiprocessing import Process, Pipe
import os, time

# 创建管道
fd1, fd2 = Pipe()


def fun(name):
    time.sleep(3)
    # 向管道写入内容
    fd1.send({name: os.getpid()})


if __name__ == '__main__':

    jobs = []
    for i in range(5):
        p = Process(target=fun, args=(i,))
        jobs.append(p)
        p.start()

    for i in range(5):
        # 读取管道
        data = fd2.recv()
        print(data)

    for i in jobs:
        i.join()
