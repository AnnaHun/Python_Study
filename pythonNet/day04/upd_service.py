"""
upd套接字
"""

from socket import *

sockfd = socket(AF_INET, SOCK_DGRAM)
server_addr = ('127.0.0.1', 8888)
sockfd.bind(server_addr)

while True:
    data, addr = sockfd.recvfrom(1024)
    print("收到的消息:", data.decode())
    sockfd.sendto("Thanks".encode(), addr)

sockfd.close()
