#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : select_service.py
    @Software    : PyCharm
    @Create Time : 2020/5/24 4:57 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Descriptions: IO多路复用select实现多客户端通讯
  
"""

from socket import *
from select import select

# 设置套接字为关注io
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(5)

# 设置关注的io
rlist = [s]
wlist = []
xlist = []

while True:
    # 监控io的发生
    rs, ws, xs = select(rlist, wlist, xlist)
    # 遍历三个返回值列表，判断哪个io发生
    for r in rs:
        if r is s:
            c, addr = r.accept()
            print("connect from ", addr)
            rlist.append(c)  # 加入新的关注io
    for w in ws:
        pass
    for x in xs:
        pass
