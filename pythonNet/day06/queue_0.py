#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : queue_0.py
    @Software    : PyCharm
    @Create Time : 2020/5/9 2:03 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Desciption  : 
  
"""

from multiprocessing import Queue, Process
from time import sleep
from random import randint

if __name__ == '__main__':


    q = Queue(5)


    def request():
        for i in range(20):
            x = randint(0, 100)
            y = randint(0, 100)
            q.put(x, y)


    def handle():
        while True:
            sleep(0.5)
            try:
                x, y = q.get(timeout=3)
            except:
                break
            print(x, y, x + y)


    p1 = Process(target=request)
    p2 = Process(target=handle)

    p1.start()
    p2.start()
    p1.join()
    p2.join()
