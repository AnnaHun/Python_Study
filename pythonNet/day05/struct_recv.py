from socket import *
import struct

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('0.0.0.0', 8888))

st = struct.Struct('i32sif')

f = open('student.txt', 'a+')

while True:
    data, addr = s.recvfrom(1024)
    data = st.unpack(data)
    # 整理写入内容
    info = "%d %s %d %.2f \n" % (data[0], data[1].decode(), data[2], data[3])
    f.write(info)
    print(info)

s.close()
f.close()