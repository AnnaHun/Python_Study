#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author      :   朱昭明
@File        :   pool.py
@Create Time :   2020/5/7 10:05 下午    
@Contact     :   18327510516@163.com
@License     :   (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
@version     :   v1.0

@Desciption  : 进程池原理示例
  
"""
from multiprocessing import Pool
from time import sleep, ctime


# 进程池事件
def worker(msg):
    sleep(2)
    print(msg)
    return ctime()


if __name__ == '__main__':
    # 创建进程池
    pool = Pool(6)

    # 向进程池添加事件
    for i in range(20):
        msg = 'Hello %d' % i
        r = pool.apply_async(func=worker, args=(msg,))

    # 关闭进程池
    pool.close()
    # 回收进程池---阻塞等待
    pool.join()
    print(r.get())  # 获取事件返回值
