#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author      :   朱昭明
@File        :   process3.py
@Create Time :   2020/5/7 9:36 下午    
@Contact     :   18327510516@163.com
@License     :   (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
@version     :   v1.0

@Desciption  : 
  
"""
from multiprocessing import Process
from time import sleep


def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I`m %s" % name)
        print("I`m working")


if __name__ == '__main__':
    # p = Process(target=worker, args=(2, "Rouse"))
    p=Process(target=worker,kwargs={'name':'Rouse','sec':2})
    p.start()
    p.join()
