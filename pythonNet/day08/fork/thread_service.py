#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : thread_service.py
    @Software    : PyCharm
    @Create Time : 2020/5/13 11:39 上午
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0

    @Descriptions: 多线程网络并发

"""
from socket import *
from threading import Thread
import sys

# 创建监听套接字
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)


# 客户端处理
def handle(c):
    print("connect from ", c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'ok')
    c.close()


# 循环等待客户端连接
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("退出服务器")
    except Exception as e:
        print(e)
        continue

    # 创建新的线程处理客户端
    t = Thread(target=handle, args=(c,))
    t.start()
    t.setDaemon(True)  # 主线程退出，分支线程也退出


