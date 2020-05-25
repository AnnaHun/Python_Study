#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : poll_server.py
    @Software    : PyCharm
    @Create Time : 2020/5/25 3:56 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Descriptions: poll多路复用
  
"""
from socket import *
from select import *

# 创建关注的io
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(5)

# 创建poll对象
p = poll()

# 建立查找地图{fileno:io_obj}
fdmap = {s.fileno(): s}

# 设置关注io
p.register(s, POLLIN | POLLERR)

# 循环监控io事件发生
while True:
    # 阻塞监控的,阻塞等待io发生
    events = p.poll()
    # 遍历列表处理io
    for fd, event in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("connect from ", addr)
            # 添加新的关注事件
            p.register(c, POLLIN | POLLHUP)
            fdmap[c.fileno()] = c
        elif event & POLLHUP:
            print("客户端退出")
            # 取消关注
            p.unregister(fd)
            fdmap[fd].close()
            # 从字典删除
            del fdmap[fd]
        # 客户端发消息
        elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            print(data.decode())
            fdmap[fd].send(b'ok')
