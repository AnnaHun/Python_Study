#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : thread_event.py
    @Software    : PyCharm
    @Create Time : 2020/5/11 10:12 上午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Desciption  : 
  
"""

from threading import Thread, Event
from time import sleep

# 全局变量用于通讯
s = None
# 事件对象
e = Event()


def yangzirong():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    # 共享资源操作完毕 
    e.set()


t = Thread(target=yangzirong)
t.start()

print("说对口令就是自己人")
# 阻塞等待
e.wait()
if s == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神，你是对的人")
else:
    print("拖出去斩了")
t.join()
