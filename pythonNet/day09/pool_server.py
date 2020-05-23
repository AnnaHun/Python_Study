#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : pool_server.py
    @Software    : PyCharm
    @Create Time : 2020/5/21 9:28 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Descriptions: 
  
"""

from socket import *
from select import *

# 创建关注的io
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(5)

# 创建pool对象
p = poll()

# 建立查找字典{fileno : io_obj}
fdmap = {s.fileno(): s}

# 设置关注io
p.register(s, POLLIN | POLLERR)

# 循环监控io事件发生
while True:
    events = p.poll()  # 阻塞等待io发生
    # 遍历列表处理io
    for fd, event in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("connect from :", addr)
            # 添加新的关注事件
            p.register(c, POLLIN | POLLHUP)
            fdmap[c.fileno()] = c
        elif event & POLLHUP:  # 客户端断开
            print("客户端退出")
            p.unregister(fd)  # 取消关注
            fdmap[fd].close()
            del fdmap[fd]  # 从字典删除
            continue
        elif event & POLLIN:  # 客户端发消息
            data = fdmap[fd].recv(1024)
            if not data:
                continue
            print(data.decode())
            fdmap[fd].send(b'ok')
