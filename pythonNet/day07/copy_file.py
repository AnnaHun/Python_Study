#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : copy_file.py
    @Software    : PyCharm
    @Create Time : 2020/5/10 12:34 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Desciption  : 
  
"""

from multiprocessing import Process
import os

filename = './teacher_cang.jpg'

# 获取图片大小
size = os.path.getsize(filename)


# 复制上半部分
def top():
    f = open(filename, 'rb')
    n = size // 2
    fw = open('top.jpg', 'wb')
    fw.write(f.read(n))
    f.close()
    fw.close()


# 复制下半部分
def bot():
    f = open(filename, 'rb')
    fw = open('top.jpg', 'wb')
    f.seek(size // 2)
    while True:
        data = f.read(1024)
        if not data:
            break
        fw.write(data)
        f.close()
        fw.close()

if __name__ == '__main__':

    t = Process(target=top)
    b = Process(target=bot)

    t.start()
    b.start()
    t.join()
    b.join()
