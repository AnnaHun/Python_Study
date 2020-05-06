import time

fd = open("test", "r")

# data = fd.read()
# 当文件较大，不适合用read

# while True:
#     data = fd.read(8)
#     if not data:
#         break
#     print(data)

# data1=fd.readline()
data=fd.readlines()
for line in data:
    print(line)
# print(data)
fd.close()
