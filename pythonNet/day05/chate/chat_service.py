"""
chat room
env :python3.5
socket fork练习
"""

from socket import *
import os, sys

# 服务器地址
ADDR = ('0.0.0.0', 8888)

# 创建用户信息
user = {}


def do_login(s, name, addr):
    if name in user:
        s.sendto("该用户已经存在".encode(), addr)
        return
    s.sendto(b'ok', addr)

    # 通知其他人
    msg = "欢迎%s进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])

    # 将用户加入
    user[name] = addr


# 接受各种客户端请求
def do_request(s):
    while True:
        data, addr = s.recvfrom(1024)
        msg = data.decode().split(" ")
        if msg[0] == "L":
            do_login(s, msg[1], addr)
        elif msg[0] == "C":
            do_chat()


# 创建网络连接
def main():
    # 套接字
    s = socket(AF_INET, SOCK_DGRAM)  # UDP套接字
    s.bind(ADDR)

    # 请求处理
    do_request(s)  # 处理客户端请求


def do_chat():
    pass


if __name__ == "__main__":
    main()
