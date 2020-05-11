#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : thread_attr.py
    @Software    : PyCharm
    @Create Time : 2020/5/10 3:15 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Desciption  : 
  
"""

from threading import Thread
from time import sleep


def fun():
    sleep(3)
    print("线程属性测试")


# 线程名称
t = Thread(target=fun, name="Tarena")
# 主线程退出，分支线程也退出
t.setDaemon(True)
t.start()

t.setName("Tedu")
print("thread name:", t.getName())

# 线程生命周期
print("is alive :", t.is_alive())
