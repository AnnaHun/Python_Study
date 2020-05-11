#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : thread_class.py
    @Software    : PyCharm
    @Create Time : 2020/5/10 3:34 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Desciption  : 
  
"""

from threading import Thread


class ThreadClass(Thread):
    def __init__(self, attr):
        self.attr = attr
        super(ThreadClass, self).__init__()

    # 多个方法配合实现具体功能
    def f1(self):
        print("步骤1")

    def f2(self):
        print("步骤2")

    def run(self):
        self.f1()
        self.f2()


t = ThreadClass("xxxxxxx")
t.start()
t.join()
