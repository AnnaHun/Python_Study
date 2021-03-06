#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : Python_Study
    @File        : lock_1.py
    @Software    : PyCharm
    @Create Time : 2020/5/11 11:33 上午
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0

    @Desciption  :

"""

import time
import threading


# 交易类
class Account:
    def __init__(self, _id, balance, lock):
        self.id = _id
        self.balance = balance
        self.lock = lock

    # 取钱
    def withdraw(self, amount):
        self.balance -= amount

    # 存钱
    def deposit(self, amount):
        self.balance += amount

    # 查看账户金额
    def get_balance(self):
        return self.balance


# 　转账函数
def transfer(from_, to, amount):
    # 上锁成功返回Ｔｒｕｅ
    if from_.lock.acquire():  # 锁住自己的账户
        from_.withdraw(amount)  # 自己账户金额减少
        time.sleep(0.5)
        if to.lock.acquire():  # 对方账户上锁
            to.deposit(amount)  # 对方账户金额增加
            to.lock.release()  # 对方账户解锁
        from_.lock.release()  # 自己账户解锁
    print("转账完成")


# 创建两个账户
Abby = Account('Abby', 5000, threading.Lock)
Levi = Account('Levi', 3000, threading.Lock)

t = threading.Thread(target=transfer, args=(Abby, Levi, 1500))
t.start()
time.sleep(2)
t.join()
print("Abby", Abby.get_balance())
print("Levi", Levi.get_balance())
