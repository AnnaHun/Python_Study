#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : teat.py
    @Software    : PyCharm
    @Create Time : 2020/5/12 1:12 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Descriptions: 
  
"""
import socketserver


def count(x, y):
    c = 0
    while c < 70000000:
        c += 1
        x += 1
        y += 1


def io():
    write()
    read()


def write():
    f = open('test', 'w')
    for i in range(1500000):
        f.write("hello world \n")
    f.close()


def read():
    f = open('test')
    lines = f.readlines()
    f.close()
