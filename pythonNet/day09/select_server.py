#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : select_server.py
    @Software    : PyCharm
    @Create Time : 2020/5/21 9:27 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Descriptions: 
  
"""


from socket import *
from select import select

#　设置套接字为关注ＩＯ
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

# 设置关注的ＩＯ
rlist = [s]
wlist = []
xlist = []

while True:
    #　监控ＩＯ的发生
    rs,ws,xs = select(rlist,wlist,xlist)
    # 遍历三个返回值列表，判断哪个ＩＯ发生
    for r in rs:
        #　如果是套接字就绪则处理链接
        if r is s:
            c,addr = r.accept()
            print("Connect from",addr)
            rlist.append(c) #　加入新的关注ＩＯ
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            # r.send(b'OK')
            #　希望我们主动处理这个ＩＯ
            wlist.append(r)

    for w in ws:
        w.send(b'Ok,Thanks')
        wlist.remove(w)
    for x in xs:
        pass


