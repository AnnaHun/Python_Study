#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : array_0.py
    @Software    : PyCharm
    @Create Time : 2020/5/10 11:10 上午
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0

    @Desciption  :

"""
from multiprocessing import Process, Array

# 创建共享内存
# 共享内存开辟五个整形列表空间
# shm = Array('i', [1, 2, 3])
shm = Array('c', b'hello')


def fun():
    for i in shm:
        print(i)
    shm[0] = b'H'


p = Process(target=fun)
p.start()
p.join()

for i in shm:
    print(i, end=" ")

print(shm.value)
