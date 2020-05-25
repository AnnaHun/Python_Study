#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : yield.py
    @Software    : PyCharm
    @Create Time : 2020/5/25 5:33 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Descriptions: 
  
"""
def fun():
    print("启动器生成")
    yield 1
    print("生成器完成")

fun()

for i in fun():
    print(i)