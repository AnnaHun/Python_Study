#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : fork_service.py
    @Software    : PyCharm
    @Create Time : 2020/5/13 10:10 上午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Descriptions: 基于fork的多进程网络并发
  
"""
from socket import *
import os, sys
import signal

# 创建监听套接字
HOST = '106.14.213.53'
PORT = 8888
ADDR = (HOST, PORT)
s = socket()  # tcp套接字
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 设置端口地址重用
s.bind(ADDR)
s.listen(3)

# 僵尸进程的处理
# 忽略子进程的退出信号
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

print("Lidten the port 8888---------------------------")


def handle(c):
    print("客户端：", c.getpeername())
    while True:
        data = c.recv()
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
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue

    # 创建子进程处理客户端请求
    pid = os.fork()
    if pid == 0:
        s.close()  # 子进程不需要父进程的套接字
        handle(c)
        os._exit(0)
        # 父进程实际只用来处理客户端连接
    else:
        c.close()  # 父进程不需要子进程的套接字
