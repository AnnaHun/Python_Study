#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : unix_send.py
    @Software    : PyCharm
    @Create Time : 2020/5/10 11:46 上午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Desciption  : 本地套接字传输客户端
  
"""

from socket import *

# 确保两边使用相同的套接字文件
sock_file = './sock'

sockfd = socket(AF_UNIX, SOCK_STREAM)
sockfd.connect(sock_file)

while True:
    msg = input(">>")
    if not msg:
        break
    sockfd.send(msg.encode())
sockfd.close()
