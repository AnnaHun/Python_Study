#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : dead_lock1.py
    @Software    : PyCharm
    @Create Time : 2020/5/11 1:45 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Descriptions:

"""

from threading import Thread, RLock
import time

num = 0
lock = RLock()  # 在一个线程内可以对锁进行重复加锁


class MyThread(Thread):
    def fun1(self):
        global num
        with lock:
            num -= 1

    def fun2(self):
        global num
        if lock.acquire():
            num += 1
            if num > 5:
                self.fun1()
            print("Num=", num)
            lock.release()

    def run(self):
        while True:
            time.sleep(2)
            self.fun2()


for i in range(10):
    t = MyThread()
    t.start()
