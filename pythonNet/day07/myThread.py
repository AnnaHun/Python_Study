#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : myThread.py
    @Software    : PyCharm
    @Create Time : 2020/5/10 3:42 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Desciption  : 
  
"""

from threading import Thread
from time import sleep, ctime


# 继承thread类
class MyThread(Thread):
    def __init__(self, target=None, args=(), kwargs={}, name="tedu"):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.name = name

    # 重写父类的run方法 - ---thread的run方法
    def run(self):
        self.target(*self.args, **self.kwargs)


def player(sec, song):
    for i in range(2):
        print("Playing %s:%s" % (song, ctime()))
        sleep(sec)


t = MyThread(target=player, args=(3,), kwargs={'song': '凉凉'}, name='happy')

t.start()
t.join()
