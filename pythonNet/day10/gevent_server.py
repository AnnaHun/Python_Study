#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : gevent_server.py
    @Software    : PyCharm
    @Create Time : 2020/5/26 11:47 上午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Descriptions: gevent协程演示

"""
import gevent
from gevent import monkey  # 该剧执行在导入socket之前
from socket import *

monkey.patch_all()

# 创建套接字
s = socket()
s.bind(('0.0.0.0', 8888))
s.listen(5)


def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'ok')
    c.close()


while True:
    c, addr = s.accept()
    print("connect from ...", addr)
    # handle(c)     循环方案
    gevent.spawn(handle,c)  #协程方案

s.close()
