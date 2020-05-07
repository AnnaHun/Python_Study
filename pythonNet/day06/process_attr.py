#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author      :   朱昭明
@File        :   process_attr.py
@Create Time :   2020/5/7 9:43 下午    
@Contact     :   18327510516@163.com
@License     :   (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
@version     :   v1.0

@Desciption  : 
  
"""

from multiprocessing import Process
from time import sleep, ctime


def tm():
    for i in range(3):
        sleep(2)
        print(ctime())


if __name__ == '__main__':
    p = Process(target=tm, name='Tedua')
    p.daemon = True
    p.start()
    # 获取进程名称
    print("Name:", p.name)
    # 获取进程pid
    print("PID:", p.pid)
    # 判断进程是否在生命周期
    print("is alive :", p.is_alive())
