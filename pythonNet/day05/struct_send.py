from socket import *
import struct

ADDR = ('0.0.0.0', 8888)
# 规定数据格式
st = struct.Struct('i32sif')
s = socket(AF_INET, SOCK_DGRAM)

while True:
    print("================================")
    id = int(input("ID:"))
    name = input("NAME:").encode()
    age = int(input("AGE:"))
    score = float(input("SCORE:"))
    data = st.pack(id, name, age, score)
    s.sendto(data, ADDR)

s.close()
