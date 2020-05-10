#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : unix_recv.py
    @Software    : PyCharm
    @Create Time : 2020/5/10 11:38 上午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Desciption  : 本地套接字服务端
  
"""

from socket import *
import os

# 确定本地套接字文件
sock_file = './sock'

# 判断文件是否存在，存在就删除
if os.path.exists(sock_file):
    os.remove(sock_file)
# 创建本地套接字
sockfd = socket(AF_UNIX, SOCK_STREAM)

# 绑定本地套接字
sockfd.bind(sock_file)

# 监听，连接
sockfd.listen(3)
while True:
    c, addr = sockfd.accept()
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
    c.close()
sockfd.close()
