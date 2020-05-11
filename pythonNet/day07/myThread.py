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


class MyThread(Thread):
    pass


# *****************************************
def player(sec, song):
    for i in range(2):
        print("Playing %s:%s" % (song, ctime()))
        sleep(sec)


t = MyThread(target=player, args=(3,), kwargs={'song': '凉凉'}, name='happy')

t.start()
t.join()
