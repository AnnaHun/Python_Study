#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author      :   朱昭明
@File        :   process1.py
@Create Time :   2020/5/7 8:51 下午
@Contact     :   18327510516@163.com
@License     :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@version     :   v1.0

@Desciption  :

"""

import multiprocessing as mp
from time import sleep

a = 1


def fun():
    """
    子进程函数
    :return:
    """
    print("子进程开始执行")
    global a
    print("a=", a)
    a = 10000
    sleep(3)
    print("子进程执行完毕")


if __name__ == '__main__':
    # 创建进程对象
    p = mp.Process(target=fun)

    # 启动进程
    p.start()

    sleep(2)
    print("父进程干点事")

    # 回收进程
    p.join()

    print("parent a:", a)
