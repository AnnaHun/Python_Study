from socket import *

s = socket()
s.connect(('0.0.0.0', 8888))
f = open('cxk,jpg', 'rb')

while True:
    data = f.read(1024)
    if not data:
        break
    s.send(data)

f.close()
s.close()
