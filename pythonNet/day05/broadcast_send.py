"""
广播发送
"""
from socket import *
from time import sleep

dest = ('192.168.0.103', 9999)

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

data = """
    ********************************
    5.5 深圳  初夏
    喜欢夏天，但你比夏天更加明媚
    ********************************
"""

while True:
    sleep(2)
    s.sendto(data.encode(), dest)

s.close()
