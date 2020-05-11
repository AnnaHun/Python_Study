#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : thread1.py
    @Software    : PyCharm
    @Create Time : 2020/5/10 2:54 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Desciption  : 线程示例
  
"""

import threading
from time import sleep
import os

a = 1


# 线程函数
def music():
    global a
    print("a=", a)
    a = 10000
    for i in range(5):
        sleep(2)
        print(os.getpid(), "播放心如止水")


# 创建线程对象
t = threading.Thread(target=music)
t.start()
for i in range(3):
    sleep(3)
    print(os.getpid(), "跳舞吧")

t.join()

print("main thread a=", a)
