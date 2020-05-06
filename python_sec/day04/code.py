s = input(">>")
# 字符串--〉字节串
byte = s.encode()
# 字节串--〉字符串
s = byte.decode()
print("str:", s)
print("bytes:", s.encode())
print("bytes:", b"Hello World")

print("int 1",bytes([1,2,3,4]))
