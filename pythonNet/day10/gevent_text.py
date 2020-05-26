#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : gevent_text.py
    @Software    : PyCharm
    @Create Time : 2020/5/26 10:57 上午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Descriptions: 
  
"""

import gevent
import time


def foo(a, b):
    print("runinig foo .....", a, b)
    gevent.sleep(2)
    print("foo again")


def bar():
    print("running bar .....")
    gevent.sleep(3)
    print("bar again")


# 将函数封装为携程，遇到gevent阻塞自动执行
f = gevent.spawn(foo, 1, 'hello')
g = gevent.spawn(bar)

gevent.joinall([f, g])
