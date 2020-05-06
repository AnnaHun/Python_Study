from socket import *

s = socket()
s.bind(('0.0.0.0', 8000))
s.listen(3)

c, addr = s.accept()
print("connetc from ", addr)
data = c.recv(4096)
print(data)

# http响应格式
data = """HTTP/1.1 200 OK
Content-Type:text/html
    
<h1>hello world</h1>
"""
c.send(data.encode())

c.close()
s.close()
