#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : async_test.py
    @Software    : PyCharm
    @Create Time : 2020/5/25 6:12 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Descriptions: 
  
"""
import asyncio
import time

now = lambda: time.time()


async def do_work(x):
    print("Waiting:", x)
    await asyncio.sleep(x)
    return "Done after %s s" % x


start = now()
cor1 = do_work(1)
cor2 = do_work(2)
cor3 = do_work(3)

# 将协程对象生成一个可轮询操作的对象列表
tasks = [
    asyncio.ensure_future(cor1),
    asyncio.ensure_future(cor2),
    asyncio.ensure_future(cor3),
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print("time: ", now() - start)
