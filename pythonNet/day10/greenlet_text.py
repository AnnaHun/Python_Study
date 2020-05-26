#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : greenlet_text.py
    @Software    : PyCharm
    @Create Time : 2020/5/26 10:42 上午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Descriptions: 
  
"""

from greenlet import greenlet
import gevent


def test1():
    print("执行test1")
    gr2.switch()
    print("结束test1")
    gr2.switch()


def test2():
    print("执行test2")
    gr1.switch()
    print("结束test2")


# 将函数变成协程函数
gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()  # 执行协程test1
