#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : block_io.py
    @Software    : PyCharm
    @Create Time : 2020/5/13 9:41 PM    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Descriptions: 套接字非阻塞示例
   
"""
from socket import *
from time import sleep, ctime

# 日志文件
f = open('log.txt', 'a+')

# tcp套接字
sockfd = socket()
sockfd.bind(('0.0.0.0', 8888)) 
sockfd.listen(3)
sockfd.settimeout(3)

# 设置套接字为非阻塞
# sockfd.setblocking(False)
while True:
    print("waiting for connect")
    try:
        connfd, addr = sockfd.accept()
    except (BlockingIOError, timeout) as e:
        sleep(2)
        f.write('%s:%s\n' % (ctime(), e))

    data = connfd.recv(1024).decode()
    print(data)
