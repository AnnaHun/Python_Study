list01 = [3,5,6,7,9]
list02 = []
for item in list01:
    list02.append(item ** 2)

print(list02)

# 列表推导式
# [对变量的操作 for 变量名 in 可迭代对象]
list03 = [ item ** 2 for item in list01]
print(list03)

list04 = [item ** 2 for item in list01 if item % 2 == 0]
print(list04)
