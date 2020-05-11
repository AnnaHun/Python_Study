#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : thread_lock.py
    @Software    : PyCharm
    @Create Time : 2020/5/11 10:41 上午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Desciption  : 
  
"""

from threading import Thread, Lock

a = b = 0
lock = Lock()


def value():
    while True:
        lock.acquire()  # 上锁
        if a != b:
            print("a=%d,b=%d" % (a, b))
        lock.release()  # 解锁


t = Thread(target=value)
t.start()
while True:
    with lock:
        a += 1
        b += 1
t.join()
 