from socket import *

s = socket()
print("地址类型", s.family)
print("套接字类型", s.type)
